import streamlit as st
from agents.llama_scraper import run_llama_scraper

st.title("Web Scraping AI Agent 🦙")
st.caption("Scrape any website locally using Llama 3.2 via Ollama")

url = st.text_input("🌐 Website URL")
prompt = st.text_input("🧠 What should the AI extract from this site?")


if st.button("🚀 Scrape"):
    result = run_llama_scraper(url, prompt)
    st.write(result)
