"""
Sentiment Analysis Module
Uses VADER (rule-based) + TextBlob for financial sentiment scoring.
No GPU or API key needed — runs fully offline.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Financial words that VADER underweights — we boost these
FINANCE_BOOSTS = {
    'surge': 0.3, 'soar': 0.3, 'rally': 0.25, 'beat': 0.2,
    'record': 0.2, 'growth': 0.15, 'profit': 0.15, 'gain': 0.15,
    'crash': -0.4, 'plunge': -0.4, 'slump': -0.3, 'miss': -0.25,
    'loss': -0.2, 'layoff': -0.25, 'debt': -0.15, 'sue': -0.2,
    'fraud': -0.4, 'bankrupt': -0.5, 'recall': -0.2, 'fine': -0.15
}

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(news_items: list) -> list:
    """
    Analyzes sentiment of each news item.
    Combines VADER + TextBlob + financial keyword boosting.
    Returns list of dicts with score and label per article.
    """
    results = []

    for item in news_items:
        text = item['title'] + " " + item['summary']
        
        # VADER score
        vader_scores = analyzer.polarity_scores(text)
        vader_compound = vader_scores['compound']
        
        # TextBlob score
        blob_score = TextBlob(text).sentiment.polarity
        
        # Financial keyword boost
        text_lower = text.lower()
        boost = sum(
            score for word, score in FINANCE_BOOSTS.items()
            if word in text_lower
        )
        
        # Weighted final score
        final_score = (vader_compound * 0.5) + (blob_score * 0.3) + (boost * 0.2)
        final_score = max(-1.0, min(1.0, final_score))  # clamp to [-1, 1]
        
        label = (
            "POSITIVE" if final_score > 0.1
            else "NEGATIVE" if final_score < -0.1
            else "NEUTRAL"
        )

        results.append({
            'title': item['title'],
            'source': item['source'],
            'score': final_score,
            'label': label,
            'vader': vader_compound,
            'textblob': blob_score
        })

    return results
