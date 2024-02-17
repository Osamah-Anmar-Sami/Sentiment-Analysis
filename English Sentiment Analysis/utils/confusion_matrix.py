from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

def confusion_matrix_(y_test, y_pred):
        confusionmatrix = confusion_matrix(y_pred, y_test)
        return confusionmatrix


def confusion_matrix_display(confusionmatrix, name):
        disp = ConfusionMatrixDisplay(confusion_matrix=confusionmatrix, display_labels=['Positive', 'Negative'])
        disp.plot(cmap='GnBu', colorbar=False, xticks_rotation='vertical', values_format='d')
        plt.title('{} Confusion Matrix'.format(name))
        plt.rcParams['font.size'] = '10'
        plt.grid(None)
        return plt.show()