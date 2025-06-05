import pandas as pd
from google_play_scraper import reviews_all
from datetime import datetime
import os


class GooglePlayReviewScraper:
    def __init__(self, apps, output_path="../../data/raw_reviews.csv", reviews_per_app=400):
        """
        apps: dict - {"BankName": "app.package.name"}
        output_path: str - path to save final CSV
        reviews_per_app: int - how many reviews to scrape per app
        """
        self.apps = apps
        self.output_path = output_path
        self.reviews_per_app = reviews_per_app

    def scrape_reviews(self):
        all_reviews = []
        for bank, app_id in self.apps.items():
            print(f"Scraping {bank}...")
            reviews = reviews_all(app_id, lang='en', country='us')
            for review in reviews[:self.reviews_per_app]:
                all_reviews.append({
                    "bank": bank,
                    "review": review.get('content', ''),
                    "rating": review.get('score', None),
                    "date": review.get('at').strftime('%Y-%m-%d') if review.get('at') else None,
                    "source": "Google Play"
                })
        df = pd.DataFrame(all_reviews)
        return df

    def preprocess_reviews(self, df):
        df.drop_duplicates(subset='review', inplace=True)
        df.dropna(subset=["review", "rating", "date"], inplace=True)
        df["rating"] = df["rating"].astype(int)
        return df

    def save_reviews(self, df):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        df.to_csv(self.output_path, index=False)
        print(f"Saved {len(df)} reviews to {self.output_path}")

    def run(self):
        raw_df = self.scrape_reviews()
        clean_df = self.preprocess_reviews(raw_df)
        self.save_reviews(clean_df)
        return clean_df
