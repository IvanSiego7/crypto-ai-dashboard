#def bisa dipakai buat pendekin if,elif,else juga

def analyze_profit(amount):
    if amount > 0:
        return "✅ Profitable"
    elif amount == 0:
        return "⚖️ Break Even"
    else:
        return "⚠️ Loss"


# --- MACHINE 1: The Cleaner ---
def clean_money(raw_data):
    cleaned_text = raw_data.replace('$', '').replace(',', '').replace('.', '')
    return float(cleaned_text)

# --- MACHINE 2: The Analyst (Your new code!) ---
def analyze_profit(amount):
    if amount > 0:
        return "✅ Profitable"
    elif amount == 0:
        return "⚖️ Break Even"
    else:
        return "⚠️ Loss"

# --- MAIN PROGRAM ---
print("--- 💰 PROFIT CALCULATOR V6.0 (Modular) 💰 ---")

while True:
    # 1. Get Input
    rev_input = input("\nEnter Revenue (or 'exit'): ")
    if rev_input.lower() == "exit": break
    revenue = clean_money(rev_input)  # <--- Using Machine 1

    exp_input = input("Enter Expenses (or 'exit'): ")
    if exp_input.lower() == "exit": break
    expenses = clean_money(exp_input) # <--- Using Machine 1

    # 2. Calculate
    profit = revenue - expenses
    
    # 3. Analyze & Print
    status = analyze_profit(profit)   # <--- Using Machine 2
    
    # Look how simple this print is now:
    print(f"Result: ${profit:,.2f} | Status: {status}")