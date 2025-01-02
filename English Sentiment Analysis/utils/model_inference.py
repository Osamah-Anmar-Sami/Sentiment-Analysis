import tensorflow as tf
import numpy as np

def machine_learning_inference(model, text, vectorizer):
    """
    Perform sentiment analysis using a machine learning model.

    Parameters:
    model (sklearn.base.BaseEstimator): The trained machine learning model for sentiment analysis.
    text (list of str): A list of text reviews to analyze.
    vectorizer (sklearn.feature_extraction.text.Vectorizer): The vectorizer used to transform the text into feature vectors.

    Returns:
    None: This function does not return a value; it prints the sentiment analysis results for each review.
    """
    text_vec = vectorizer.transform(text)
    results = model.predict(text_vec)
    for i, review in enumerate(text):
        sentiment = "Positive" if results[i] == 1 else "Negative" 
        print(f"Review: {review}\nSentiment: {sentiment}\n")


def deep_learning_inference(model, text, tokenizer, max_length):
    """
    Perform sentiment analysis using a deep learning model.

    Parameters:
    model (tf.keras.Model): The trained deep learning model for sentiment analysis.
    text (list of str): A list of text reviews to analyze.
    tokenizer (tf.keras.preprocessing.text.Tokenizer): The tokenizer used to convert text into sequences.
    max_length (int): The maximum length of the input sequences for padding.

    Returns:
    None: This function does not return a value; it prints the sentiment analysis results for each review.
    """
    text_ = tokenizer.texts_to_sequences(text)
    text_ = tf.keras.utils.pad_sequences(sequences=text_, maxlen=max_length)
    results = model.predict([text_], verbose=0)
    for i, review in enumerate(text):
        sentiment = "Positive" if results[i] > 0.5 else "Negative"
        print(f"Review: {review}\nSentiment: {sentiment}\n")
