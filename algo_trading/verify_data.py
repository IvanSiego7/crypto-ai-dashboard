import sqlite3

print("--- 🕵️‍♂️ INSPECTING DATABASE ---")

# 1. Connect to the file
connection = sqlite3.connect("crypto_history.db")
cursor = connection.cursor()

# 2. check if the table exists first (to avoid crashes if file is empty)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='prices'")
if cursor.fetchone() is None:
    print("❌ Error: The table 'prices' does not exist yet.")
    print("   (Did you run the recorder script long enough?)")
else:
    # 3. Read the data
    cursor.execute("SELECT * FROM prices")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("⚠️ The database is empty! (Recorder didn't save anything yet)")
    else:
        print(f"✅ Found {len(rows)} recorded prices:\n")
        for row in rows:
            # row[0] is the Time, row[1] is the Price
            print(f"   📅 Time: {row[0]}  |  💰 Price: ${row[1]}")

connection.close()