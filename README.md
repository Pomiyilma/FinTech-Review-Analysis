# FinTech Review Analytics

An end-to-end fintech review analytics pipeline using NLP, sentiment analysis, PostgreSQL, and data visualization to generate actionable insights from banking app reviews.

---

# Project Overview

This project was developed as part of a multi-stage data engineering and analytics challenge focused on extracting business intelligence from Google Play Store reviews of major Ethiopian banking applications. The project analyzes customer feedback from:

* Commercial Bank of Ethiopia (CBE)
* Bank of Abyssinia (BOA)
* Dashen Bank

The goal is to transform unstructured review data into actionable insights that help financial institutions improve customer satisfaction, product quality, and operational decision-making.

The pipeline includes:

* Review scraping and preprocessing
* Sentiment analysis using NLP
* Thematic analysis and keyword extraction
* PostgreSQL database integration
* Business insights and recommendation generation
* Data visualization and reporting

---

# Business Objective

Omega Consultancy aims to help Ethiopian fintech institutions better understand customer experience by leveraging large-scale review analytics. Play Store reviews contain valuable but underutilized information regarding:

* Customer satisfaction
* Feature usability
* Performance issues
* Service reliability
* Product expectations

Therefore, this project builds a complete analytics workflow that converts raw customer feedback into measurable business intelligence.

---

# Repository Structure

```bash
fintech-review-analytics/
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   ├── raw/
│   ├── bank_reviews_cleaned.csv
│   ├── reviews_with_sentiment.csv
│   └── final_thematic_analysis.csv
│
├── notebooks/
│   ├── task1_eda.ipynb
│   ├── task2_sentiment_analysis.ipynb
│   ├── task3_database.ipynb
│   └── task4_business_insights.ipynb
│
├── task-3/
│   ├── database/
│   │   ├── schema.sql
│   │   └── insert_data.py
│   │
│   ├── notebooks/
│   │   └── task3_database.ipynb
│   │
│   ├── scripts/
│   │   └── db_connection.py
│   │
│   └── README.md
│
├── scripts/
│   ├── scrape_reviews.py
│   ├── preprocess_reviews.py
│   ├── sentiment_pipeline.py
│   └── thematic_analysis.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

## Data Collection
* Python
* google-play-scraper

## Data Processing
* pandas
* numpy

## NLP & Sentiment Analysis
* HuggingFace Transformers
* distilbert-base-uncased-finetuned-sst-2-english
* TextBlob
* NLTK
* TF-IDF

## Visualization
* matplotlib
* seaborn

## Database
* PostgreSQL
* psycopg2
* SQLAlchemy

## Development Tools
* Git & GitHub
* Jupyter Notebook
* VS Code
* GitHub Actions CI/CD

---

# ON Task 1 — Data Collection & Preprocessing

## Objective
Collect and clean Google Play Store reviews from Ethiopian banking apps.

## Methodology
Reviews were scraped using the `google-play-scraper` library.

Collected fields:
* Review text
* Rating
* Review date
* Bank name
* Source

## Preprocessing Steps
* Removed duplicate reviews
* Handled missing values
* Standardized date formats
* Normalized text fields
* Saved cleaned dataset as CSV

## Output Dataset
Final cleaned dataset contains:
* 1,200+ total reviews
* Less than 5% missing data
* Standardized structure for downstream analysis

---

# ON Task 2 — Sentiment & Thematic Analysis

## Objective
Identify customer sentiment and recurring themes from bank reviews.

## Sentiment Analysis
The project used:

### Primary Model: **`distilbert-base-uncased-finetuned-sst-2-english`**
Reason for selection:
* Higher contextual understanding
* Better performance on short customer reviews
* Stronger accuracy compared to rule-based approaches

### Alternative Models Considered
* VADER
* TextBlob

## Sentiment Categories
Each review was classified as: Positive and Negative. A confidence score was also generated for every review.

## Thematic Analysis
TF-IDF and keyword extraction techniques were used to identify recurring themes such as:
* Account Access Issues
* Transaction Performance
* UI & Design
* Customer Support
* Feature Requests

## Example Findings:

### Satisfaction Drivers
* Fast navigation
* Easy transfers
* Modern UI
* Convenient banking access

### Common Pain Points
* Login failures
* OTP issues
* App crashes
* Slow transaction processing

---

# ON Task 3 — PostgreSQL Database Integration

## Objective
Store cleaned and processed review data inside a relational database.

## Database Name
```sql
bank_reviews
```

## Database Schema
### Banks Table

| Column    | Description      |
| --------- | ---------------- |
| bank_id   | Primary Key      |
| bank_name | Name of bank     |
| app_name  | Application name |

### Reviews Table

| Column           | Description        |
| ---------------- | ------------------ |
| review_id        | Primary Key        |
| bank_id          | Foreign Key        |
| review_text      | Customer review    |
| rating           | Review rating      |
| review_date      | Review date        |
| sentiment_label  | Sentiment category |
| sentiment_score  | Confidence score   |
| identified_theme | Extracted theme    |
| source           | Review source      |

## Database Features
* Foreign key relationships
* Structured relational design
* SQL verification queries
* Bulk data insertion pipeline

## Verification Queries
The project includes SQL checks for:
* Review counts per bank
* Average ratings
* Null value validation
* Referential integrity

---

# ON Task 4 — Insights & Recommendations

## Objective
Generate business-actionable recommendations using customer review analytics.

## Key Insights

### Commercial Bank of Ethiopia (CBE)

**Strengths**
* Reliable transfer functionality
* Strong accessibility

**Issues**
* Login instability
* Huawei device compatibility problems

### Bank of Abyssinia (BOA)

**Strengths**
* Positive interface feedback
* Easy account access

**Issues**
* Slow response times
* Occasional crashes

### Dashen Bank

**Strengths**
* Smooth navigation
* Good mobile experience

**Issues**
* OTP verification failures
* Transaction delays

---

# Visualizations
The project includes several publication-quality visualizations:
* Sentiment distribution by bank
* Rating distribution per bank
* Theme frequency analysis
* Keyword frequency charts
* Sentiment trends over time

---

# Setup Instructions: 

## 1. Clone Repository

```bash
git clone https://github.com/your-username/fintech-review-analytics.git
cd fintech-review-analytics
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

## Create Database

```sql
CREATE DATABASE bank_reviews;
```

## Run Schema

```bash
psql -U postgres -d bank_reviews -f schema.sql
```

## Insert Data

```bash
python insert_data.py
```

---

# CI/CD

GitHub Actions workflow automatically verifies dependency installation on push to main.
Workflow file:

```bash
.github/workflows/unittests.yml
```

---

# Key Achievements
* Scraped and processed 1,200+ banking reviews
* Built NLP sentiment analysis pipeline
* Identified major customer satisfaction drivers
* Designed relational PostgreSQL schema
* Generated business intelligence dashboards
* Produced actionable fintech recommendations

---

# Limitations

* Google Play reviews may not represent all customers
* Some reviews contain multilingual or informal text
* Sentiment analysis models may misinterpret sarcasm or mixed sentiment
* Scraping limitations may affect recency and completeness

---


# Author
Pomi Yilma

---

# License
This project was developed for educational and analytical purposes.
