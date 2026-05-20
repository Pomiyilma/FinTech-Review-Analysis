import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

summary = df.groupby(["bank", "sentiment_label"]).size().unstack()

summary.plot(kind="bar")

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("sentiment_distribution.png")

plt.show()