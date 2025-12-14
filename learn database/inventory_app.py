import sqlite3

# --- 1. DATABASE FUNCTIONS (The Workers) ---

def view_inventory():
    """Reads the database and prints the table."""
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    
    print("\n--- 📦 CURRENT STOCK ---")
    if len(items) == 0:
        print("(Warehouse is empty)")
    else:
        for item in items:
            # item[0]=Name, item[1]=Price, item[2]=Qty
            print(f"🔹 {item[0]} | Rp{item[1]:,.0f} | Stock: {item[2]}")
            
    connection.close()

def add_new_item():
    """Asks user for details and INSERTS a new row."""
    name = input("Item Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    
    # The SQL Command
    cursor.execute("INSERT INTO items VALUES (?, ?, ?)", (name, price, qty))
    
    connection.commit() # Save!
    connection.close()
    print(f"✅ Added {name} to warehouse.")

def buy_item():
    """Asks what was bought and UPDATES the stock (Decreases it)."""
    name = input("Which item are you buying? ")
    qty_bought = int(input("How many? "))
    
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    
    # 1. First, check if item exists!
    cursor.execute("SELECT quantity FROM items WHERE name = ?", (name,))
    result = cursor.fetchone()
    
    if result is None:
        print("❌ Error: Item not found!")
    else:
        current_stock = result[0]
        
        if current_stock < qty_bought:
            print(f"⚠️ Not enough stock! We only have {current_stock}.")
        else:
            # 2. If safe, UPDATE the database
            new_stock = current_stock - qty_bought
            cursor.execute("UPDATE items SET quantity = ? WHERE name = ?", (new_stock, name))
            connection.commit()
            print(f"💰 Sold {qty_bought} {name}(s). New Stock: {new_stock}")
            
    connection.close()


# --- 2. MAIN PROGRAM LOOP (The Boss) ---

print("--- 🏪 STORE MANAGEMENT SYSTEM V1.0 ---")

while True:
    print("\nMENU: [1] View Stock  [2] Add Item  [3] Buy Item  [4] Exit")
    choice = input("Enter command: ")

    if choice == '1':
        view_inventory()
    elif choice == '2':
        add_new_item()
    elif choice == '3':
        buy_item()
    elif choice == '4':
        print("Closing Store...")
        break
    else:
        print("Invalid command.")