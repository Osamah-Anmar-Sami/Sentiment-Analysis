from transformers import pipeline
def sentiment_analysis_transformers(data):
    """
    Perform sentiment analysis on a list of Arabic text reviews using a transformer model.

    Parameters:
    data (list of str): A list of Arabic text reviews to analyze.

    Returns:
    None: This function does not return a value; it prints the sentiment analysis results for each review.
    """
    sentiment_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=0)
    for review, sentiment in zip(data, sentiment_pipeline(data, truncation=True)):
          print(f"Review: {review}\nSentiment: { sentiment.get('label').title()}\n")
