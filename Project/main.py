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



def view_shipments():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM shipments")
    rows = cursor.fetchall()

    print("\n--- Shipments ---")
    for row in rows:
        print(row)

    conn.close()



def update_shipment():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    shipment_id = input("Enter shipment ID to update: ")
    new_status = input("Enter new status: ")

    cursor.execute("UPDATE shipments SET status = ? WHERE shipment_id = ?",
                   (new_status, shipment_id))

    conn.commit()
    conn.close()

    print("Shipment updated successfully")



def delete_shipment():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    shipment_id = input("Enter shipment ID to delete: ")

    cursor.execute("DELETE FROM shipments WHERE shipment_id = ?", (shipment_id,))

    conn.commit()
    conn.close()

    print("Shipment deleted successfully")



def search_shipment():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    order = input("Enter order number to search: ")

    cursor.execute("SELECT * FROM shipments WHERE order_number = ?", (order,))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No shipment found")

    conn.close()



def menu():
    while True:
        print("\n--- Logistics System ---")
        print("1. Add Shipment")
        print("2. View Shipments")
        print("3. Update Shipment")
        print("4. Delete Shipment")
        print("5. Search Shipment")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_shipment()
        elif choice == "2":
            view_shipments()
        elif choice == "3":
            update_shipment()
        elif choice == "4":
            delete_shipment()
        elif choice == "5":
            search_shipment()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice, try again")


menu()