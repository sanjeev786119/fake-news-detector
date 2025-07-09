# app.py

import streamlit as st
from detector import predict_news

st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detector")
st.subheader("Paste or write any news article to check its authenticity")

# Input box
news_input = st.text_area("Enter News Content Here", height=300)

if st.button("Check"):
    if news_input.strip() == "":
        st.warning("Please paste some news to check.")
    else:
        result = predict_news(news_input)
        if result.lower() == "fake":
            st.error("🚨 This news is FAKE!")
        else:
            st.success("✅ This news is REAL.")
