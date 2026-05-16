import pandas as pd
from transformers import pipeline

# Load cleaned dataset
df = pd.read_csv("data/raw/bank_reviews_cleaned.csv")

# Load sentiment analysis model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Function to classify sentiment
def analyze_sentiment(text):
    try:
        result = sentiment_pipeline(str(text))[0]

        label = result["label"]
        score = result["score"]

        # Convert LABEL_0 / LABEL_1 if needed
        if label == "POSITIVE":
            sentiment = "positive"
        elif label == "NEGATIVE":
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return pd.Series([sentiment, score])

    except Exception:
        return pd.Series(["neutral", 0.0])

# Apply sentiment analysis
df[["sentiment_label", "sentiment_score"]] = df["review"].apply(analyze_sentiment)

# Create review_id
df["review_id"] = range(1, len(df) + 1)

# Save partial results
df.to_csv("data/raw/reviews_with_sentiment.csv", index=False)

print(df.head())

print("\nSentiment analysis completed successfully.")