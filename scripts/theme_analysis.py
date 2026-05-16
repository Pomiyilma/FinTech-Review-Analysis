import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load dataset
df = pd.read_csv("data/raw/reviews_with_sentiment.csv")

# Text preprocessing function
def preprocess_text(text):
    doc = nlp(str(text).lower())

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and token.is_alpha
    ]

    return " ".join(tokens)

# Apply preprocessing
df["processed_review"] = df["review"].apply(preprocess_text)

# TF-IDF keyword extraction
vectorizer = TfidfVectorizer(
    max_features=50,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["processed_review"])

keywords = vectorizer.get_feature_names_out()

print("\nTop Keywords:")
print(keywords)



def assign_theme(text):
    text = text.lower()

    if "login" in text or "otp" in text or "password" in text:
        return "Account Access Issues"

    elif "transfer" in text or "slow" in text:
        return "Transaction Performance"

    elif "ui" in text or "design" in text or "ux" in text:
        return "UI & Design"

    elif "support" in text or "service" in text or "questions" in text:
        return "Customer Support"

    elif "fingerprint" in text or "feature" in text:
        return "Feature Requests"

    else:
        return "Other"

df["identified_theme"] = df["review"].apply(assign_theme)

final_df = df[
    [
        "review_id",
        "review",
        "sentiment_label",
        "sentiment_score",
        "identified_theme"
    ]
]

final_df.columns = [
    "review_id",
    "review_text",
    "sentiment_label",
    "sentiment_score",
    "identified_theme"
]

final_df.to_csv(
    "data/raw/final_thematic_analysis.csv",
    index=False
)

print("\nThematic analysis completed successfully.")