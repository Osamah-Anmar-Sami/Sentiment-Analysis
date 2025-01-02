import tensorflow as tf
import keras
from keras.layers import Embedding, LSTM, Dense, Dropout, GRU, Bidirectional # type: ignore
from tensorflow import *
from keras.preprocessing import * # type: ignore
import matplotlib.pyplot as plt
from keras.callbacks import ReduceLROnPlateau, EarlyStopping # type: ignore

def callbacks_ ():
    """create callback functions for model training

    Args:
        name (string): name using for model checkpoint file

    Returns:
        tuple: A tuple containing three callbacks:
            - ReduceLROnPlateau: Reduces learning rate when validation loss plateaus
            - EarlyStopping: Stops training when validation loss stops improving
            - ModelCheckpoint: Saves the best model weights based on validation loss
    """    ""
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.001)
    early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True,)

    return reduce_lr, early_stop

def lstm_(vocab_size, embedding_dim, max_length, units,  embeddings_matrix):
            """
        creates and returns a sequential LSTM model for sentiment analysis

        Args:
            vocab_size (integer): Size of the vocabulary (number of unique words).
            embedding_dim (integer): dimensionality of word embeddings
            units (integer): number of units in the first LSTM layer
            embeddings_matrix (np.ndarray): pre-trained word embedding matrix

        Returns:
            keras.Model: the compiled LSTM model
        """   
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,  weights = [embeddings_matrix], trainable = True),
                LSTM(units=units),
                Dense(1, activation= 'sigmoid')
                ])     
            return model  

def gru_(vocab_size, embedding_dim, max_length, units, embeddings_matrix):
            """
                creates and returns a sequential GRU model for sentiment analysis

                Args:
                    vocab_size (integer): size of the vocabulary (number of unique words)
                    embedding_dim (integer): dimensionality of word embeddings
                    units(integer): number of units in the first GRU layer
                    embeddings_matrix (np.ndarray): pre-trained word embedding matrix

                Returns:
                    keras.Model: the compiled GRU model
             """
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,  weights = [embeddings_matrix], trainable = True),
                GRU(units=units),
                Dense(1, activation= 'sigmoid')
                ])     
            return model


def bidirectional_lstm(vocab_size, embedding_dim, max_length, units,  embeddings_matrix):
            """
                creates and returns a sequential bidirectional LSTM model for sentiment analysis

                Args:
                    vocab_size (integer): size of the vocabulary (number of unique words)
                    embedding_dim (integer): dimensionality of word embeddings
                    units (integer): number of units in the bidirectional LSTM layer
                    embeddings_matrix (np.ndarray): pre-trained word embedding matrix

                Returns:
                    keras.Model: the compiled bidirectional LSTM model.
            """
            model = keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,  weights = [embeddings_matrix], trainable = True),
                Bidirectional(LSTM(units=units)),
                Dense(1, activation= 'sigmoid', kernel_initializer=tf.keras.initializers.GlorotUniform(seed=100), kernel_regularizer=keras.regularizers.L2(l2=0.001))
                ])     
            return model  


def model_compile(model) :
        """
            compiles a provided Keras model with a common configuration suitable for sentiment analysis tasks

            Args:
                model (keras.Model): the Keras model to be compiled

            Returns:
                keras.Model: the compiled Keras model
    """
        return model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
                            loss=tf.keras.losses.BinaryCrossentropy(),
                            metrics= ['accuracy'])
    
def model_fit(model, X_train, y_train, epochs, X_test, y_test, batch_size):       
        """
            fits a Keras model on training data with validation and early stopping.

        Args:
            model (keras.Model): the Keras model to be trained
            X_train (np.ndarray): training data features
            y_train (np.ndarray): training data labels
            epochs (int): number of training epochs
            X_test (np.ndarray): validation data features
            y_test (np.ndarray): validation data labels
            batch_size (int): batch size for training
            class_weights (dict, optional): dictionary of class weights for imbalanced datasets. Defaults to None
            name (string): name to be used for model checkpoint files

        Returns:
            keras.callbacks.History: Training history object containing performance metrics.
        """
        reduce_lr, early_stop = callbacks_()
        history = model.fit(X_train, y_train,
                    epochs=epochs,
                    validation_data=(X_test, y_test),
                    batch_size=batch_size,
                    callbacks=[early_stop, reduce_lr])
        return history
    

