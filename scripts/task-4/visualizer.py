import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os


class ReviewVisualizer:
    def __init__(self, input_csv="../../data/sentiment_reviews.csv", output_dir="../../outputs/"):
        self.input_csv = input_csv
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.df = pd.read_csv(self.input_csv)

    def plot_sentiment_distribution(self):
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.df, x="sentiment_label", hue="bank")
        plt.title("Sentiment Distribution by Bank")
        plt.xlabel("Sentiment")
        plt.ylabel("Review Count")
        plt.legend(title="Bank")
        self._save_plot("sentiment_distribution.png")

    def plot_rating_distribution(self):
        plt.figure(figsize=(8, 5))
        sns.histplot(data=self.df, x="rating",
                     hue="bank", multiple="stack", bins=5)
        plt.title("Rating Distribution by Bank")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        self._save_plot("rating_distribution.png")

    def plot_wordcloud_per_theme(self):
        for theme in self.df["themes"].unique():
            subset = self.df[self.df["themes"] == theme]
            text = " ".join(subset["review"].astype(str))
            wc = WordCloud(background_color="white", width=800,
                           height=400).generate(text)

            plt.figure(figsize=(10, 5))
            plt.imshow(wc, interpolation="bilinear")
            plt.axis("off")
            plt.title(f"Word Cloud for Theme: {theme}")
            self._save_plot(f"wordcloud_{theme.replace(' ', '_')}.png")

    def extract_drivers_pain_points(self):
        insights = {}
        for bank in self.df["bank"].unique():
            bank_df = self.df[self.df["bank"] == bank]
            pos_keywords = self._common_keywords(
                bank_df[bank_df["sentiment_label"] == "positive"])
            neg_keywords = self._common_keywords(
                bank_df[bank_df["sentiment_label"] == "negative"])
            insights[bank] = {
                "drivers": pos_keywords[:3],
                "pain_points": neg_keywords[:3]
            }
        return insights

    def _common_keywords(self, df_subset):
        text = " ".join(df_subset["review"].astype(str).str.lower())
        words = pd.Series(text.split())
        common = words[~words.isin(
            ["the", "and", "is", "to", "it", "for", "in", "this", "that"])]
        return common.value_counts().head(10).index.tolist()

    def _save_plot(self, filename):
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath)
        plt.close()
        print(f"📊 Saved plot: {filepath}")

    def run_all(self):
        print("🚀 Task 4: Generating Visuals & Insights")
        self.plot_sentiment_distribution()
        self.plot_rating_distribution()
        self.plot_wordcloud_per_theme()
        insights = self.extract_drivers_pain_points()
        return insights
