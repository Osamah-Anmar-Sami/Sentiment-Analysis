import tensorflow as tf
from keras.layers import *
from tensorflow import *
from keras.preprocessing import *
import matplotlib.pyplot as plt


def lstm_(vocab_size, embedding_dim, max_length, dropout, units, embeddings_matrix, units_):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
                LSTM(units=units_),
                Dense(64, activation= 'relu'),
                Dropout(dropout),
                Dense(units_, activation= 'relu'),
                Dense(3, activation= 'softmax')
                ])     
            return model  

def gru_(vocab_size, embedding_dim, max_length, dropout, units, embeddings_matrix, units_):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
                GRU(units=units_),
                Dense(64, activation= 'relu'),
                Dropout(dropout),
                Dense(units_, activation= 'relu'),
                Dense(3, activation= 'softmax')
                ])     
            return model


def bidirectional_lstm(vocab_size, embedding_dim, max_length, dropout, units, embeddings_matrix, units_):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
                Bidirectional(LSTM(units=units_)),
                Dense(64, activation= 'relu'),
                Dropout(dropout),
                Dense(units_, activation= 'relu'),
                Dense(3, activation= 'softmax')
                ])     
            return model  


def model_compile(model) :
        return model.compile(optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=0.0001),
                            loss=tf.keras.losses.CategoricalHinge(),
                            metrics=['accuracy'])
    
def model_fit(model, X_train, y_train, epochs, X_test, y_test, batch_size, Callback):
            history = model.fit(X_train, y_train,
                    epochs=epochs,
                    validation_data=(X_test, y_test),
                    batch_size=batch_size,
                    callbacks=[Callback ])
            return history
    
def evaluate(model, x, y, train_test):
                loss, accuracy = model.evaluate(x, y, verbose=False)
                print(" ")
                print('The {} Loss is {:.4f}, And {} Accuracy is {:.4f}'.format(train_test, loss, train_test, accuracy))

def plot_accuracy_loss(histoty):
                    accuracy = histoty.history['accuracy']
                    loss = histoty.history['loss']  
                    val_accuracy = histoty.history['val_accuracy']
                    val_loss = histoty.history['val_loss']

                    plt.plot(accuracy, label='Accuracy')
                    plt.plot(loss, label='Loss')
                    plt.plot(val_accuracy, label='Val_Accuracy')
                    plt.plot(val_loss, label='Val_Loss')
                    plt.legend()
                    return plt.show()

