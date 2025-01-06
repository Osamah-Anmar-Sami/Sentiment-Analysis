def generate_poitive_negative(confusion_matrix):
    """
    Calculate the counts of true positives, false positives, true negatives, and false negatives.

    Parameters:
    y_test (iterable): The true labels (ground truth) for the test set. It should contain binary values (0 or 1).
    y_pred (iterable): The predicted labels from the model for the test set. It should also contain binary values (0 or 1).

    Returns:
    tuple: A tuple containing four integers:
        - False_Positive (int): The count of false positive predictions.
        - True_Positive (int): The count of true positive predictions.
        - False_Negative (int): The count of false negative predictions.
        - True_Negative (int): The count of true negative predictions.
    """
    True_Positive = confusion_matrix.loc['Positive']['Positive']
    False_Positive = confusion_matrix.loc['Positive']['Negative']
    True_Negative = confusion_matrix.loc['Negative']['Negative']
    False_Negative = confusion_matrix.loc['Negative']['Positive']

    return False_Positive, True_Positive, False_Negative, True_Negative
