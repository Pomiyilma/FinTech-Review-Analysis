import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="pompompostg05"
)

cur = conn.cursor()

# Load final dataset
df = pd.read_csv('data/final_database_dataset.csv')

# Insert unique banks
unique_banks = df['bank'].unique()

for bank in unique_banks:
    cur.execute("""
        INSERT INTO banks (bank_name, app_name)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING
    """, (bank, f"{bank} Mobile Banking"))

conn.commit()

print("Banks inserted successfully!")

# Fetch bank IDs
cur.execute("SELECT bank_id, bank_name FROM banks")
bank_mapping = {name: bank_id for bank_id, name in cur.fetchall()}

# Insert reviews
for _, row in df.iterrows():

    bank_id = bank_mapping[row['bank']]

    cur.execute("""
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            identified_theme,
            source
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        bank_id,
        row['review'],
        int(row['rating']),
        row['date'],
        row['sentiment_label'],
        float(row['sentiment_score']),
        row['identified_theme'],
        row['source']
    ))

conn.commit()

print("Reviews inserted successfully!")

cur.close()
conn.close()