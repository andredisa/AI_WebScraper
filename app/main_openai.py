import streamlit as st
from agents.openai_scraper import run_openai_scraper

st.title("Web Scraping AI Agent 🕵️‍♂️")
st.caption("Scrape any website using OpenAI's GPT")

api_key = st.text_input("🔑 OpenAI API Key", type="password")
if api_key:
    model = st.radio("Select the model", ["gpt-3.5-turbo", "gpt-4"], index=0)
    url = st.text_input("🌐 Website URL")
    prompt = st.text_input("🧠 What should the AI extract from this site?")
    
    if st.button("🚀 Scrape"):
        result = run_openai_scraper(url, prompt, api_key, model)
        st.write(result)
