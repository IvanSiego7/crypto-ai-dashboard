import csv
import os

print("--- 🛠️ STEP 1: GENERATING DATA... ---")

# 1. Let's FORCE create the file with data right now
# This guarantees the file is NOT empty
data = [
    ["Month", "Revenue", "Expenses"], # The Headers
    ["January", "5000", "2000"],
    ["February", "6000", "2500"],
    ["March", "4000", "4500"],
    ["April", "7500", "1000"],
    ["May", "8000", "3000"]
]

filename = "transactions.csv"

# Write the data to the hard drive
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"✅ Success! '{filename}' has been created with 5 rows of data.\n")


print("--- 🤖 STEP 2: THE ROBOT READS THE DATA ---")

# 2. Now we read the file we just made
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    
    row_count = 0
    
    for row in reader:
        row_count += 1
        
        # Read
        month = row['Month']
        revenue = float(row['Revenue'])
        expenses = float(row['Expenses'])
        
        # Calculate
        profit = revenue - expenses
        
        # Print
        print(f"Processing {month}...")
        print(f"   Revenue: ${revenue:,.2f} | Expenses: ${expenses:,.2f}")
        
        if profit > 0:
            print(f"   ✅ Profit: ${profit:,.2f}")
        else:
            print(f"   ⚠️ Loss:   ${profit:,.2f}")
        print("-" * 20)

    if row_count == 0:
        print("❌ ERROR: The file was empty!")
    else:
        print(f"🎉 SUCCESS: Processed {row_count} months.")