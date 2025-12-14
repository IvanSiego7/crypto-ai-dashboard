import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

# --- 1. THE TOOLS (Your Toolkit) ---

def clean_hyperbole(text):
    """Fixes 'loooove' -> 'love' (Regex Surgeon)"""
    return re.sub(r'(.)\1{2,}', r'\1', text)

def fix_spelling(text):
    """Fixes 'horible' -> 'horrible' (TextBlob Spellcheck)"""
    blob = TextBlob(text)
    return str(blob.correct())

def get_smart_sentiment(text, do_autocorrect):
    # STEP A: Clean Hyperbole (We always do this, it's safe)
    # "loooove" becomes "love"
    clean_text = clean_hyperbole(text)
    
    # STEP B: Fix Spelling (CONDITIONAL)
    # We only run this if the User said "Yes"
    if do_autocorrect:
        final_text = fix_spelling(clean_text)
    else:
        final_text = clean_text
    
    # STEP C: VADER Analysis with CUSTOM RULES
    analyzer = SentimentIntensityAnalyzer()
    
    # 🧠 TEACHING VADER NEW WORDS
    new_words = {
        'garbage': -2.0,
        'trash': -2.0,
        'horrible': -3.0,
        'fire': 2.0,
        'meh': -0.5
    }
    analyzer.lexicon.update(new_words)
    
    scores = analyzer.polarity_scores(final_text)
    compound_score = scores['compound']
    
    return compound_score, final_text

# --- 2. THE UI (The Face) ---

st.title("🤖 Hybrid AI Agent (Control Panel)")
st.write("Regex + VADER + Optional Spellcheck")

# THE SWITCH 🎚️
# value=True means it is ON by default
use_spellcheck = st.checkbox("Enable Spelling Auto-Correct", value=True)

user_input = st.text_area("Customer Feedback:", height=100)

if st.button("Analyze"):
    if user_input:
        
        # Pass the checkbox value (True/False) to our logic function
        score, processed_text = get_smart_sentiment(user_input, use_spellcheck)
        
        # Show the "Processed" text so we know what the AI actually read
        if processed_text != user_input:
            st.info(f"✨ **AI Processed Input:** {processed_text}")
        else:
            st.info(f"📝 **AI Read Raw Input:** {processed_text}")
        
        # Display Results
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Score", f"{score:.2f}")
        with col2:
            if score > 0.05:
                label = "😃 Positive"
            elif score < -0.05:
                label = "😡 Negative"
            else:
                label = "😐 Neutral"
            st.metric("Verdict", label)
            
        # Alerts
        if score > 0.05:
            st.success("✅ Happy Customer!")
        elif score < -0.05:
            st.error("🚨 Angry Customer!")
        else:
            st.warning("⚠️ Neutral.")