# Task 1: Scraping & Preprocessing

This task focuses on collecting and cleaning app reviews from the Google Play Store using the `google-play-scraper` package.

---

## Objectives

- Scrape at least **400 reviews per bank** (3 banks = 1200 total)
- Normalize the review format (date, text, rating)
- Clean the dataset by removing:
  - Duplicates
  - Missing entries

---

## Key Features

- Uses `GooglePlayReviewScraper` class for modular scraping
- Saves output as `data/raw_reviews.csv`

---

## Output Columns

| Column | Description |
|--------|-------------|
| review | User review text |
| rating | 1–5 star score |
| date | Standardized `YYYY-MM-DD` |
| bank | Bank name |
| source | Fixed as "Google Play" |

---

## Usage

See: `notebooks/task-1/task_1_runner.ipynb`

