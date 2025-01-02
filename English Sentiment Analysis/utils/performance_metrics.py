import pandas as pd
def accuracy_score(True_Positive, True_Negative, False_Positive, False_Negative):
        """Calculates the accuracy score of a model

    Args:
        True_Positive (integer): number of correctly classified positive examples.
        True_Negative (integer): number of correctly classified negative examples.
        False_Positive (integer): number of incorrectly classified positive examples.
        False_Negative (integer): number of incorrectly classified negative examples.

    Returns:
        float: the accuracy score, ranging from 0 (worst) to 1 (perfect).
    """
        Accuracy = (True_Positive + True_Negative) / (True_Positive + True_Negative + False_Positive + False_Negative)
        return Accuracy
    
def precision_score(True_Positive, False_Positive):
        """calculates the precision score of a model.

    Args:
        true_Positive (integer): number of correctly classified positive examples
        false_Positive (integer): number of incorrectly classified positive examples

    Returns:
        float: the precision score, ranging from 0 (worst) to 1 (perfect).
    """
        Precision = ((True_Positive) / (True_Positive + False_Positive))
        return Precision
    
def sensitivity_score(True_Positive, False_Negative):
        """calculates the sensitivity (recall) score of a model

    Args:
        True_Positive (integer): number of correctly classified positive examples
        False_Negative (integer): number of incorrectly classified negative examples

    Returns:
        float: the sensitivity score, ranging from 0 (worst) to 1 (perfect)
    """
        Sensitivity = ((True_Positive ) / (True_Positive  + False_Negative)) 
        return Sensitivity

def specificity_score(True_Negative, False_Positive):
        """calculates the specificity score of a model

    Args:
        True_Negative (integer): number of correctly classified negative examples
        False_Positive (integer): nuumber of incorrectly classified positive examples (Type I error)

    Returns:
        float: the specificity score, ranging from 0 (worst) to 1 (perfect)
    """
        Specificity = ((True_Negative) / (True_Negative + False_Positive)) 
        return Specificity
    
def f1_score(True_Positive, False_Negative, False_Positive):
        """calculates the F1 score (harmonic mean of precision and recall) of a model

        Args:
                True_Positive (integer): number of correctly classified positive examples
                False_Negative (integer): number of incorrectly classified negative examples (Type II error)
                False_Positive (integer): number of incorrectly classified positive examples (Type I error)

        Returns:
                float: the F1 score, ranging from 0 (worst) to 1 (perfect).
        """
        F1Score = (True_Positive) / (True_Positive + (0.5*(False_Positive + False_Negative)))
        return F1Score
    
def error_rate(True_Positive, True_Negative, False_Positive, False_Negative):
        """calculates the error rate (misclassification rate) of a model

    Args:
        True_Positive (integer): number of correctly classified positive examples (Type II error)
        True_Negative (integer): number of correctly classified negative examples
        False_Positive (integer): number of incorrectly classified positive examples (Type I error)
        False_Negative (integer): number of incorrectly classified negative examples (Type II error)

    Returns:
        float: the error rate, ranging from 0 (perfect) to 1 (worst).
    """
        Error = ((False_Positive + False_Negative) / (True_Positive + True_Negative + False_Positive + False_Negative)) 
        return Error 

def performance_metrics_data_frame(Accuracy, Precision, Sensitivity,  Specificity, F1Score, Error):
        """
    creates a pandas DataFrame containing various classification performance metrics

    Args:
        Accuracy (float): the accuracy score of the model
        Precision (float): the precision score of the model
        Sensitivity (float): the sensitivity (recall) score of the model
        Specificity (float): the specificity score of the model
        F1Score (float): the F1 score of the model
        Error (float): the error rate (misclassification rate) of the model

    Returns:
        pandas.DataFrame: A DataFrame with rows representing the performance metrics
                         and columns representing the metric values
    """
        MetricsValues = pd.DataFrame(columns=['Values'], index = ['Accuracy', 'Precision', 'Sensitivity', 'Specificity', 'F1Score', 'Error'], data=[Accuracy, Precision, Sensitivity,  Specificity, F1Score, Error])
        return MetricsValues

