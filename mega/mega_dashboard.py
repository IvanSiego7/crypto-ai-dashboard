import streamlit as st
import sqlite3
import pandas as pd # Tool for handling tables of data
import feedparser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="Ivan's Crypto Terminal", layout="wide")

# --- FUNCTION 1: GET PRICE HISTORY (From Database) ---
def get_price_history():
    # Connect to the database you built on Day 3
    conn = sqlite3.connect("crypto_history.db")
    
    # Read data directly into a "DataFrame" (A super-powered table)
    # We order by timestamp so the chart goes Left -> Right
    df = pd.read_sql_query("SELECT timestamp, price FROM prices ORDER BY timestamp", conn)
    conn.close()
    
    # Convert text time to real Time Objects for the chart
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Set the time as the "Index" (the X-axis)
    df = df.set_index('timestamp')
    return df

# --- FUNCTION 2: GET NEWS SENTIMENT (From RSS) ---
def get_news_sentiment():
    analyzer = SentimentIntensityAnalyzer()
    # Add your custom crypto dictionary here if you want
    new_words = {'bullish': 2.0, 'bearish': -2.0, 'moons': 2.0, 'rekt': -2.0}
    analyzer.lexicon.update(new_words)
    
    feed = feedparser.parse("https://cointelegraph.com/rss")
    
    articles = []
    total_score = 0
    
    # Analyze top 5 only (to keep it fast)
    for i in range(5):
        entry = feed.entries[i]
        score = analyzer.polarity_scores(entry.title)['compound']
        total_score += score
        
        icon = "⚪"
        if score > 0.05: icon = "🟢"
        elif score < -0.05: icon = "🔴"
            
        articles.append(f"{icon} **{score:.2f}**: [{entry.title}]({entry.link})")
        
    avg_score = total_score / 5
    return avg_score, articles

# --- THE LAYOUT (UI) ---
st.title("🚀 Ivan's AI Trading Terminal")

# Create two big columns
col_price, col_news = st.columns(2)

# --- LEFT COLUMN: PRICE ---
with col_price:
    st.subheader("💰 SUI Price History")
    
    try:
        # Load data from DB
        df = get_price_history()
        
        # Get the very latest price
        latest_price = df.iloc[-1]['price']
        st.metric("Current Price", f"${latest_price}")
        
        # Draw the Line Chart
        st.line_chart(df)
        
    except Exception as e:
        st.error("⚠️ Could not read database. Is recorder.py running?")
        st.write(e)

# --- RIGHT COLUMN: NEWS ---
with col_news:
    st.subheader("📰 AI Market Sentiment")
    
    if st.button("🔄 Analyze News"):
        with st.spinner("Reading Cointelegraph..."):
            score, headlines = get_news_sentiment()
        
        # Sentiment Gauge
        if score > 0.05:
            st.success(f"BULLISH (+{score:.2f})")
        elif score < -0.05:
            st.error(f"BEARISH ({score:.2f})")
        else:
            st.warning(f"NEUTRAL ({score:.2f})")
            
        # Show Headlines
        for h in headlines:
            st.markdown(h)
    else:
        st.info("Click button to scan news.")