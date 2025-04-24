from scrapegraphai.graphs import SmartScraperGraph

def run_openai_scraper(url: str, prompt: str, api_key: str, model: str = "gpt-3.5-turbo") -> str:
    graph_config = {
        "llm": {
            "api_key": api_key,
            "model": model,
        },
    }
    scraper = SmartScraperGraph(prompt=prompt, source=url, config=graph_config)
    return scraper.run()
