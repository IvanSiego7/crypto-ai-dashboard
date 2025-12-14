import streamlit as st
import feedparser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd # Optional, but makes tables look nice

# --- 1. THE BRAIN (Logic) ---
def get_crypto_news():
    # Setup VADER
    analyzer = SentimentIntensityAnalyzer()
    new_words = {
        'crushes': 2.0, 'moons': 2.0, 'buying': 1.0, 'bullish': 2.0,
        'bearish': -2.0, 'fades': -1.5, 'slams': -2.0, 'struggles': -2.0,
        'hack': -3.0, 'bid': 1.0, 'benefits': 1.5
    }
    analyzer.lexicon.update(new_words)
    
    # Fetch RSS
    rss_url = "https://cointelegraph.com/rss"
    feed = feedparser.parse(rss_url)
    
    news_data = []
    total_score = 0
    
    # Analyze Top 10
    for i in range(10):
        article = feed.entries[i]
        title = article.title
        link = article.link
        
        # Sentiment
        vs = analyzer.polarity_scores(title)
        score = vs['compound']
        total_score += score
        
        # Icon
        if score > 0.05: icon = "🟢"
        elif score < -0.05: icon = "🔴"
        else: icon = "⚪"
            
        news_data.append({
            "Sentiment": icon,
            "Score": score,
            "Headline": title,
            "Link": link
        })
        
    avg_score = total_score / 10
    return avg_score, news_data

# --- 2. THE FACE (UI) ---
st.set_page_config(page_title="Crypto AI Trader", layout="wide")

st.title("📡 AI Crypto Market Sentiment")
st.markdown("Real-time analysis of CoinTelegraph headlines.")

# The "Refresh" Button
if st.button("🔄 Scan Market Now"):
    with st.spinner('Reading the news...'):
        avg_score, news_list = get_crypto_news()
    
    # 3. THE SCOREBOARD
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Market Sentiment Score", value=f"{avg_score:.3f}")
    
    with col2:
        if avg_score > 0.05:
            st.success("🚀 VERDICT: BULLISH")
        elif avg_score < -0.05:
            st.error("🐻 VERDICT: BEARISH")
        else:
            st.warning("⚖️ VERDICT: NEUTRAL")
            
    with col3:
        st.info("Scanning Top 10 Headlines")

    st.divider()

    # 4. THE NEWS FEED
    st.subheader("📰 Latest Headlines Analyzed")
    
    # Display as a clean list
    for item in news_list:
        # Create a clickable link
        st.markdown(f"**{item['Sentiment']} [{item['Score']:.2f}]** [{item['Headline']}]({item['Link']})")

else:
    st.write("Click the button above to start the AI analysis.")