def generate_poitive_negative(y_test, y_pred):
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

    return False_Positive, True_Positive, False_Negative, True_Negative
