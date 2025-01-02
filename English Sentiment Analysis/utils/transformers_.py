from transformers import pipeline
from utils.textnormalization import Text_Normalization


text_normalization = Text_Normalization(string_lower = True,
                                        remove_emojis = True,
                                        remove_hashtags = True,
                                        remove_emails = True,
                                        remove_url = True,   
                                        remove_mention = True,
                                        remove_html_tags = True,
                                        remove_new_line_char = True,
                                        expand_contractions = True, 
                                        remove_stop_words = True,
                                        remove_duplicate_word = True,
                                        remove_single_letter = True,
                                        remove_duplicated_letter = True,
                                        remove_unicode_and_special_character = True,
                                        remove_punctuations = True,
                                        remove_number = True,
                                        remove_non_english = True,
                                        remove_longest_than = True,
                                        remove_extra_whitespace = True)

def sentiment_analysis_transformers(data):
    """
    Perform sentiment analysis on a list of text data using a pre-trained transformer model.

    Args:
        data (list of str): A list of text reviews to analyze.

    Returns:
        None: This function prints the sentiment analysis results for each review.e
    """
    data_ = list(map(text_normalization.text_normalization, data))
    sentiment_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=0)
    for review, sentiment in zip(data, sentiment_pipeline(data_, truncation=True)):
          print(f"Review: {review}\nSentiment: { sentiment.get('label').title()}\n")
