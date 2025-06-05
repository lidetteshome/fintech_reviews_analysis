# 10 Academy – Week 2 Challenge: Customer Experience Analytics for Fintech Apps

This week's challenge focuses on **analyzing Google Play Store reviews** for three Ethiopian banks' mobile apps, to provide insights on **customer satisfaction**, **feature usage**, and **pain points**. The challenge mimics real-world consulting tasks at Omega Consultancy, working with mobile banking clients.

---

## Project Objective

- Scrape and clean mobile app reviews from the Google Play Store
- Analyze **sentiment** and **themes** to understand user experience
- Store structured review data in an Oracle XE database
- Visualize insights and provide **actionable recommendations** for each bank

---

## Project Structure

```
.
├── LICENSE
├── README.md
├── data
│   ├── raw_reviews.csv
│   └── sentiment_reviews.csv
├── notebooks
│   ├── task-1
│   │   └── task_1_runner.ipynb
│   ├── task-2
│   │   └── task_2_runner.ipynb
│   ├── task-3
│   │   ├── db_test.ipynb
│   │   └── task_3_runner.ipynb
│   └── task-4
│       └── task_4_runner.ipynb
├── outputs
│   ├── rating_distribution.png
│   ├── sentiment_distribution.png
│   ├── wordcloud_Customer_Support,_Feature_Requests.png
│   ├── wordcloud_Customer_Support.png
│   ├── wordcloud_Feature_Requests.png
│   ├── wordcloud_Login_Issues,_Customer_Support.png
│   ├── wordcloud_Login_Issues,_Feature_Requests.png
│   ├── wordcloud_Login_Issues,_Performance,_Feature_Requests.png
│   ├── wordcloud_Login_Issues,_Performance.png
│   ├── wordcloud_Login_Issues.png
│   ├── wordcloud_Performance,_Customer_Support.png
│   ├── wordcloud_Performance,_Feature_Requests.png
│   ├── wordcloud_Performance.png
│   ├── wordcloud_UI
│   │   ├── UX,_Feature_Requests.png
│   │   ├── UX,_Login_Issues.png
│   │   ├── UX,_Performance.png
│   │   └── UX.png
│   └── wordcloud_Uncategorized.png
├── requirements.txt
└── scripts
    ├── task-1
    │   ├── __pycache__
    │   │   └── scraper.cpython-312.pyc
    │   └── scraper.py
    ├── task-2
    │   ├── __pycache__
    │   │   └── analyzer.cpython-312.pyc
    │   └── analyzer.py
    ├── task-3
    │   ├── __pycache__
    │   │   └── db_inserter.cpython-312.pyc
    │   └── db_inserter.py
    └── task-4
        ├── __pycache__
        │   └── visualizer.cpython-312.pyc
        └── visualizer.py
```


---

## 📌 Weekly Tasks Overview

| Task | Description |
|------|-------------|
| [Task 1](./notebooks/task-1/README.md) | Scrape and preprocess reviews from Google Play Store |
| [Task 2](./notebooks/task-2/README.md) | Perform sentiment analysis and extract review themes |
| [Task 3](./notebooks/task-3/README.md) | Store the cleaned data in an Oracle XE database |
| [Task 4](./notebooks/task-4/README.md) | Visualize insights and derive business recommendations |

---

## Key Technologies Used

- Python (pandas, seaborn, wordcloud, sklearn)
- NLP: VADER for sentiment
- Oracle XE for structured storage
- Google Play Scraper
- Docker (for Oracle DB on macOS)

---

## Outcome

- 1200+ cleaned and analyzed reviews
- Stored relational data in a secure Oracle XE instance
- Visual and thematic insights across 3 banks
- Practical recommendations to improve app features and performance

---

## Contact

For questions or collaboration, please contact the contributor via email or Slack.

