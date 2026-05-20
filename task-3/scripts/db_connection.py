import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="bank_reviews",
        user="postgres",
        password="pompompostg05"
    )

    print("Database connected successfully!")

    conn.close()

except Exception as e:
    print("Connection failed:")
    print(e)