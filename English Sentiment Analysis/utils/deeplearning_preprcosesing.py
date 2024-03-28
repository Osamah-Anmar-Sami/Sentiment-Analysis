import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import *
from keras.layers import *
from keras.preprocessing.sequence import pad_sequences

def deeplearning_preprcosesing_(X_train, X_test, truncating, padding,):
    """
    Perform pre-processing steps for deep learning tasks, including tokenization and padding.

    Args:
      X_train (list): List of training text data.
      X_test (list): List of testing text data.
      truncating (string): Method for truncating sequences ('pre' or 'post').
      padding (string): Method for padding sequences ('pre' or 'post').


    Returns:
        tokenizer: Tokenizer object fitted on the training data.
        vocab_size (integer): Size of the vocabulary based on the training data.
        max_length (integer): Maximum length of sequences in the training data.
        encoded_X_train (numpy.ndarray): Padded and encoded training sequences.
        encoded_X_test (numpy.ndarray): Padded and encoded testing sequences.
    """
    tokenizer = Tokenizer(oov_token='<oov>')
    tokenizer.fit_on_texts(X_train)
    word_index = tokenizer.word_index
    vocab_size = len(word_index)
    X_train_seqs = tokenizer.texts_to_sequences(X_train)
    X_test_seqs = tokenizer.texts_to_sequences(X_test)
    max_length =  max([len(x) for x in X_train_seqs])
    encoded_X_train = pad_sequences(X_train_seqs,  padding=padding, truncating=truncating, maxlen=max_length)
    encoded_X_test = pad_sequences(X_test_seqs, padding=padding, truncating=truncating,maxlen=max_length)
    return tokenizer, vocab_size, max_length, encoded_X_train , encoded_X_test, word_index