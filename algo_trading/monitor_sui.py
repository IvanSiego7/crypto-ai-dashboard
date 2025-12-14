import requests
import time # New tool: Allows us to pause the script

print("--- 🦅 SUI SNIPER BOT ACTIVATED ---")
print("Press 'Ctrl + C' to stop the bot.\n")

target_price = 1.5 # The price we are waiting for

while True:
    # 1. Ask for the price
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=sui&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        current_price = data['sui']['usd']
        
        # 2. Print the status
        print(f"Checking... SUI is ${current_price}")
        
        # 3. The "Sniper" Logic
        if current_price < target_price:
            print("🚨 ALERT: PRICE IS CHEAP! BUY NOW! 🚨")
            print("🚨 ALERT: PRICE IS CHEAP! BUY NOW! 🚨")
        elif current_price > target_price:
            print("   (Too expensive, waiting...)")
            
    except Exception as e:
        print(f"⚠️ Error connection: {e}")

    # 4. Wait for 10 seconds before checking again
    # If we don't wait, CoinGecko will ban us for spamming!
    time.sleep(10)