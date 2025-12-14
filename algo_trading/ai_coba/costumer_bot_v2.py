from textblob import TextBlob
import time
import re # 1. Import the Regex Surgeon

def clean_text(text):
    """
    Reduces 3+ repeated characters to just 1.
    Example: "loooove" -> "love", "horribleeee" -> "horrible"
    """
    # The Regex Pattern: (char)\1{2,} matches any character that repeats 3+ times
    # We replace it with just the character itself (r'\1')
    cleaned_text = re.sub(r'(.)\1{2,}', r'\1', text)
    return cleaned_text

print("--- 🤖 AUTOMATED SUPPORT AGENT V3 (Hyperbole Fix) ---")

while True:
    user_input = input("\nCustomer: ")
    
    if user_input.lower() == 'exit':
        break

    # 1. CLEAN THE HYPERBOLE
    # "horribleeeeee" becomes "horrible"
    cleaned_input = clean_text(user_input)
    
    if cleaned_input != user_input:
        print(f"   (Hyperbole detected! Cleaning to: '{cleaned_input}')")

    # 2. CREATE BLOB
    raw_blob = TextBlob(cleaned_input)
    
    # 3. SPELL CHECK (Optional, but good for "horible")
    corrected_blob = raw_blob.correct()
    
    # 4. ANALYZE
    score = corrected_blob.sentiment.polarity
    print(f"   [Score: {score:.2f}]")
    
    time.sleep(1)

    # 5. DECISION LOGIC
    if score < -0.1:
        print("🤖 Bot: We are sorry! A Manager has been alerted. 🚨")
    elif score > 0.1:
        print("🤖 Bot: Thank you for the love! 🌟")
    else:
        print("🤖 Bot: Understood. Let us know if we can help. 😐")