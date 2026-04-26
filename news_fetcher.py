"""
News Fetcher Module
Fetches latest financial news using RSS feeds (no API key needed)
"""

import feedparser
import urllib.parse
from datetime import datetime

def fetch_news(company: str, max_articles: int = 10) -> list:
    """
    Fetches latest news for a company using Google News RSS.
    No API key required.
    """
    query = urllib.parse.quote(f"{company} stock")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    
    feed = feedparser.parse(url)
    articles = []
    
    for entry in feed.entries[:max_articles]:
        articles.append({
            'title': entry.get('title', ''),
            'summary': entry.get('summary', entry.get('title', '')),
            'published': entry.get('published', str(datetime.now())),
            'source': entry.get('source', {}).get('title', 'Unknown')
        })
    
    return articles
