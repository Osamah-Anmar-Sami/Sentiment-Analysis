from transformers import pipeline
def sentiment_analysis_transformers(data):
    sentiment_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=0)
    for review, sentiment in zip(data, sentiment_pipeline(data, truncation=True)):
          print(f"Review: {review}\nSentiment: { sentiment.get('label').title()}\n")