from scrapegraphai.graphs import SmartScraperGraph

def run_llama_scraper(url: str, prompt: str) -> str:
    graph_config = {
        "llm": {
            "model": "ollama/llama3.2",
            "temperature": 0,
            "format": "json",
            "base_url": "http://localhost:11434",
        },
        "embeddings": {
            "model": "ollama/nomic-embed-text",
            "base_url": "http://localhost:11434",
        },
        "verbose": True,
    }
    scraper = SmartScraperGraph(prompt=prompt, source=url, config=graph_config)
    return scraper.run()
