import os
from supabase import create_client, Client

print("--- ☁️ SUPABASE CONNECTION TEST ---")

# 1. KONFIGURASI (GANTI DENGAN PUNYAMU!)
url = "https://ykdbbcshvikbzpnnzjkz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlrZGJiY3NodmlrYnpwbm56amt6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjU5NTEwMzQsImV4cCI6MjA4MTUyNzAzNH0.1gHfksN8XBFNfh6iteKFhlCgBuStb2-fC-6zBHxqBR0"

# 2. BUKA KONEKSI
# Kita membuat 'client' (mirip dengan 'cursor' di SQLite)
supabase: Client = create_client(url, key)

# 3. TEST INSERT (Kirim Data)
print("Sending data to Cloud...")
# Perintahnya mirip bahasa Inggris: Table 'prices' -> Insert data -> Execute
# Kita tidak perlu kirim 'created_at', Supabase mengisinya otomatis!
data_to_send = {"price": 1.55}
response = supabase.table("prices").insert(data_to_send).execute()

print(f"✅ Data Sent! Response: {response}")

# 4. TEST SELECT (Baca Data)
print("\nReading data from Cloud...")
# Select "*" means all columns
response_read = supabase.table("prices").select("*").execute()

# Data ada di dalam response_read.data
items = response_read.data

for item in items:
    print(f"🆔 ID: {item['id']} | ⏰ Time: {item['created_at']} | 💰 Price: ${item['price']}")