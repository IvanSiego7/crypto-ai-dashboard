print("--- 💰 PROFIT CALCULATOR V4.0 (With Auto-Save) 💰 ---")
print("Type 'exit' to finish.\n")

history = [] 

while True:
    print(f"--- Month {len(history + 1 )} ---")
    
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
    history.append(profit)
    
    # --- [FILE SAVE START] --- 
    # We prepare a nice string to save. 
    # \n at the end means "hit enter" so the next line is below it.
    log_entry = f"Revenue: ${revenue:,.2f} | Expenses: ${expenses:,.2f} | Profit: ${profit:,.2f}\n"
    
    # Open the file, write the line, and close it automatically
    with open("my_business_ledger.txt", "a") as file:
        file.write(log_entry)
        
    print(f"   💾 Saved to ledger!")
    # --- [FILE SAVE END] ---

    print(f"   Month Profit: ${profit:,.2f}") 

    if profit > 0:
        print("   ✅ Profitable")
    elif profit == 0:
        print("   ⚖️ Break Even")
    else:
        print("   ⚠️ Loss")
    print("") 

# --- END OF LOOP ---

print("\n============================")
print("📊 FINAL BUSINESS REPORT")
print("============================")

if len(history) > 0:
    print(f"Total Months:   {len(history)}")
    print(f"Total Profit:   ${sum(history):,.2f}") 
    print(f"Best Month:     ${max(history):,.2f}")
    print("Check 'my_business_ledger.txt' to see your full history!")
else:
    print("No data entered.")


