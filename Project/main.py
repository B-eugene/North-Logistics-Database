import sqlite3


# Connect to database or creates it if it doesn't exist
conn = sqlite3.connect("logistics.db")

# Create a cursor that can be used to run SQL commands
cursor = conn.cursor()

print("Database connected successfully")


# Shipments table
cursor.execute("CREATE TABLE IF NOT EXISTS shipments (shipment_id INTEGER PRIMARY KEY AUTOINCREMENT, order_number TEXT, "
               "sender TEXT, receiver TEXT, status TEXT, delivery_date TEXT, cost REAL, driver_id INTEGER, "
               "FOREIGN KEY (driver_id) REFERENCES drivers(driver_id))")


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
    driver_id = int(input("Assign driver ID: "))

    cursor.execute("INSERT INTO shipments (order_number, sender, receiver, status, delivery_date, cost, driver_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
               (order, sender, receiver, status, delivery_date, cost, driver_id))

    conn.commit()
    conn.close()

    print("Shipment added successfully")



def view_shipments():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT shipments.shipment_id, shipments.order_number, shipments.status, drivers.name FROM shipments
                      LEFT JOIN drivers ON shipments.driver_id = drivers.driver_id""")

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



def shipment_reports():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    print("\n--- Shipment Reports ---")

    # Total shipments
    cursor.execute("SELECT COUNT(*) FROM shipments")
    total = cursor.fetchone()[0]
    print(f"Total shipments: {total}")

    # Delivered shipments
    cursor.execute("SELECT COUNT(*) FROM shipments WHERE status = 'Delivered'")
    delivered = cursor.fetchone()[0]
    print(f"Delivered shipments: {delivered}")

    # In transit shipments
    cursor.execute("SELECT COUNT(*) FROM shipments WHERE status = 'In Transit'")
    in_transit = cursor.fetchone()[0]
    print(f"In transit shipments: {in_transit}")

    # Show all delayed shipments
    print("\nDelayed shipments:")
    cursor.execute("SELECT * FROM shipments WHERE status = 'Delayed'")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("None")

    conn.close()



def add_inventory():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    item = input("Item name: ")
    quantity = int(input("Quantity: "))
    warehouse = int(input("Warehouse ID: "))

    cursor.execute("INSERT INTO inventory (item_name, quantity, warehouse_id) VALUES (?, ?, ?)",
                   (item, quantity, warehouse))

    conn.commit()
    conn.close()

    print("Inventory added successfully")



def view_inventory():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()

    print("\n--- Inventory ---")
    for row in rows:
        print(row)

    conn.close()



def add_driver():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    name = input("Driver name: ")
    license_number = input("License number: ")
    phone = input("Phone: ")

    cursor.execute("INSERT INTO drivers (name, license_number, phone) VALUES (?, ?, ?)",
                   (name, license_number, phone))

    conn.commit()
    conn.close()

    print("Driver added successfully")



def view_drivers():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM drivers")
    rows = cursor.fetchall()

    print("\n--- Drivers ---")
    for row in rows:
        print(row)

    conn.close()



def add_vehicle():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    capacity = int(input("Vehicle capacity: "))
    availability = input("Availability (Available/Not Available): ")
    driver_id = int(input("Assign driver ID: "))

    cursor.execute("INSERT INTO vehicles (capacity, availability, driver_id) VALUES (?, ?, ?)",
                   (capacity, availability, driver_id))

    conn.commit()
    conn.close()

    print("Vehicle added successfully")



def view_vehicles():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vehicles")
    rows = cursor.fetchall()

    print("\n--- Vehicles ---")
    for row in rows:
        print(row)

    conn.close()



def menu():
    while True:
        print("\n--- Logistics System ---")
        print("1. Add Shipment")
        print("2. View Shipments")
        print("3. Update Shipment")
        print("4. Delete Shipment")
        print("5. Search Shipment")
        print("6. Shipment Reports")
        print("7. Add Inventory")
        print("8. View Inventory")
        print("9. Add Driver")
        print("10. View Drivers")
        print("11. Add Vehicle")
        print("12. View Vehicles")
        print("13. Exit")

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
            shipment_reports()
        elif choice == "7":
            add_inventory()
        elif choice == "8":
            view_inventory()
        elif choice == "9":
            add_driver()
        elif choice == "10":
            view_drivers()
        elif choice == "11":
            add_vehicle()
        elif choice == "12":
            view_vehicles()
        elif choice == "13":
            print("Exiting system...")
            break
        else:
            print("Invalid choice, try again")




menu()