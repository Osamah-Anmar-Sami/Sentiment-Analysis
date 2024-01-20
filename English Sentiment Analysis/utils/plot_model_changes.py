import matplotlib.pyplot as plt

def plot_changes(histoty):
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