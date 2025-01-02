import matplotlib.pyplot as plt

def plot_changes(histoty):
                    """
                    Plots the training and validation accuracy and loss from the history of a model training process.

                    Args:
                        histoty (History): A History object returned by the fit method of a Keras model. 
                                           It contains the training and validation accuracy and loss for each epoch.

                    Returns:
                        None: The function displays the plot and does not return any value.
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