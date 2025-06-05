import pandas as pd
from google_play_scraper import reviews_all
import os


class GooglePlayReviewScraper:
    def __init__(self, apps: dict, output_path="../../data/raw_reviews.csv", reviews_per_bank=400, scrape_limit=600):
        """
        :param apps: Dict[str, str] - Mapping of bank names to their Play Store app IDs
        :param output_path: Where to save cleaned CSV
        :param reviews_per_bank: How many CLEAN reviews to retain per bank
        :param scrape_limit: How many to scrape to compensate for cleaning losses
        """
        self.apps = apps
        self.output_path = output_path
        self.reviews_per_bank = reviews_per_bank
        self.scrape_limit = scrape_limit

    def scrape_reviews(self):
        all_cleaned = []

        for bank, app_id in self.apps.items():
            print(f"🔍 Scraping {self.scrape_limit} reviews for {bank}...")
            raw_reviews = reviews_all(app_id, lang='en', country='us')

            temp = [{
                "review": r.get("content", "").strip(),
                "rating": r.get("score", None),
                "date": r.get("at").strftime("%Y-%m-%d") if r.get("at") else None,
                "bank": bank,
                "source": "Google Play"
            } for r in raw_reviews[:self.scrape_limit]]

            df = pd.DataFrame(temp)
            df_clean = self.preprocess_reviews(df, bank)
            df_trimmed = df_clean.head(self.reviews_per_bank)
            all_cleaned.append(df_trimmed)

        return pd.concat(all_cleaned, ignore_index=True)

    def preprocess_reviews(self, df, bank):
        start = len(df)
        df.dropna(subset=["review", "rating", "date"], inplace=True)
        df.drop_duplicates(subset="review", inplace=True)
        df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
        end = len(df)
        print(f"🧹 Cleaned {start - end} rows for {bank}. Final count: {end}")
        return df

    def save_reviews(self, df):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        df.to_csv(self.output_path, index=False)
        print(f"✅ Saved {len(df)} cleaned reviews to {self.output_path}")

    def run(self):
        print("🚀 Running Task 1: Scrape + Preprocess")
        df = self.scrape_reviews()
        self.save_reviews(df)
        return df
