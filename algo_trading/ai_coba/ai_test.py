from textblob import TextBlob

print("--- 🧠 AI SENTIMENT TEST ---")

# 1. The Input (Human Language)
text = "I absolutely love this new phone. It is amazing!"

# 2. The Processing (AI Brain)
blob = TextBlob(text)
score = blob.sentiment.polarity

# 3. The Output (Math)
print(f"Text: '{text}'")
print(f"Sentiment Score: {score}")

# Let's try a negative one
text2 = "This service is terrible and slow."
blob2 = TextBlob(text2)
print(f"\nText: '{text2}'")
print(f"Sentiment Score: {blob2.sentiment.polarity}")