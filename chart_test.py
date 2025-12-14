import matplotlib.pyplot as plt # We nickname it 'plt'

print("--- 🎨 PAINTING THE CHART... ---")

# 1. Prepare the Data (The Two Lists)
months = ["Jan", "Feb", "Mar", "Apr", "May"]
profits = [3000, 3500, -500, 6500, 5000]

# 2. Draw the Line
# plt.plot(x_axis, y_axis)
plt.plot(months, profits, marker='o', color='green', linestyle='-')

# 3. Add Labels (Make it look professional)
plt.title("Startup Profit Growth (2025)")
plt.xlabel("Month")
plt.ylabel("Profit ($)")
plt.grid(True) # Adds a grid background

# 4. SAVE the picture
filename = "my_first_chart.png"
plt.savefig(filename)

print(f"✅ Success! Open '{filename}' to see your chart.")