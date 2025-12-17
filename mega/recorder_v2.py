import time
import requests
import urllib3
from datetime import datetime
from supabase import create_client
import config

# Matikan warning SSL (agar terminal bersih)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("--- 🚀 CLOUD RECORDER (V2 - COINGECKO) STARTED ---")

# 1. Koneksi ke Supabase
try:
    supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)
    print("✅ Terhubung ke Cloud Database")
except Exception as e:
    print(f"❌ Error Connect Supabase: {e}")

def get_sui_price():
    """Mengambil harga SUI dari API CoinGecko (Lebih stabil)"""
    try:
        # Kita pakai CoinGecko karena lebih ramah aksesnya
        url = "https://api.coingecko.com/api/v3/simple/price?ids=sui&vs_currencies=usd"
        
        # Pura-pura jadi browser (User-Agent) supaya tidak ditolak
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        data = response.json()
        
        # Struktur CoinGecko beda: {'sui': {'usd': 1.55}}
        price = data['sui']['usd']
        return float(price)
        
    except Exception as e:
        print(f"⚠️ Error taking price: {e}")
        # Jika error, coba print isi response biar tau kenapa
        try:
            print(f"   Response isi: {response.text[:100]}") # Print 100 huruf pertama
        except:
            pass
        return None

def save_to_cloud(price):
    """Mengirim harga ke Supabase"""
    try:
        data = {"price": price}
        supabase.table("prices").insert(data).execute()
        print(f"☁️ Saved to Cloud: ${price}")
    except Exception as e:
        print(f"❌ Failed to save: {e}")

# --- LOOP UTAMA ---
while True:
    current_price = get_sui_price()
    
    if current_price:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Current SUI: ${current_price}")
        save_to_cloud(current_price)
    else:
        print("❌ Gagal mengambil harga, mencoba lagi nanti...")
    
    print("💤 Waiting 60 seconds...")
    time.sleep(60)