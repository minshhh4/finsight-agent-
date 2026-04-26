import argparse
from news_fetcher import fetch_news
from sentiment import analyze_sentiment
from signals import generate_signal
from reporter import generate_report

def run_agent(ticker: str, company: str):
    print(f"\n🤖 FinSight Agent starting analysis for {ticker}...\n")
    print("=" * 55)

    # Step 1: Fetch news
    print(f"📰 Step 1: Fetching latest news for {company}...")
    news_items = fetch_news(company)
    if not news_items:
        print("❌ No news found. Try a different company name.")
        return
    print(f"   Found {len(news_items)} articles\n")

    # Step 2: Sentiment analysis
    print("🧠 Step 2: Running NLP sentiment analysis...")
    sentiment_results = analyze_sentiment(news_items)
    avg_score = sum(r['score'] for r in sentiment_results) / len(sentiment_results)
    avg_label = "POSITIVE" if avg_score > 0 else "NEGATIVE" if avg_score < -0.1 else "NEUTRAL"
    print(f"   Avg sentiment: {avg_label} ({avg_score:.3f})\n")

    # Step 3: Generate signal
    print("📊 Step 3: Generating trading signal...")
    signal = generate_signal(avg_score, sentiment_results)
    print(f"   Signal: {signal['recommendation']} (Confidence: {signal['confidence']}%)\n")

    # Step 4: Generate report
    print("📝 Step 4: Generating analyst report...")
    report = generate_report(ticker, company, news_items, 
                           sentiment_results, signal)
    print("\n" + "=" * 55)
    print(report)
    print("=" * 55)

    # Save report
    filename = f"{ticker}_report.txt"
    with open(filename, "w") as f:
        f.write(report)
    print(f"\n✅ Report saved to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='FinSight AI Agent')
    parser.add_argument('--ticker', type=str, required=True,
                       help='Stock ticker (e.g. AAPL)')
    parser.add_argument('--company', type=str, required=True,
                       help='Company name (e.g. Apple)')
    args = parser.parse_args()
    run_agent(args.ticker.upper(), args.company)
