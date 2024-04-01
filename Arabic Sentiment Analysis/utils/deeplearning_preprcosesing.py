from keras.layers import *
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import *

def deeplearning_preprcosesing_(X_train, X_test, truncating, padding, y_train_, y_test_):
    """
    Perform pre-processing steps for deep learning tasks, including tokenization and padding.

    Args:
      X_train (list): List of training text data.
      X_test (list): List of testing text data.
      truncating (string): Method for truncating sequences ('pre' or 'post').
      padding (string): Method for padding sequences ('pre' or 'post').
      y_train (array-like): Array of labels for the training set.
      y_test (array-like): Array of labels for the testing set.

    Returns:
        tokenizer: Tokenizer object fitted on the training data.
        vocab_size (integer): Size of the vocabulary based on the training data.
        max_length (integer): Maximum length of sequences in the training data.
        encoded_X_train (numpy.ndarray): Padded and encoded training sequences.
        encoded_X_test (numpy.ndarray): Padded and encoded testing sequences.
        encoded_y_train (tensorflow.Tensor): One-hot encoded labels for the training set.
        encoded_y_test (tensorflow.Tensor): One-hot encoded labels for the testing set.
    """
    tokenizer = Tokenizer(oov_token='<oov>')
    tokenizer.fit_on_texts(X_train)
    word_index = tokenizer.word_index
    vocab_size = len(word_index)
    X_train_seqs = tokenizer.texts_to_sequences(X_train)
    X_test_seqs = tokenizer.texts_to_sequences(X_test)
    max_length =  max([len(x) for x in X_train_seqs])
    encoded_X_train = pad_sequences(X_train_seqs, maxlen=max_length, padding=padding, truncating=truncating)
    encoded_X_test = pad_sequences(X_test_seqs, maxlen=max_length, padding='pre', truncating=truncating)
    encoded_y_train =  tf.one_hot(indices = y_train_, depth = 3)
    encoded_y_test =   tf.one_hot(indices = y_test_, depth = 3)
    return tokenizer, vocab_size, max_length, encoded_X_train, encoded_X_test, encoded_y_train, encoded_y_test, word_index