import pandas as pd
def accuracy_score(True_Positive, True_Negative, False_Positive, False_Negative):
        """
        Calculate the accuracy score.

        Accuracy is defined as the ratio of correctly predicted instances (both true positives and true negatives)
        to the total number of instances.

        Args:
            True_Positive (int): The number of true positive instances.
            True_Negative (int): The number of true negative instances.
            False_Positive (int): The number of false positive instances.
            False_Negative (int): The number of false negative instances.

        Returns:
            float: The accuracy score as a float value.
        """
        Accuracy = (True_Positive + True_Negative) / (True_Positive + True_Negative + False_Positive + False_Negative)
        return Accuracy
    
def precision_score(True_Positive, False_Positive):
        """
        Calculate the precision score.

        Precision is the ratio of correctly predicted positive observations 
        to the total predicted positives. It is calculated as:
        
            Precision = True_Positive / (True_Positive + False_Positive)
        
        Args:
            True_Positive (int): The number of true positive cases.
            False_Positive (int): The number of false positive cases.

        Returns:
            float: The precision score.
        """
        Precision = ((True_Positive) / (True_Positive + False_Positive))
        return Precision
    
def sensitivity_score(True_Positive, False_Negative):
        """
        Calculate the sensitivity score (also known as recall or true positive rate).

        Sensitivity measures the proportion of actual positives that are correctly identified.

        Args:
            True_Positive (int): The number of true positive cases.
            False_Negative (int): The number of false negative cases.

        Returns:
            float: The sensitivity score, which is the ratio of true positives to the sum of true positives and false negatives.
        """
        Sensitivity = ((True_Positive ) / (True_Positive  + False_Negative)) 
        return Sensitivity

def specificity_score(True_Negative, False_Positive):
        """
        Calculate the specificity score.

        Specificity, also known as the true negative rate, measures the proportion of actual negatives that are correctly identified as such.

        Args:
            True_Negative (int): The number of true negative cases.
            False_Positive (int): The number of false positive cases.

        Returns:
            float: The specificity score, calculated as True_Negative / (True_Negative + False_Positive).
        """
        Specificity = ((True_Negative) / (True_Negative + False_Positive)) 
        return Specificity
    
def f1_score(True_Positive, False_Negative, False_Positive):
        """
        Calculate the F1 score, which is the harmonic mean of precision and recall.

        Args:
            True_Positive (int): The number of true positive cases.
            False_Negative (int): The number of false negative cases.
            False_Positive (int): The number of false positive cases.

        Returns:
            float: The F1 score.
        """
        F1Score = (True_Positive) / (True_Positive + (0.5*(False_Positive + False_Negative)))
        return F1Score
    
def error_rate(True_Positive, True_Negative, False_Positive, False_Negative):
        """
        Calculate the error rate of a classification model.

        The error rate is defined as the proportion of incorrect predictions 
        (False Positives and False Negatives) out of the total number of predictions.

        Parameters:
        True_Positive (int): The number of true positive predictions.
        True_Negative (int): The number of true negative predictions.
        False_Positive (int): The number of false positive predictions.
        False_Negative (int): The number of false negative predictions.

        Returns:
        float: The error rate of the model.
        """
        Error = ((False_Positive + False_Negative) / (True_Positive + True_Negative + False_Positive + False_Negative)) 
        return Error 

def performance_metrics_data_frame(Accuracy, Precision, Sensitivity,  Specificity, F1Score, Error):
        def performance_metrics_data_frame(Accuracy, Precision, Sensitivity, Specificity, F1Score, Error):
            """
            Creates a pandas DataFrame to store performance metrics values.

            Args:
                Accuracy (float): The accuracy of the model.
                Precision (float): The precision of the model.
                Sensitivity (float): The sensitivity (recall) of the model.
                Specificity (float): The specificity of the model.
                F1Score (float): The F1 score of the model.
                Error (float): The error rate of the model.

            Returns:
                pd.DataFrame: A DataFrame containing the performance metrics with their corresponding values.
            """
        MetricsValues = pd.DataFrame(columns=['Values'], index = ['Accuracy', 'Precision', 'Sensitivity', 'Specificity', 'F1Score', 'Error'], data=[Accuracy, Precision, Sensitivity,  Specificity, F1Score, Error])
        return MetricsValues

