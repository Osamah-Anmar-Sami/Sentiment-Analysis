import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def confusion_matrix_(true_positive, false_positive, true_negative, false_negative):
    """
    Create a confusion matrix DataFrame.

    Parameters:
    true_positive (int): The number of true positive predictions.
    false_positive (int): The number of false positive predictions.
    true_negative (int): The number of true negative predictions.
    false_negative (int): The number of false negative predictions.

    Returns:
    pd.DataFrame: A DataFrame representing the confusion matrix with the counts of true positives, false positives,
                  true negatives, and false negatives.
    """
    Confusion_matrix = pd.DataFrame(data=[[true_positive, false_positive], [false_negative, true_negative]], 
                                     columns=['Positive', 'Negative'], 
                                     index=['Positive', 'Negative'])
    return Confusion_matrix


def confusion_matrix_display(confusion_matrix, name):
    """
    Display the confusion matrix using a heatmap.

    Parameters:
    confusion_matrix (pd.DataFrame): The confusion matrix DataFrame to be displayed.
    name (str): The name of the model or task for labeling the plot title.

    Returns:
    None: This function does not return a value; it displays the confusion matrix as a heatmap.
    """
    sns.heatmap(confusion_matrix, annot=True, cbar=False, cmap='Greens', fmt='g');
    plt.xlabel("Prediction Label")
    plt.ylabel("Actual Label")
    plt.suptitle('Confusion Matrix Of {}'.format(name));
    plt.show()
