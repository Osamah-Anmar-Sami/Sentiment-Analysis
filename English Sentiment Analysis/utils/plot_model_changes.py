import matplotlib.pyplot as plt

def plot_changes(histoty):
                    """
                    plots the training and validation curves of various performance metrics
                    during model training.

                    Args:
                        history (keras.callbacks.History): he training history object
                            returned after training a model using Keras

                    Returns:
                        matplotlib.pyplot.Figure: the generated plot object
                    """
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