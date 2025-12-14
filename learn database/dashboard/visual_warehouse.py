import sqlite3
import matplotlib.pyplot as plt

print("--- 📊 GENERATING WAREHOUSE DASHBOARD ---")

# --- STEP 1: THE ROBOT FETCHES DATA ---
connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

# SQL Power Move: We multiply Price * Quantity right here in the query!
cursor.execute("SELECT name, price * quantity FROM items")
data = cursor.fetchall()

connection.close()

# --- STEP 2: ORGANIZE DATA FOR THE PAINTER ---
item_names = []
item_values = []

print("Analyzing Assets...")
for row in data:
    # row[0] is Name, row[1] is Total Value (Price * Qty)
    name = row[0]
    total_value = row[1]
    
    item_names.append(name)
    item_values.append(total_value)
    
    print(f"   Found {name}: Rp {total_value:,.0f}")

# --- STEP 3: THE PAINTER DRAWS THE PIE ---
print("Painting the chart...")

plt.figure(figsize=(8, 8)) # Make it a nice square

# The Magic Pie Command
# autopct='%1.1f%%' means "Show the percentage with 1 decimal"
plt.pie(item_values, labels=item_names, autopct='%1.1f%%', startangle=140)

plt.title("Inventory Asset Distribution (Where is the money?)")

# Save it
filename = "warehouse_assets.png"
plt.savefig(filename)

print(f"✅ DONE! Open '{filename}' to see your asset report.")