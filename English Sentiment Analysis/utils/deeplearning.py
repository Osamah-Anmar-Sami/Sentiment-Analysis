import tensorflow as tf
from keras.layers import *
from tensorflow import *
from keras.preprocessing import *
import matplotlib.pyplot as plt


def lstm_(vocab_size, embedding_dim, max_length, dropout, units1, embeddings_matrix, units2):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,   weights=[embeddings_matrix]),
                LSTM(units=units1),
                Dropout(dropout),
                Dense(units2, activation= 'relu'),
                Dense(1, activation= 'sigmoid')
                ])     
            return model  

def gru_(vocab_size, embedding_dim, max_length, dropout, units1, embeddings_matrix, units2):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,  weights=[embeddings_matrix]),
                GRU(units=units1),
                Dropout(dropout),
                Dense(units2, activation= 'relu'),
                Dense(1, activation= 'sigmoid')
                ])     
            return model


def bidirectional_lstm(vocab_size, embedding_dim, max_length, dropout, units1, embeddings_matrix, units2):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,   weights=[embeddings_matrix]),
                Bidirectional(LSTM(units=units1)),
                Dropout(dropout),
                Dense(units2, activation= 'relu'),
                Dense(1, activation= 'sigmoid')
                ])     
            return model  


def model_compile(model) :
        model.compile(optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=0.0001),
                            loss=tf.keras.losses.BinaryCrossentropy(),
                            metrics=['accuracy'])
    
def model_fit(model, X_train, y_train, epochs, X_test, y_test, batch_size, Callback):
            history = model.fit(X_train, y_train,
                    epochs=epochs,
                    validation_data=(X_test, y_test),
                    batch_size=batch_size,
                    callbacks=[Callback])
            return history
    

