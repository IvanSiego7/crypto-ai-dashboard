from textblob import TextBlob
import time

print("--- 🤖 AUTOMATED SUPPORT AGENT V2 (Smart Fix) ---")

while True:
    user_input = input("\nCustomer: ")
    
    if user_input.lower() == 'exit':
        break

    # 1. CREATE BLOB
    raw_blob = TextBlob(user_input)
    
    # 2. THE SPELL CHECKER (The Magic Step)
    # We ask the AI: "What did they probably mean?"
    corrected_blob = raw_blob.correct()
    
    # Let's print what the bot "heard" so you can see the fix
    if raw_blob != corrected_blob:
        print(f"   (Typo detected! Auto-corrected to: '{corrected_blob}')")
    
    # 3. ANALYZE THE CORRECTED TEXT
    score = corrected_blob.sentiment.polarity
    print(f"   [Score: {score:.2f}]")
    
    time.sleep(1)

    # 4. DECISION LOGIC
    if score < -0.1: # Even slightly negative
        print("🤖 Bot: We are sorry! A Manager has been alerted. 🚨")
    elif score > 0.1:
        print("🤖 Bot: Thank you for the love! 🌟")
    else:
        print("🤖 Bot: Understood. Let us know if we can help. 😐")

    #this code can handle typo already