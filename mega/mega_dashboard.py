import streamlit as st
import pandas as pd
import plotly.express as px
from supabase import create_client
from google import genai  # <-- Library Baru
import time

# --- 1. SETUP HALAMAN ---
st.set_page_config(page_title="SUI AI Advisor", layout="wide")
st.title("🤖 SUI Intelligent Dashboard")

# --- 2. KONEKSI KE SUPABASE & AI ---
@st.cache_resource
def init_connections():
    try:
        # Coba load dari Laptop (config.py)
        import config
        sb_url = config.SUPABASE_URL
        sb_key = config.SUPABASE_KEY
        ai_key = config.GEMINI_KEY
    except ImportError:
        # Load dari Cloud (Secrets)
        sb_url = st.secrets["SUPABASE_URL"]
        sb_key = st.secrets["SUPABASE_KEY"]
        ai_key = st.secrets["GEMINI_KEY"]
        
    return create_client(sb_url, sb_key), ai_key

try:
    supabase, GEMINI_API_KEY = init_connections()
    # Setup Client AI Baru
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception as e:
    st.error(f"Connection Error: {e}")
    st.stop()

# --- 3. AMBIL DATA DARI SUPABASE ---
def get_market_data():
    # Ambil 20 data terakhir
    response = supabase.table('prices').select("*").order('created_at', desc=True).limit(20).execute()
    df = pd.DataFrame(response.data)
    
    if not df.empty:
        df = df.rename(columns={'created_at': 'timestamp'})
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
    return df

# --- 4. FUNGSI ANALISIS GEMINI (VERSI BARU) ---
def ask_ai_opinion(current_price, price_change):
    
    prompt = f"""
    Bertindaklah sebagai analis Crypto yang santai tapi tajam.
    Harga SUI saat ini: ${current_price}.
    Perubahan harga (Delta): ${price_change}.
    
    Berikan komentar pasar 2 kalimat saja:
    1. Analisis singkat trennya.
    2. Rekomendasi aksi (Beli/Jual/Tahan).
    """
    
    try:
        # Cara panggil terbaru (google-genai)
        response = client.models.generate_content(
            model='gemini-flash-latest', 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI sedang pusing: {e}"

# --- 5. TAMPILAN UTAMA ---
if st.button('🔄 Refresh Analysis'):
    st.rerun()

df = get_market_data()

if not df.empty:
    # Siapkan Data
    latest_price = df.iloc[-1]['price']
    prev_price = df.iloc[-2]['price'] if len(df) > 1 else latest_price
    delta = latest_price - prev_price
    
    # TAMPILAN KOLOM
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric("Live SUI Price", f"${latest_price}", f"{delta:.4f}")
        
        st.write("---")
        st.subheader("🧠 AI Opinion")
        
        with st.spinner('Asking Gemini...'):
            ai_comment = ask_ai_opinion(latest_price, delta)
            st.info(ai_comment)

    with col2:
        fig = px.line(df, x='timestamp', y='price', title='SUI Price Trend (Last 20 Points)')
        # Perbaikan Warning Streamlit (use_container_width -> width)
        st.plotly_chart(fig, width="stretch") # <-- Updated syntax

else:
    st.warning("Data kosong. Jalankan robot dulu!")
