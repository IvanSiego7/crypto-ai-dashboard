import sqlite3

print("--- 📦 WAREHOUSE MANAGER V1 ---")

# 1. Connect
connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

# --- PART A: INSERT (Adding Stock) ---
print("Adding new items...")

# We use execute() to run the SQL command
# Note: Text must be in quotes 'Apple', numbers are just numbers.
cursor.execute("INSERT INTO items VALUES ('Gaming Mouse', 250000, 10)")
cursor.execute("INSERT INTO items VALUES ('Keyboard', 500000, 5)")
cursor.execute("INSERT INTO items VALUES ('Monitor', 1500000, 3)")

# CRITICAL STEP: Save the changes!
# If you forget commit(), the data disappears when the script ends.
connection.commit() 
print("✅ Items added to database.")


# --- PART B: SELECT (Viewing Stock) ---
print("\n--- CURRENT INVENTORY ---")

# 1. Run the "Get Everything" command
cursor.execute("SELECT * FROM items")

# 2. Fetch the results from the cursor
# The cursor holds the data in its hand; we need to take it.
all_items = cursor.fetchall()

# 3. Loop through the list (It looks like a list of tuples!)
for item in all_items:
    # item[0] is Name, item[1] is Price, item[2] is Quantity
    print(f"Item: {item[0]} | Price: Rp{item[1]:,.0f} | Stock: {item[2]}")

# 4. Close the door
connection.close()