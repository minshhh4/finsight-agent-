"""
Signal Generation Module
Converts sentiment scores into actionable trading signals.
Uses sentiment strength + consistency across articles.
"""

def generate_signal(avg_score: float, sentiment_results: list) -> dict:
    """
    Generates BUY / HOLD / SELL signal with confidence score.
    
    Logic:
    - Strong positive + consistent → BUY
    - Strong negative + consistent → SELL  
    - Mixed or weak → HOLD
    """
    total = len(sentiment_results)
    positive = sum(1 for r in sentiment_results if r['label'] == 'POSITIVE')
    negative = sum(1 for r in sentiment_results if r['label'] == 'NEGATIVE')
    neutral = sum(1 for r in sentiment_results if r['label'] == 'NEUTRAL')

    pos_ratio = positive / total
    neg_ratio = negative / total
    consistency = max(pos_ratio, neg_ratio)  # how consistent is the signal

    # Confidence based on avg score magnitude + consistency
    raw_confidence = (abs(avg_score) * 0.6 + consistency * 0.4) * 100
    confidence = round(min(raw_confidence, 95), 1)  # cap at 95%

    if avg_score > 0.15 and pos_ratio >= 0.5:
        recommendation = "🟢 BUY"
        reasoning = f"{positive}/{total} articles positive, strong upward sentiment"
    elif avg_score < -0.15 and neg_ratio >= 0.5:
        recommendation = "🔴 SELL"
        reasoning = f"{negative}/{total} articles negative, strong downward sentiment"
    else:
        recommendation = "🟡 HOLD"
        reasoning = f"Mixed signals — {positive} positive, {negative} negative, {neutral} neutral"

    return {
        'recommendation': recommendation,
        'confidence': confidence,
        'reasoning': reasoning,
        'breakdown': {
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
            'total': total
        }
    }
