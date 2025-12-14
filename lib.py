import csv 

print("--- 🤖 AUTOMATED PROFIT PROCESSOR 🤖 ---")

# We open the file we created earlier
with open("transactions.csv", "r") as file:
    
    # 1. Create the reader
    reader = csv.DictReader(file)
    
    # 2. THE LOOP (Automatic)
    # This replaces "while True". It runs once for every row in the file.
    for row in reader:
        
        # READ the data (Don't ask the user!)
        month = row['Month']
        revenue = float(row['Revenue'])  # Python reads this from the file
        expenses = float(row['Expenses']) # Python reads this from the file
        
        # Calculate
        profit = revenue - expenses
        
        # Print Result
        print(f"Processing {month}...")
        print(f"   Revenue: ${revenue:,.2f} | Expenses: ${expenses:,.2f}")
        
        if profit > 0:
            print(f"   ✅ Profit: ${profit:,.2f}")
        else:
            print(f"   ⚠️ Loss:   ${profit:,.2f}")
        print("-" * 20)

print("Done! I processed all data in 0.01 seconds.")