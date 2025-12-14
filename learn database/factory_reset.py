import sqlite3

print("--- ☢️ FACTORY RESET INITIATED ☢️ ---")

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

# 1. DELETE EVERYTHING
# No 'WHERE' means "Target Every Row"
cursor.execute("DELETE FROM items")
print("✅ All items deleted. Warehouse is empty.")

# 2. Add Fresh Stock (One of each)
print("Restocking fresh items...")
fresh_stock = [
    ('Gaming Mouse', 250000, 10),
    ('Mechanical Keyboard', 500000, 5),
    ('HD Monitor', 2000000, 3),
    ('Mousepad', 50000, 20)
]

# Pro Tip: executemany() adds a whole list at once!
cursor.executemany("INSERT INTO items VALUES (?,?,?)", fresh_stock)

connection.commit()

print("\n--- NEW CLEAN INVENTORY ---")
cursor.execute("SELECT * FROM items")
for item in cursor.fetchall():
    print(f"Item: {item[0]} | Price: Rp{item[1]:,.0f} | Stock: {item[2]}")

connection.close()