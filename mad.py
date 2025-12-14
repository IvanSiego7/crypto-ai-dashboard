# #mad libs project
# name = input("Enter a name: ")  
# random = input('Enter a random word: ')
# print(f"{name} likes {random}")

# birth_year = input("birth year: ") 
# age = 2025 - int(birth_year)
# print(f"you're {age} years old"

revenue = float(input("Revenue: ").replace('$', '').replace(',', ''))
expenses = float(input("Expenses: ").replace('$', '').replace(',', ''))
profit = revenue - expenses
print(f"Profit: {profit}")

if profit > 0:
    print("Good job! You made profit")
elif profit == 0:  # Note: Use == to check if numbers are equal
    print("You broke even. No profit, no loss.")
else:
    print("Warning! You lost money")