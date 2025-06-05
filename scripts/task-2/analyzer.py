import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import re

THEME_KEYWORDS = {
    "UI/UX": ["interface", "design", "layout", "navigation", "user-friendly", "screen"],
    "Login Issues": ["login", "password", "authentication", "otp", "credentials"],
    "Performance": ["crash", "slow", "freeze", "lag", "bug"],
    "Customer Support": ["support", "help", "service", "response", "complain"],
    "Feature Requests": ["add", "feature", "include", "update", "option", "setting"]
}


class ReviewAnalyzer:
    def __init__(self, input_csv="../../data/raw_reviews.csv", output_csv="../../data/sentiment_reviews.csv", top_n_keywords=10):
        self.input_csv = input_csv
        self.output_csv = output_csv
        self.top_n_keywords = top_n_keywords
        self.df = None
        self.analyzer = SentimentIntensityAnalyzer()

    def load_data(self):
        if not os.path.exists(self.input_csv):
            raise FileNotFoundError(f"❌ Input CSV not found: {self.input_csv}")
        self.df = pd.read_csv(self.input_csv)
        print(f"📥 Loaded {len(self.df)} reviews from {self.input_csv}")

    def compute_sentiment(self):
        def get_label(score):
            if score >= 0.05:
                return "positive"
            elif score <= -0.05:
                return "negative"
            else:
                return "neutral"

        self.df['sentiment_score'] = self.df['review'].apply(
            lambda x: self.analyzer.polarity_scores(str(x))['compound'])
        self.df['sentiment_label'] = self.df['sentiment_score'].apply(
            get_label)
        print("✅ Sentiment analysis complete.")

    def extract_keywords(self):
        vectorizer = TfidfVectorizer(
            stop_words='english', max_features=self.top_n_keywords)
        tfidf_matrix = vectorizer.fit_transform(self.df['review'].astype(str))
        keywords = vectorizer.get_feature_names_out()
        self.df['top_keywords'] = [", ".join(keywords)] * len(self.df)
        print(f"🗂️ Top keywords extracted: {', '.join(keywords)}")

    def assign_themes(self):
        def get_themes(text):
            text = text.lower()
            matched = []
            for theme, keywords in THEME_KEYWORDS.items():
                if any(re.search(rf"\b{kw}\b", text) for kw in keywords):
                    matched.append(theme)
            return ", ".join(matched) if matched else "Uncategorized"

        self.df["themes"] = self.df["review"].astype(str).apply(get_themes)
        print("🎯 Themes assigned to reviews.")

    def save_output(self):
        os.makedirs(os.path.dirname(self.output_csv), exist_ok=True)
        self.df.to_csv(self.output_csv, index=False)
        print(f"💾 Saved sentiment & themes to {self.output_csv}")

    def run(self):
        print("🚀 Running Task 2: Sentiment, Keywords & Themes")
        self.load_data()
        self.compute_sentiment()
        self.extract_keywords()
        self.assign_themes()
        self.save_output()
        return self.df
