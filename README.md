# 🕵️‍♂️ AI Web Scraper Agent

> Welcome to **AI Web Scraper Agent**, a powerful and user-friendly app to scrape websites using natural language via **OpenAI** or **Llama 3.2 (Ollama)**.  
Perfect for quick data extraction, content collection, or research — just give it a prompt and a URL, and let the AI do the rest!

---

## 🌍 Use Cases

- 📰 Extract news from media sites  
- 📊 Pull data from tables or pages  
- 📦 Scrape product info from e-commerce platforms  
- 📚 Collect structured knowledge from articles or blogs

---

## 🗂️ Project Structure

```bash
AI_WebScraper/
├── agents/
│   ├── openai_scraper.py   # Scraper logic using OpenAI
│   └── llama_scraper.py    # Scraper logic using Llama 3.2
├── app/
│   ├── main_openai.py      # Streamlit app using OpenAI
│   └── main_llama.py       # Streamlit app using Llama
├── requirements.txt        # Dependencies
└── README.md
```

---

## 🛠️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/AI_WebScraper.git
cd AI_WebScraper
```
2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the App
> **▶️ OpenAI (Cloud-based)**
```bash
streamlit run app/main_openai.py
```
> **🦙 Llama 3.2 (Local Ollama)**
Make sure Ollama is installed and running locally.
```bash
streamlit run app/main_llama.py
```

---

## 🔑 API Keys Required
| Service | API Key Name     | Where to get it          |
|---------|------------------|--------------------------|
| OpenAI  | `OPENAI_API_KEY` | [openai.com](https://openai.com) |
| Ollama  | *(runs locally)* | [ollama.com](https://ollama.com) |


---

## 🧠 Powered by

- [Streamlit](https://streamlit.io/)
- [ScrapeGraphAI](https://github.com/EnricoMingo/ScrapeGraph-ai)
- [OpenAI API](https://platform.openai.com/)
- [Ollama](https://ollama.com)

---

## ✨ Contributing

🎉 **Contributions are more than welcome!**

If you find a bug 🐞, have a feature request ✨, or want to improve the code 💻:

- Open an [Issue](https://github.com/andredisa/AI_WebScraper/issues)  
- Submit a [Pull Request](https://github.com/andredisa/AI_WebScraper/pulls) 🚀  

>💬 Feel free to reach out on [GitHub](https://github.com/andredisa) or by [email](mailto:andreadisanti22@gmail.com)!

Let’s build this together!


---

## 📜 License

📄 This project is released under the **MIT License**.  
Please refer to the [LICENSE](LICENSE) file for full details.

---

### 🧑‍💻✨ Happy coding