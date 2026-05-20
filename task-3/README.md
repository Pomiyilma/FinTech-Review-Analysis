# Task 3 — PostgreSQL Database Storage

## Objective
Design and implement a PostgreSQL relational database to store cleaned fintech review data and NLP analysis outputs.

## Technologies Used
- PostgreSQL
- Python
- psycopg2
- pandas

## Database Schema

### banks
- bank_id
- bank_name
- app_name

### reviews
- review_id
- bank_id
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- identified_theme
- source

## Workflow
1. Cleaned review data was merged with sentiment and thematic analysis outputs.
2. PostgreSQL tables were created using schema.sql.
3. Python insertion scripts populated the database.
4. Verification SQL queries validated data integrity.

## Verification Checks
- Review counts per bank
- Average ratings per bank
- Null value validation

## Result
The database successfully stored over 1,000 processed review records with relational integrity preserved.