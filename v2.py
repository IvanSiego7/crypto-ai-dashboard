print("--- 💰 PROFIT CALCULATOR V2.0 💰 ---")
print("Type 'exit' to finish and see your summary.\n")

# [MEMORY START] Create the empty list before the loop starts
history = [] 

while True:
    print(f"--- Month {len(history) + 1} ---") # Pro tip: Shows which month you are on!

    # 1. REVENUE
    rev_input = input("Enter Revenue: ")
    if rev_input.lower() == "exit":
        break
    revenue = float(rev_input.replace('$', '').replace(',', '').replace('.', ''))

    # 2. EXPENSES
    exp_input = input("Enter Expenses: ")
    if exp_input.lower() == "exit":
        break
    expenses = float(exp_input.replace('$', '').replace(',', '').replace('.', ''))

    # 3. CALCULATE
    profit = revenue - expenses
    
    # [MEMORY ADD] Save the result to our list!
    history.append(profit)
    
    print(f"   Month Profit: ${profit}")

    if profit > 0:
        print("   ✅ Profitable")
    elif profit == 0:
        print("   ⚖️ Break Even")
    else:
        print("   ⚠️ Loss")
    
    print("") # Just adds an empty line for neatness

# --- END OF LOOP ---

# [MEMORY RESULTS] This runs only after you break the loop
print("\n============================")
print("📊 FINAL BUSINESS REPORT")
print("============================")

print(f"Total Months: {len(history)}")

if len(history) > 0:
    print(f"Total Profit: ${sum(history)}")
    print(f"Best Month: ${max(history)}")
    print(f"Worst Month: ${min(history)}")
    print(f"Average Profit: ${sum(history)/len(history)}")
else:
    print("No data entered.")

# Entrepreneur Challenge: Can you guess how to calculate the Average?
# Hint: Average = Total / Number of items