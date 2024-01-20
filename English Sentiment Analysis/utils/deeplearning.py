import tensorflow as tf
from keras.layers import *
from tensorflow import *
from keras.preprocessing import *
import matplotlib.pyplot as plt


def lstm_(vocab_size, embedding_dim, max_length, dropout1,dropout2, units1, units2, units3, embeddings_matrix):
        model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length, weights=[embeddings_matrix],  trainable=False),
                LSTM(units=units1, return_sequences=True),
                LSTM(units=units2, return_sequences=False),
                Dropout(dropout1),
                BatchNormalization(),
                Dense(units3, activation='tanh', kernel_regularizer=tf.keras.regularizers.L2(l2=0.001)),
                Dropout(dropout2),
                BatchNormalization(),
                Dense(1, activation= 'sigmoid')
                ])         
        return model  

def gru_(vocab_size, embedding_dim, max_length, dropout1,dropout2, units1, units2, units3, embeddings_matrix):
        model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,  weights=[embeddings_matrix],  trainable=False),
                GRU(units=units1, return_sequences=True),
                GRU(units=units2, return_sequences=False),
                Dropout(dropout1),
                BatchNormalization(),
                Dense(units3, activation='tanh', kernel_regularizer=tf.keras.regularizers.L2(l2=0.001)),
                Dropout(dropout2),
                BatchNormalization(),
                Dense(1, activation= 'sigmoid')
                ])         
        return model 


def bidirectional_lstm(vocab_size, embedding_dim, max_length, dropout1,dropout2, units1, units2, units3, embeddings_matrix):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length,  weights=[embeddings_matrix],  trainable=False),
                Bidirectional(LSTM(units1, return_sequences=True)),
                Bidirectional(LSTM(units2, return_sequences=False)),
                Dropout(dropout1),
                BatchNormalization(),
                Dense(units3, activation='tanh', kernel_regularizer=tf.keras.regularizers.L2(l2=0.001)),
                Dropout(dropout2),
                BatchNormalization(),
                Dense(1, activation= 'sigmoid')
                ])       
            return model  


def model_compile(model) :
        lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
                initial_learning_rate=0.001,
                decay_steps=10000,
                decay_rate=0.9)

                # staircase

        return model.compile(optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=lr_schedule),
                            loss='binary_crossentropy',
                            metrics=['accuracy'])
    
def model_fit(model, X_train, y_train, epochs, X_test, y_test, batch_size, stop):
            history = model.fit(X_train, y_train,
                    epochs=epochs,
                    validation_data=(X_test, y_test),
                    batch_size=batch_size,
                    callbacks=[stop])
            return history