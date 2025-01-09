import tensorflow as tf
import numpy as np
from utils.text_preprocessing import text_to_sequence, sequences_padding
from utils.textnormalization import Text_Normalization


text_normalization = Text_Normalization(remove_emojis = True,
                                        remove_hashtags = True,
                                        remove_url = True,
                                        remove_mention = True,
                                        remove_html_tags = True,
                                        remove_new_line_char = True,
                                        remove_english_letter = True,
                                        remove_stop_words = True,
                                        remove_al = True,
                                        remove_arabic_diacritics = True,
                                        remove_arabic_tatweel = True,
                                        convert_gaf = True,
                                        convert_pe = True,
                                        convert_che = True,
                                        convert_ve = True,
                                        convert_alef = True,
                                        convert_alef_maqsura = True,
                                        convert_teh_marbuta = True,
                                        convert_kurdish_rah = True,
                                        convert_ayin = True,
                                        convert_la = True,
                                        convert_kurdish_tah = True,
                                        convert_kurdish_waw = True,
                                        convert_kurdish_kha = True,
                                        convert_kurdish_ga = True,
                                        remove_greek_letter = True,
                                        remove_hindi_letter = True,
                                        remove_mathematical_operators = True,
                                        remove_cyrillic_letter = True,
                                        remove_latin_letter = True,
                                        remove_currency = True,
                                        remove_punctuations = True,
                                        remove_number = True,
                                        remove_longest_than = True,
                                        remove_duplicate_word = True,
                                        remove_single_letter = True,
                                        remove_duplicated_letter = True,
                                        remove_unwanted_char = False,
                                        normalize_arabic_unicode = False,
                                        remove_unicode_and_special_character = True,
                                        remove_whitespace = True)




def machine_learning_inference(model, text, vectorizer):
    """
    Perform sentiment analysis inference using a machine learning model.

    Args:
        model: The trained machine learning model used for prediction.
        text (list of str): A list of text reviews to analyze.
        vectorizer: The vectorizer used to transform text data into numerical format.

    Returns:
        None: Prints the sentiment (Positive/Negative) for each review in the input text list.
    """
    text_ = list(map(text_normalization.text_normalization, text))
    text_vec = vectorizer.transform(text_)
    results = model.predict(text_vec)
    for i, review in enumerate(text):
        sentiment = "Positive" if results[i] == 1 else "Negative"
        print(f"Review: {review}\nSentiment: {sentiment}\n")


def deep_learning_inference(model, text, max_length, word_index):
    """
    Perform sentiment analysis inference using a deep learning model.

    Args:
        model (keras.Model): The pre-trained deep learning model for sentiment analysis.
        text (list of str): A list of text reviews to analyze.
        max_length (int): The maximum length of the input sequences.
        word_index (dict): A dictionary mapping words to their corresponding indices.

    Returns:
        None: This function prints the sentiment of each review in the input text list.
    """
    text_ = list(map(text_normalization.text_normalization, text))
    text_ = text_to_sequence(word_index = word_index, data = text_)
    text_ = sequences_padding(padding = 'pre', input_sequence = text_, max_length = max_length)
    results = model.predict([text_], verbose=0)
    for i, review in enumerate(text):
        sentiment = "Positive" if results[i] > 0.5 else "Negative"
        print(f"Review: {review}\nSentiment: {sentiment}\n")