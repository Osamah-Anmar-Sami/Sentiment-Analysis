import numpy as np


def false_true_positive(Confusin_Matrix):
    """
    Calculates the number of False Positives and True Positives from a confusion matrix.

    Args:
        confusion_matrix (np.ndarray): A 2D array representing a confusion matrix, where rows represent actual classes and columns represent predicted classes.

    Returns:
        tuple: A tuple containing two elements:
            - False positives (int): the total number of False Positives.
            - True positives (int): the total number of True Positives.
    """
    False_Postive = Confusin_Matrix[0,1]
    True_Positive = Confusin_Matrix[0, 0]

    return False_Postive, True_Positive


def false_true_negative(Confusin_Matrix):
        """
        calculates the number of False Negatives and True Negatives from a confusion matrix.

        Args:
                confusion_matrix (np.ndarray): A 2D array representing a confusion matrix, where rows represent actual classes and columns represent predicted classes.

        Returns:
                tuple: A tuple containing two elements:
                - False negatives (int): the total number of False Negatives
                - True negatives (int): the total number of True Negatives
    """
        False_Negative = Confusin_Matrix[1,0]
        True_Negative = Confusin_Matrix[1, 1]
        
        return False_Negative, True_Negative
