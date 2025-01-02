def generate_poitive_negative(confusion_matrix):
    """
    Extracts the counts of true positives, false positives, true negatives, and false negatives from a confusion matrix.

    Args:
        confusion_matrix (pandas.DataFrame): A confusion matrix with actual labels as rows and predicted labels as columns.

    Returns:
        tuple: A tuple containing the counts of false positives, true positives, false negatives, and true negatives in the following order:
            (False_Positive, True_Positive, False_Negative, True_Negative)
    """
    True_Positive = confusion_matrix.loc['Positive']['Positive']
    False_Positive = confusion_matrix.loc['Positive']['Negative']
    True_Negative = confusion_matrix.loc['Negative']['Negative']
    False_Negative = confusion_matrix.loc['Negative']['Positive']

    return False_Positive, True_Positive, False_Negative, True_Negative
