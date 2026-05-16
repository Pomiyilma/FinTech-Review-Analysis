import pandas as pd

df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

# Sentiment distribution by bank
summary = df.groupby(["bank", "sentiment_label"]).size()

print(summary)

# Average sentiment score by rating
rating_summary = df.groupby("rating")["sentiment_score"].mean()

print("\nAverage Sentiment Score by Rating:")
print(rating_summary)