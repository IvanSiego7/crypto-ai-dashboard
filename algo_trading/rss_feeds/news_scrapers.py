import feedparser

print("--- 📡 CRYPTO NEWS FEED ---")

# 1. THE SOURCE
# This is the "Radio Station" URL for CoinTelegraph's RSS feed
rss_url = "https://cointelegraph.com/rss"

# 2. THE FETCH
# feedparser downloads the data and organizes it nicely
feed = feedparser.parse(rss_url)

print(f"✅ Connection Successful: {feed.feed.title}")
print(f"Found {len(feed.entries)} articles.\n")

# 3. THE LOOP
# Let's print the top 5 newest articles
for i in range(5):
    article = feed.entries[i]
    print(f"📰 {article.title}")
    print(f"🔗 {article.link}")
    print("---")