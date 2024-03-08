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
        False_Postive = Confusin_Matrix.sum(axis=0) - np.diag(Confusin_Matrix)
        False_Postive = False_Postive.astype(int)
        False_Postive = sum(False_Postive)

        True_Positive = np.diag(Confusin_Matrix)
        True_Positive = True_Positive.astype(int)
        True_Positive = sum(True_Positive)

        
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
        False_Negative = Confusin_Matrix.sum(axis=1) - np.diag(Confusin_Matrix)
        False_Negative = False_Negative.astype(int)
        False_Negative = sum(False_Negative)


        True_Negative = Confusin_Matrix.sum()
        X = (Confusin_Matrix.sum(axis=0) - np.diag(Confusin_Matrix)) + (Confusin_Matrix.sum(axis=1) - np.diag(Confusin_Matrix)) + np.diag(Confusin_Matrix)
        True_Negative = True_Negative.astype(int) - X
        True_Negative = sum(True_Negative)
        
        return False_Negative, True_Negative
