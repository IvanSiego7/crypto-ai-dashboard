import streamlit as st
import pandas as pd
import plotly.express as px
from supabase import create_client
import feedparser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# --- 1. SETUP HALAMAN ---
st.set_page_config(page_title="Crypto Cloud Dashboard", layout="wide")
st.title("☁️ Real-Time SUI Price & Sentiment")

# --- 2. KONEKSI KE SUPABASE (AMAN UNTUK CLOUD) ---
@st.cache_resource
def init_connection():
    try:
        # Coba import dari file config.py (Untuk di Laptop)
        import config
        url = config.SUPABASE_URL
        key = config.SUPABASE_KEY
    except ImportError:
        # Jika file config tidak ada, cari di "Brankas" Streamlit Cloud
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        
    return create_client(url, key)

try:
    supabase = init_connection()
except Exception as e:
    st.error(f"Gagal koneksi database: {e}")
    st.stop()

# --- 3. FUNGSI AMBIL DATA HARGA ---
def get_data_from_cloud():
    response = supabase.table('prices').select("*").order('created_at', desc=True).limit(100).execute()
    data = response.data
    if not data:
        return pd.DataFrame()
    df = pd.DataFrame(data)
    df = df.rename(columns={'created_at': 'timestamp'})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    return df

# --- 4. FUNGSI AMBIL BERITA (VADER) ---
def get_news_sentiment():
    rss_url = "https://cointelegraph.com/rss/tag/bitcoin"
    feed = feedparser.parse(rss_url)
    analyzer = SentimentIntensityAnalyzer()
    
    news_items = []
    for entry in feed.entries[:5]:
        title = entry.title
        score = analyzer.polarity_scores(title)['compound']
        
        # Tentukan label emosi
        if score > 0.05: sentiment = "🟢 Bullish"
        elif score < -0.05: sentiment = "🔴 Bearish"
        else: sentiment = "⚪ Neutral"
            
        news_items.append({"title": title, "score": score, "sentiment": sentiment})
    
    return news_items

# --- 5. TAMPILAN DASHBOARD ---

# Kolom Kiri (Berita) dan Kanan (Grafik)
col1, col2 = st.columns([1, 2]) # Kiri kecil, Kanan besar

with col1:
    st.header("📰 Market Mood")
    news_data = get_news_sentiment()
    
    # Hitung rata-rata mood
    avg_score = sum([item['score'] for item in news_data]) / len(news_data)
    if avg_score > 0.05:
        st.success(f"Overall Mood: POSITIVE ({avg_score:.2f})")
    elif avg_score < -0.05:
        st.error(f"Overall Mood: NEGATIVE ({avg_score:.2f})")
    else:
        st.info(f"Overall Mood: NEUTRAL ({avg_score:.2f})")
        
    for item in news_data:
        st.markdown(f"**{item['sentiment']}**")
        st.caption(item['title'])
        st.divider()

with col2:
    st.header("📈 SUI Price Action")
    
    # Tombol Refresh
    if st.button('🔄 Refresh Data'):
        st.rerun()

    # Load Data Database
    df = get_data_from_cloud()

    if not df.empty:
        latest_price = df.iloc[-1]['price']
        
        # Hitung perubahan harga (biar keren)
        if len(df) > 1:
            prev_price = df.iloc[-2]['price']
            delta = latest_price - prev_price
        else:
            delta = 0
            
        st.metric(label="SUI/USDT", value=f"${latest_price}", delta=f"{delta:.4f}")
        
        fig = px.line(df, x='timestamp', y='price', title='Live Data from Supabase')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Belum ada data di database. Jalankan recorder!")