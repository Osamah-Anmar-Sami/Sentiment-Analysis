import tensorflow as tf
import keras
from keras.layers import Embedding, LSTM, Dense, GRU, Bidirectional # type: ignore
from tensorflow import *
from keras.preprocessing import * # type: ignore
from keras.callbacks import ReduceLROnPlateau, EarlyStopping # type: ignore

def callbacks_ ():
        """
        Creates and returns a tuple of Keras callbacks for training deep learning models.

        The callbacks included are:
        - ReduceLROnPlateau: Reduces the learning rate when a metric has stopped improving.
        - EarlyStopping: Stops training when a monitored metric has stopped improving.

        Returns:
            tuple: A tuple containing the ReduceLROnPlateau and EarlyStopping callbacks.
        """
        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.3, patience=3, min_lr=0.001, mode = 'min')
        early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True,)

        return reduce_lr, early_stop

def lstm_(vocab_size, embedding_dim, max_length, units, embeddings_matrix):        
            """
            Builds and returns an LSTM model for sentiment analysis.

            Args:
                vocab_size (int): Size of the vocabulary.
                embedding_dim (int): Dimension of the embedding vectors.
                max_length (int): Maximum length of input sequences.
                units (int): Number of LSTM units.
                embeddings_matrix (numpy.ndarray): Pre-trained embeddings matrix.

            Returns:
                tf.keras.Sequential: A compiled LSTM model.
            """
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length, weights = [embeddings_matrix],  trainable = True),
                LSTM(units=units),
                Dense(1, activation='sigmoid')
                ])     
            return model  

def gru_(vocab_size, embedding_dim, max_length, units, embeddings_matrix):            
            """
            Builds and returns a GRU-based neural network model for sentiment analysis.

            Args:
                vocab_size (int): Size of the vocabulary.
                embedding_dim (int): Dimension of the embedding vectors.
                max_length (int): Maximum length of input sequences.
                units (int): Number of units in the GRU layer.
                embeddings_matrix (numpy.ndarray): Pre-trained embedding matrix.

            Returns:
                tf.keras.Sequential: A compiled GRU-based neural network model.
            """
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,  weights = [embeddings_matrix], trainable = True),
                GRU(units=units),
                Dense(1, activation='sigmoid')
                ])     
            return model


def bidirectional_lstm(vocab_size, embedding_dim, max_length, units, embeddings_matrix):
            """
            Builds a Bidirectional LSTM model for sentiment analysis.

            Args:
                vocab_size (int): Size of the vocabulary.
                embedding_dim (int): Dimension of the embedding vectors.
                max_length (int): Maximum length of the input sequences.
                units (int): Number of units in the LSTM layer.
                embeddings_matrix (numpy.ndarray): Pre-trained embeddings matrix.

            Returns:
                keras.Sequential: A compiled Bidirectional LSTM model.
            """
            model = keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length, weights = [embeddings_matrix],  trainable = True),
                Bidirectional(LSTM(units=units)),
                Dense(1, activation='sigmoid')
                ])     
            return model  


def model_compile(model) :
            """
            Compiles a given Keras model with specified optimizer, loss function, and metrics.

            Args:
                model (tf.keras.Model): The Keras model to be compiled.

            Returns:
                None: The function modifies the model in place and does not return anything.
            """
            return model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                            loss=tf.keras.losses.BinaryCrossentropy(),
                            metrics= ['accuracy'])
    
def model_fit(model, X_train, y_train, epochs, batch_size, X_test, y_test):       
        """
        Trains the given model using the provided training data and evaluates it on the test data.

        Args:
            model: The deep learning model to be trained.
            X_train: Training data features.
            y_train: Training data labels.
            epochs: Number of epochs to train the model.
            batch_size: Number of samples per gradient update.
            X_test: Test data features for validation.
            y_test: Test data labels for validation.

        Returns:
            history: A History object. Its History.history attribute is a record of training loss values 
                     and metrics values at successive epochs, as well as validation loss values and 
                     validation metrics values.
        """
        reduce_lr, early_stop = callbacks_()
        history = model.fit(X_train, y_train,
                    epochs=epochs,
                    batch_size=batch_size,
                    validation_data = (X_test, y_test),
                    callbacks=[early_stop, reduce_lr])
        return history

def model_evaluate(x_test, y_test, model):
        """
        Evaluates the performance of a given model on the test dataset and prints the test loss and accuracy.

        Parameters:
        x_test (array-like): Test data features.
        y_test (array-like): True labels for the test data.
        model (keras.Model): Trained model to be evaluated.

        Returns:
        None
        """
        score = model.evaluate(x_test, y_test, verbose=0)
        print(f'Test loss: {score[0]}')
        print(f'Test accuracy: {score[1]}')