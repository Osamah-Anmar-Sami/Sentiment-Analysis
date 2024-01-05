import tensorflow as tf
from keras.layers import *
from tensorflow import *
from keras.preprocessing import *
import matplotlib.pyplot as plt

def convolutional_neural_network_1d(vocab_size, embedding_dim, max_length, dropout, filters, kernel, strides, padding, embeddings_matrix, units_):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
                Conv1D(filters=filters, kernel_size = kernel, activation='relu', strides = strides, padding = padding),
                GlobalAveragePooling1D(),
                Dropout(dropout),
                BatchNormalization(),
                Dense(units_, activation= 'relu'),
                BatchNormalization(),
                Dense(3, activation= 'softmax')
                ])     
            return model

def lstm_(vocab_size, embedding_dim, max_length, dropout, units, embeddings_matrix, units_):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
                LSTM(units=units, return_sequences=False),
                Dropout(dropout),
                BatchNormalization(),
                Dense(units_, activation= 'relu'),
                BatchNormalization(),
                Dense(3, activation= 'softmax')
                ])     
            return model  

def gru_(vocab_size, embedding_dim, max_length, dropout, units, embeddings_matrix, units_):
            model = tf.keras.Sequential([
                Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
                GRU(units=units, return_sequences=False),
                Dropout(dropout),
                BatchNormalization(),
                Dense(units_, activation= 'relu'),
                BatchNormalization(),
                Dense(3, activation= 'softmax')
                ])     
            return model  

    
def model_compile(model) :
        return model.compile(optimizer=tf.keras.optimizers.legacy.RMSprop(learning_rate=0.001),
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

