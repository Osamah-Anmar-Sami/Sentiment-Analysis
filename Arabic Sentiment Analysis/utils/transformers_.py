from transformers import pipeline

def sentiment_analysis_transformers(data):
    """
    Perform sentiment analysis on a list of Arabic text reviews using a transformer model.

    Parameters:
    data (list of str): A list of Arabic text reviews to analyze.

    Returns:
    None: This function does not return a value; it prints the sentiment analysis results for each review.
    """
    sentiment_pipeline = pipeline(task='text-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment', device=0)
    for review, sentiment in zip(data, sentiment_pipeline(data, truncation=False)):
        print(f"Review: {review}\nSentiment: {sentiment.get('label').title()}\n")
