# finsight-agent-
 FinSight AI Agent

An autonomous AI agent that fetches live financial news,
analyzes sentiment using NLP, and generates analyst-style
buy/hold/sell reports — from a single command.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![NLP](https://img.shields.io/badge/NLP-VADER+TextBlob-green)
![Agent](https://img.shields.io/badge/Architecture-AI--Agent-purple)

---

 Architecture

```
User Input (ticker + company)
        ↓
[News Fetcher] → Live RSS news (no API key)
        ↓
[Sentiment Analyzer] → VADER + TextBlob + Finance keywords
        ↓
[Signal Generator] → BUY / HOLD / SELL + confidence %
        ↓
[Report Generator] → Full analyst report saved to .txt
```

 How to Run

```bash
git clone https://github.com/minshhh4/finsight-agent
cd finsight-agent
pip install -r requirements.txt
python -m textblob.download_corpora

# Analyze any stock
python agent.py --ticker AAPL --company Apple
python agent.py --ticker TSLA --company Tesla
python agent.py --ticker NVDA --company Nvidia
```

#Sample Output

```
🤖 FinSight Agent starting analysis for AAPL...
📰 Fetching latest news for Apple... Found 10 articles
🧠 Running NLP sentiment analysis... POSITIVE (0.342)
📊 Signal: 🟢 BUY (Confidence: 78.4%)
📝 Generating analyst report...
✅ Report saved to AAPL_report.txt
```

 Tech Stack

- Python 3.8+
- VADER Sentiment (financial NLP)
- TextBlob (secondary sentiment layer)
- FeedParser (live RSS news, no API key)
- Custom financial keyword boosting

 What Makes It Different

- Agentic pipeline — each module is an independent agent step
- No API keys needed — fully open source
- Custom financial sentiment boosting beyond generic NLP
- Confidence scoring based on signal consistency

 Author

**Minshu Vijay** | GSoC '24 | LeetCode Max 2000 | ICPC Algo Queen
- LinkedIn: [linkedin.com/in/minshu-vijay](https://linkedin.com/in/minshu-vijay)
- GitHub: [github.com/minshhh4](https://github.com/minshhh4)
