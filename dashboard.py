import csv
import matplotlib.pyplot as plt

print("--- 📊 GENERATING BUSINESS DASHBOARD ---")

# Step 1: Create empty lists to hold the data
# The painter needs these to draw!
all_months = []
all_profits = []

# Step 2: The Robot reads the file
filename = "transactions.csv"
print(f"Reading data from {filename}...")

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Extract the data
        month = row['Month']
        revenue = float(row['Revenue'])
        expenses = float(row['Expenses'])
        profit = revenue - expenses
        
        # HANDOFF: Give the data to the lists
        all_months.append(month)
        all_profits.append(profit)

print(f"Found {len(all_months)} months of data.")

# Step 3: The Painter draws the chart
print("Painting the chart...")

# Make the line Green if successful, Red if bad? 
# Let's stick to Blue for now.
plt.figure(figsize=(10, 6)) # Make the image a bit bigger (10x6 inches)

plt.plot(all_months, all_profits, marker='o', color='blue', linewidth=2)

# Add a "Zero Line" so we can see when we lost money
plt.axhline(y=0, color='red', linestyle='--', alpha=0.5) 

# Labels
plt.title("Business Profit Trend (2025)", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Net Profit ($)", fontsize=12)
plt.grid(True)

# Step 4: Save the Masterpiece
output_file = "final_profit_report.png"
plt.savefig(output_file)

print(f"✅ DONE! Open '{output_file}' to see your business trend.")