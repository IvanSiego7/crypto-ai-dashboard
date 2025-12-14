import sqlite3

print("--- 🏗️ BUILDING THE WAREHOUSE ---")

# 1. Connect to the database
# If 'inventory.db' doesn't exist, Python creates it automatically.
connection = sqlite3.connect("inventory.db")

# 2. Create the "Cursor" (The Worker)
# The cursor is the robot that actually goes inside and does the work.
cursor = connection.cursor()

# 3. Create the Table (The Shelves)
# SQL Command: CREATE TABLE IF NOT EXISTS
# We define 3 columns: name (Text), price (Decimal), quantity (Integer)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        name TEXT,
        price REAL,
        quantity INTEGER
    )
""")

# 4. Save Changes
connection.commit()

# 5. Close connection
connection.close()

print("✅ Success! Database 'inventory.db' created with an empty 'items' table.")