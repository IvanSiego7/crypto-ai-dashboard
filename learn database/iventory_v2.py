import sqlite3

# --- HELPER: The Cleaner ---
def clean_number(raw_text):
    """Removes 'Rp', '$', commas, and dots to return a clean number."""
    clean_text = raw_text.replace('Rp', '').replace('$', '').replace(',', '').replace('.', '')
    # If empty (user just hit enter), return 0
    if clean_text == "":
        return 0
    return float(clean_text)

# --- DATABASE FUNCTIONS ---

def view_inventory():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    
    print("\n--- 📦 CURRENT STOCK ---")
    if len(items) == 0:
        print("(Warehouse is empty)")
    else:
        for item in items:
            print(f"🔹 {item[0]} | Rp{item[1]:,.0f} | Stock: {item[2]}")
            
    connection.close()

def add_new_item():
    """Now supports inputs like '10,000' or 'Rp 50000'"""
    name = input("Item Name: ")
    
    # FIX 1: Use the cleaner function here!
    price_input = input("Price: ")
    price = clean_number(price_input)
    
    qty = int(input("Quantity: "))
    
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items VALUES (?, ?, ?)", (name, price, qty))
    connection.commit()
    connection.close()
    print(f"✅ Added {name} (Rp{price:,.0f}) to warehouse.")

def buy_item():
    """Now finds items even if you use lowercase!"""
    user_input_name = input("Which item are you buying? ")
    qty_bought = int(input("How many? "))
    
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    
    # FIX 2: Case-Insensitive Search
    # We ask SQL: "Find the row where the lowercase version of the name matches my input"
    # We also select the 'name' column so we get the REAL name (e.g., 'Gaming Mouse')
    cursor.execute("SELECT quantity, name FROM items WHERE LOWER(name) = LOWER(?)", (user_input_name,))
    result = cursor.fetchone()
    
    if result is None:
        print("❌ Error: Item not found!")
    else:
        current_stock = result[0]
        real_name = result[1] # This captures the correct capitalization (e.g. "Gaming Mouse")
        
        if current_stock < qty_bought:
            print(f"⚠️ Not enough stock! We only have {current_stock}.")
        else:
            new_stock = current_stock - qty_bought
            
            # Update using the REAL name we found
            cursor.execute("UPDATE items SET quantity = ? WHERE name = ?", (new_stock, real_name))
            connection.commit()
            print(f"💰 Sold {qty_bought} {real_name}(s). New Stock: {new_stock}")
            
    connection.close()

# --- MAIN LOOP ---
print("--- 🏪 STORE MANAGEMENT SYSTEM V2.0 (Polished) ---")

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