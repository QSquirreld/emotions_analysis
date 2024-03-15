import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.write("# Real Time Sentiment Analysys")
nltk.download('vader_lexicon')
user_input = st.text_input("Please Rate Out Services >>: ")
sid = SentimentIntensityAnalyzer()
# sid.lexicon
score = sid.polarity_scores(user_input)
if score == 0:
    st.write("")
elif score["neg"] != 0:
    st.write("Negative")
elif score["pos"] != 0:
    st.write("Positive")
