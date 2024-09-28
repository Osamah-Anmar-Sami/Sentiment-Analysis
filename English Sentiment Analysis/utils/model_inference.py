import tensorflow as tf
import numpy as np

def machine_learning_inference(model, text, vectorizer):
    text_vec = vectorizer.transform(text)
    results = model.predict(text_vec)
    for i, review in enumerate(text):
        sentiment = "Positive" if results[i] == 1 else "Negative"
        print(f"Review: {review}\nSentiment: {sentiment}\n")
  

def deep_learning_inference(model, text, tokenizer, max_length):
    text_ = tokenizer.texts_to_sequences(text)
    text_ = tf.keras.utils.pad_sequences(sequences = text_, maxlen = max_length)
    results = model.predict([text_], verbose=0)
    for i, review in enumerate(text):
        sentiment = "Positive" if results[i] > 0.5 else "Negative"
        print(f"Review: {review}\nSentiment: {sentiment}\n")