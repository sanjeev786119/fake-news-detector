# news_fetcher.py

import requests

API_KEY = "4637bbc5dc4f4e0898e350ae8add916f"

def get_top_headlines(query="India", language="en", page_size=5):
    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"q={query}&language={language}&pageSize={page_size}&apiKey={API_KEY}"
    )
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Failed to fetch news. Check your API key or internet.")
        return []

    data = response.json()
    articles = data.get("articles", [])

    news_list = []
    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        content = f"{title}\n\n{description}"
        news_list.append(content)

    return news_list
