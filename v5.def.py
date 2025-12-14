# --- 1. THE TOOLBOX (Definitions) ---
def clean_money(raw_data):
    # This is your code!
    # We strip symbols and return a clean number
    cleaned_text = raw_data.replace('$', '').replace(',', '').replace('.', '')
    return float(cleaned_text)

# --- 2. THE MAIN PROGRAM ---
print("--- 💰 PROFIT CALCULATOR V5.0 (Functions) 💰 ---")

history = []

while True:
    # REVENUE
    rev_input = input("\nEnter Revenue (or 'exit'): ")
    if rev_input.lower() == "exit":
        break
    
    # MAGIC HAPPENS HERE: We just call the function!
    revenue = clean_money(rev_input)


    # EXPENSES
    exp_input = input("Enter Expenses (or 'exit'): ")
    if exp_input.lower() == "exit":
        break
    
    # MAGIC HAPPENS HERE TOO
    expenses = clean_money(exp_input)


    # MATH
    profit = revenue - expenses
    history.append(profit)
    print(f"Profit: ${profit:,.2f}")

print("Done.")

#def bisa dipakai buat pendekin if,elif,else juga

def analyze_profit(amount):
    if amount > 0:
        return "✅ Profitable"
    elif amount == 0:
        return "⚖️ Break Even"
    else:
        return "⚠️ Loss"

