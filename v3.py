print("--- 💰 PROFIT CALCULATOR V3.0 💰 ---")
print("Type 'exit' to finish.\n")

history = [] 

while True:
    # --- INPUT SECTION ---
    print(f"--- Month {len(history) + 1} ---")
    
    rev_input = input("Enter Revenue: ")
    if rev_input.lower() == "exit":
        break
    # We strip symbols to keep math safe
    revenue = float(rev_input.replace('$', '').replace(',', '').replace('.', ''))

    exp_input = input("Enter Expenses: ")
    if exp_input.lower() == "exit":
        break
    expenses = float(exp_input.replace('$', '').replace(',', '').replace('.', ''))

    # --- LOGIC SECTION ---
    profit = revenue - expenses
    history.append(profit)
    
    # FORMATTING MAGIC: The :,.2f adds commas and 2 decimals
    print(f"   Month Profit: ${profit:,.2f}") 

    if profit > 0:
        print("   ✅ Profitable")
    elif profit == 0:
        print("   ⚖️ Break Even")
    else:
        print("   ⚠️ Loss")
    print("") 

# --- REPORT SECTION ---
print("\n============================")
print("📊 FINAL BUSINESS REPORT")
print("============================")

# SAFETY CHECK: Only run stats if we have data!
if len(history) > 0:
    total_profit = sum(history)
    average_profit = total_profit / len(history)
    
    # Look how clean these f-strings are now:
    print(f"Total Months:   {len(history)}")
    print(f"Total Profit:   ${total_profit:,.2f}") 
    print(f"Average Profit: ${average_profit:,.2f}")
    print(f"Best Month:     ${max(history):,.2f}")
    print(f"Worst Month:    ${min(history):,.2f}")
else:
    print("No data entered. Business didn't start yet!")