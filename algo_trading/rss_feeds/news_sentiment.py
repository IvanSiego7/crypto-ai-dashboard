import feedparser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

print("--- 📰 AI MARKET ANALYST INITIALIZED ---")

# 1. SETUP
analyzer = SentimentIntensityAnalyzer()
rss_url = "https://cointelegraph.com/rss"

# 🧠 Teach VADER some crypto slang
new_words = {
    'crushes': 2.0,
    'moons': 2.0,
    'buying': 1.0,
    'bullish': 2.0,
    'bearish': -2.0,
    'fades': -1.5,
    'slams': -2.0,
    'struggles': -2.0,
    'hack': -3.0
}
analyzer.lexicon.update(new_words)

# 2. FETCH NEWS
print("Fetching latest headlines...")
feed = feedparser.parse(rss_url)

total_score = 0
count = 0

print(f"\nAnalyzing Top 10 Stories:\n{'-'*30}")

# 3. ANALYZE LOOP (Only check top 10 to keep it fast)
for i in range(10):
    article = feed.entries[i]
    title = article.title
    
    # Get Sentiment
    vs = analyzer.polarity_scores(title)
    score = vs['compound']
    
    # Add to total so we can calculate average later
    total_score += score
    count += 1
    
    # Print individual result
    # We use an arrow to show direction: 🟢 Up, 🔴 Down, ⚪ Flat
    icon = "⚪"
    if score > 0.05: icon = "🟢"
    elif score < -0.05: icon = "🔴"
        
    print(f"{icon} [{score:.2f}] {title}")

# 4. THE FINAL VERDICT
average_score = total_score / count

print(f"\n{'-'*30}")
print(f"📊 MARKET SENTIMENT REPORT")
print(f"Average Score: {average_score:.3f}")

if average_score > 0.05:
    print("🚀 VERDICT: BULLISH (Good time to buy?)")
elif average_score < -0.05:
    print("🐻 VERDICT: BEARISH (Market is fearful)")
else:
    print("⚖️ VERDICT: NEUTRAL (Market is uncertain)")