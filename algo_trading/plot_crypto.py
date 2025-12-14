import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates # New tool for formatting dates

print("--- 📈 GENERATING CRYPTO CHART ---")

# 1. FETCH DATA
conn = sqlite3.connect("crypto_history.db")
cursor = conn.cursor()
cursor.execute("SELECT timestamp, price FROM prices")
data = cursor.fetchall()
conn.close()

if len(data) == 0:
    print("❌ No data found! Run your recorder.py first.")
    exit()

# 2. PREPARE DATA (The Conversion)
dates = []
prices = []

print(f"Processing {len(data)} data points...")

for row in data:
    # row[0] is the time string "2025-12-11 14:35:00"
    # We must convert it to a real Python Time Object
    # %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute, %S = Second
    time_obj = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
    
    dates.append(time_obj)
    prices.append(row[1])

# 3. PAINT THE CHART
plt.figure(figsize=(10, 5))

# Plot the line
plt.plot(dates, prices, marker='o', linestyle='-', color='orange', label='SUI Price')

# 4. FORMATTING THE TIME AXIS (The Tricky Part)
# This makes the dates look nice (shows Hour:Minute)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gcf().autofmt_xdate() # Slants the text so it doesn't overlap

plt.title("SUI Price Movement (Live Data)")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.legend()

# 5. SAVE
filename = "sui_chart.png"
plt.savefig(filename)
print(f"✅ Chart saved to '{filename}'")