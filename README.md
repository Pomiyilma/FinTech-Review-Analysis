# Fintech Review Analytics

AI-powered customer experience analytics for Ethiopian fintech mobile applications.

## Objective

Analyze Google Play Store reviews from Ethiopian banking apps to identify:
- customer sentiment,
- recurring complaints,
- feature requests,
- and actionable business insights.



## Data Collection

Reviews were scraped from Google Play Store using the `google-play-scraper` Python library.

### Banks Included
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

### Data Collected
- Review text
- Rating
- Review date
- Bank name
- Review source

### Review Volume
A minimum of 400 reviews were collected per bank.


## Data Preprocessing

The preprocessing pipeline included:
- duplicate removal,
- missing value handling,
- date normalization,
- column standardization.

Final dataset columns:
- review
- rating
- date
- bank
- source

## Limitations

- Some reviews may be unavailable due to Google Play rate limits.
- Some reviews were removed during preprocessing due to missing values.

## Banks Included
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

## Tech Stack
- Python
- Pandas
- NLP
- PostgreSQL
- GitHub Actions