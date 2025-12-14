import requests # The Messenger

print("--- 📡 CONTACTING COINGECKO... ---")

# 1. The Menu (URL)
# We are asking for the price of 'sui' in 'usd'
url = "https://api.coingecko.com/api/v3/simple/price?ids=sui&vs_currencies=usd"

# 2. Send the Waiter (GET Request)
response = requests.get(url)

# 3. Check the Plate (Status Code)
# 200 means "OK! Here is your food."
# 404 means "Not Found."
if response.status_code == 200:
    print("✅ Server answered!")
    
    # 4. Eat the Food (Parse JSON)
    # The server sends data in JSON format (looks like a Python Dictionary)
    data = response.json()
    
    # Let's print the raw data first to see what it looks like
    print(f"Raw Data: {data}")
    
    # 5. Extract the nugget we want
    price = data['sui']['usd']
    print(f"💰 Current Price of SUI: ${price}")
    
else:
    print(f"❌ Error: Server returned code {response.status_code}")