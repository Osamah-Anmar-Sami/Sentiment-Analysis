import tensorflow as tf
from keras.layers import *
from tensorflow import *
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import *

def deeplearning_preprcosesing_(X_train, X_test, truncating, padding):
    tokenizer = Tokenizer(oov_token='<oov>')
    tokenizer.fit_on_texts(X_train)
    vocab_size = len(tokenizer.word_index)
    X_train_seqs = tokenizer.texts_to_sequences(X_train)
    X_test_seqs = tokenizer.texts_to_sequences(X_test)
    max_length =  max([len(x) for x in X_train_seqs])
    encoded_X_train = pad_sequences(X_train_seqs, maxlen=max_length, padding=padding, truncating=truncating)
    encoded_X_test = pad_sequences(X_test_seqs, maxlen=max_length, padding='pre', truncating=truncating)
    # y_train =  keras.utils.to_categorical(y_train_)
    # y_test =  keras.utils.to_categorical(y_test_)
    return tokenizer, vocab_size, max_length, encoded_X_train, encoded_X_test