import os
import requests
import urllib3
from supabase import create_client

# Matikan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("--- 🤖 GITHUB ROBOT STARTING ---")

# --- 1. SETUP KUNCI RAHASIA ---
# Robot akan mencari kunci di "Kantong" Server (Environment Variables)
# Jika tidak ada (misal di laptop), dia coba cari file config.py
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url:
    # Fallback untuk test lokal di laptop
    try:
        import config
        url = config.SUPABASE_URL
        key = config.SUPABASE_KEY
    except ImportError:
        print("❌ Error: Tidak ada URL/Key ditemukan!")
        exit()

# --- 2. KONEKSI SUPABASE ---
supabase = create_client(url, key)

# --- 3. AMBIL HARGA (CoinGecko) ---
def run_task():
    try:
        print("attempting to fetch price...")
        # URL CoinGecko
        api_url = "https://api.coingecko.com/api/v3/simple/price?ids=sui&vs_currencies=usd"
        headers = {
            "User-Agent": "Mozilla/5.0 (GitHubAction; CloudBot) AppleWebKit/537.36"
        }
        
        response = requests.get(api_url, headers=headers, verify=False, timeout=20)
        data = response.json()
        price = data['sui']['usd']
        
        print(f"💰 Price Found: ${price}")
        
        # --- 4. KIRIM KE CLOUD ---
        payload = {"price": price}
        supabase.table("prices").insert(payload).execute()
        print("✅ Success: Data saved to Supabase!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# JALANKAN TUGAS SEKALI SAJA (Tanpa Loop)
run_task()
print("--- 🤖 ROBOT FINISHED ---")