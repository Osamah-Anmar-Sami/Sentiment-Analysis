from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

def confusion_matrix_(y_test, y_pred):
        """ Compute the confusion matrix for a classification model

        Args:
            y_test (array-like): True labels of the test set
            y_pred (array-like): Predicted labels of the test set

         Returns:
                ndarray: The confusion matrix, a 2D array of shape (n_classes, n_classes),
                 where n_classes is the number of unique classes in y_test and y_pred
        """     
        confusionmatrix = confusion_matrix(y_pred, y_test)
        return confusionmatrix


def confusion_matrix_display(confusionmatrix, name):
        """
        Display a visual representation of the confusion matrix.

        Args:
          confusionmatrix (array-like): The confusion matrix to be visualized.
          name (string): The name or label associated with the confusion matrix

        Returns:
           None: Displays the confusion matrix plot using Matplotlib
    """
        disp = ConfusionMatrixDisplay(confusion_matrix=confusionmatrix, display_labels=['Positive', 'Negative', 'Neutral'])
        disp.plot(cmap='YlGnBu_r', colorbar=False, xticks_rotation='vertical', values_format='d')
        plt.title('{} Confusion Matrix'.format(name))
        plt.rcParams['font.size'] = '10'
        plt.grid(None)
        return plt.show()