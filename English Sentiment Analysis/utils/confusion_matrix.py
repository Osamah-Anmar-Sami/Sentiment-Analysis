import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def confusion_matrix_(y_test, y_pred):
    """
    Computes the confusion matrix for binary classification.

    Parameters:
    y_test (list or array-like): True labels.
    y_pred (list or array-like): Predicted labels.

    Returns:
    pd.DataFrame: A confusion matrix with the following structure:
                  - Rows represent the actual classes (Positive, Negative).
                  - Columns represent the predicted classes (Positive, Negative).
                  - The values represent the counts of True Positives, False Positives, False Negatives, and True Negatives.
    """

    True_Positive, False_Positive =  0, 0
    True_Negative, False_Negative = 0, 0

    for i, j in zip(y_test, y_pred):
        if (i == 1) and (j == 1):
            True_Positive += 1
        if (i == 1) and (j != 1):
            False_Positive += 1
        if (i == 0) and (j == 0):
            True_Negative += 1
        if (i == 0) and (j != 0):
            False_Negative += 1

    Confusion_matrix = pd.DataFrame(data=[[True_Positive, False_Positive], [False_Negative, True_Negative]], 
                                     columns=['Positive', 'Negative'], 
                                     index=['Positive', 'Negative'])
    return Confusion_matrix



def confusion_matrix_display(confusion_matrix, name):
    """
    Displays a heatmap of the given confusion matrix using seaborn.

    Parameters:
    confusion_matrix (array-like): The confusion matrix to be displayed.
    name (str): The name or title to be displayed on the confusion matrix plot.

    Returns:
    None
    """

    sns.heatmap(confusion_matrix, annot=True, cbar=False, cmap='Greens', fmt='g');
    plt.xlabel("Prediction Label")
    plt.ylabel("Actual Label")
    plt.suptitle('Confusion Matrix Of {}'.format(name));
    plt.show()
