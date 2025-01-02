from transformers import pipeline
from utils.textnormalization import Text_Normalization


text_normalization = Text_Normalization(remove_emojis = True,
                                        remove_hashtags = True,
                                        remove_url = True,
                                        remove_mention = True,
                                        remove_html_tags = True,
                                        remove_new_line_char = True,
                                        remove_english_letter = True,
                                        remove_hindi_letter = True,
                                        remove_urdu_letter = True,
                                        remove_sindhi_letter = True,
                                        remove_hebrew_letter = True,
                                        remove_latin_letter = True,
                                        remove_unwanted_char = True,
                                        remove_arabic_diacritics = True,
                                        remove_arabic_tatweel = True,
                                        convert_gaf = True,
                                        convert_pe = True,
                                        convert_che = True,
                                        convert_ve = True,
                                        convert_alef = True,
                                        convert_alef_maqsura = True,
                                        convert_teh_marbuta = True,
                                        convert_ayin = True,
                                        convert_la = True,
                                        convert_kurdish_waw = True,
                                        remove_punctuations = True,
                                        normalize_arabic_unicode = True,
                                        remove_unicode_and_special_character = True,
                                        remove_stop_words = True,
                                        remove_number = True,
                                        remove_longest_than = True,
                                        remove_duplicate_word = True,
                                        remove_single_letter = True,
                                        remove_duplicated_letter = True,
                                        remove_whitespace = True
                                        )



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

