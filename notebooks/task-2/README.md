# Task 2: Sentiment & Thematic Analysis

This task focuses on **understanding user emotion** and **common review topics** using Natural Language Processing.

---

## Objectives

- Assign sentiment scores (positive/neutral/negative) to each review
- Extract high-frequency keywords
- Cluster review content into themes such as:
  - UI/UX
  - Login Issues
  - Performance
  - Feature Requests
  - Support

---

## NLP Tools Used

- **VADER** for sentiment scoring
- **TF-IDF** for keyword extraction
- **Rule-based theme mapping** with keyword dictionaries

---

## Output Columns (appended to `sentiment_reviews.csv`)

| Column | Description |
|--------|-------------|
| sentiment_score | Float value from VADER |
| sentiment_label | `positive` / `neutral` / `negative` |
| top_keywords | Top TF-IDF keywords |
| themes | Inferred review category |

---

## Usage

See: `notebooks/task-2/task_2_runner.ipynb`
