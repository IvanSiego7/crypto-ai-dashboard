import sqlite3

print("--- 📦 WAREHOUSE CLEANUP CREW ---")

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

# --- PART 1: DELETE (Fixing the Duplicate Mess) ---
print("1. Deleting ALL Gaming Mice (Cleaning duplicates)...")
# WARNING: This deletes EVERY row where the name is 'Gaming Mouse'
cursor.execute("DELETE FROM items WHERE name = 'Gaming Mouse'")


# --- PART 2: UPDATE (Changing Prices) ---
print("2. Updating Monitor Price (Inflation)...")
# We find the monitor and set its new price to 2,000,000
cursor.execute("UPDATE items SET price = 2000000 WHERE name = 'Monitor'")


# --- PART 3: RE-INSERT (Adding one clean copy) ---
print("3. Restocking one Gaming Mouse...")
cursor.execute("INSERT INTO items VALUES ('Gaming Mouse', 250000, 10)")


# --- SAVE & VERIFY ---
connection.commit() # Don't forget this!

print("\n--- FINAL INVENTORY ---")
cursor.execute("SELECT * FROM items")
for item in cursor.fetchall():
    print(f"Item: {item[0]} | Price: Rp{item[1]:,.0f} | Stock: {item[2]}")

connection.close()