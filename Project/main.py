import sqlite3


# Connect to database or creates it if it doesn't exist
conn = sqlite3.connect("logistics.db")

# Create a cursor that can be used to run SQL commands
cursor = conn.cursor()

print("Database connected successfully")


# Shipments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS shipments (shipment_id INTEGER PRIMARY KEY AUTOINCREMENT, order_number TEXT, sender TEXT, receiver TEXT,
                                      status TEXT, delivery_date TEXT, cost REAL)""")

def add_shipment():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    order = input("Order number: ")
    sender = input("Sender: ")
    receiver = input("Receiver: ")
    status = input("Status: ")
    delivery_date = input("Delivery date: ")
    cost = float(input("Cost: "))

    cursor.execute("INSERT INTO shipments (order_number, sender, receiver, status, delivery_date, cost) VALUES (?, ?, ?, ?, ?, ?)",
                   (order, sender, receiver, status, delivery_date, cost))

    conn.commit()
    conn.close()

    print("Shipment added successfully")

add_shipment()

# Drivers table
cursor.execute("""CREATE TABLE IF NOT EXISTS drivers (driver_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, 
                                                      license_number TEXT, phone TEXT)""")

# Vehicles table
cursor.execute("CREATE TABLE IF NOT EXISTS vehicles (vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT, capacity INTEGER, "
               "availability TEXT, driver_id INTEGER, FOREIGN KEY (driver_id) REFERENCES drivers(driver_id))")

# Warehouses table
cursor.execute("CREATE TABLE IF NOT EXISTS warehouses (warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT, location TEXT)")

# Inventory table
cursor.execute("CREATE TABLE IF NOT EXISTS inventory (item_id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT, quantity INTEGER, "
               "warehouse_id INTEGER, FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id))")

conn = sqlite3.connect("logistics.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in database:", tables)

conn.close()