import requests
import sqlite3
import time
from datetime import datetime # Tool to get the current time

print("--- 💽 SUI DATA RECORDER STARTED ---")

# 1. SETUP: Create the database/table if it doesn't exist
conn = sqlite3.connect("crypto_history.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS prices (timestamp TEXT, price REAL)")
conn.commit()
conn.close()

while True:
    try:
        # 2. FETCH: Get price from Internet
        url = "https://api.coingecko.com/api/v3/simple/price?ids=sui&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data['sui']['usd']
        
        # 3. TIME: Get exact time right now
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 4. STORE: Save to Database
        conn = sqlite3.connect("crypto_history.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO prices VALUES (?, ?)", (now, price))
        conn.commit()
        conn.close()
        
        print(f"[{now}] 💾 Saved SUI Price: ${price}")
        
    except Exception as e:
        print(f"⚠️ Error: {e}")

    # 5. WAIT: Sleep for 60 seconds
    time.sleep(60)