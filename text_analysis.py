import json
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import yake

nltk.download("punkt")

# ---------------- LOAD TEXT ----------------
with open("transcript.json", "r", encoding="utf-8") as f:
    data = json.load(f)

text = data["full_text"]

# ---------------- SENTIMENT ----------------
analyzer = SentimentIntensityAnalyzer()
sentiment_scores = analyzer.polarity_scores(text)

compound = sentiment_scores["compound"]

if compound >= 0.05:
    sentiment = "Positive"
elif compound <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# ---------------- KEY TOPICS ----------------
kw_extractor = yake.KeywordExtractor(
    lan="en",
    n=2,
    top=5
)

keywords = [kw for kw, score in kw_extractor.extract_keywords(text)]

# ---------------- SUMMARY ----------------
sentences = nltk.sent_tokenize(text)
summary = " ".join(sentences[:2])

# ---------------- OUTPUT ----------------
analysis = {
    "sentiment": sentiment,
    "sentiment_score": compound,
    "key_topics": keywords,
    "call_summary": summary
}

with open("analysis.json", "w", encoding="utf-8") as f:
    json.dump(analysis, f, indent=4)

print(" Analysis done and saved to analysis.json")
