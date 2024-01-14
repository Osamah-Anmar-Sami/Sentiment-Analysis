import pandas as pd
def accuracy_score(True_Positive, True_Negative, False_Positive, False_Negative):
        Accuracy = (True_Positive + True_Negative) / (True_Positive + True_Negative + False_Positive + False_Negative)
        return Accuracy
    
def precision_score(True_Positive, False_Positive):
        Precision = ((True_Positive) / (True_Positive + False_Positive))
        return Precision
    
def sensitivity_score(True_Positive, False_Negative):
        Sensitivity = ((True_Positive ) / (True_Positive  + False_Negative)) 
        return Sensitivity

def specificity_score(True_Negative, False_Positive):
        Specificity = ((True_Negative) / (True_Negative + False_Positive)) 
        return Specificity
    
def f1_score(True_Positive, False_Negative, False_Positive):
        F1Score = (True_Positive) / (True_Positive + (0.5*(False_Positive + False_Negative)))
        return F1Score
    
def error_rate(True_Positive, True_Negative, False_Positive, False_Negative):
        Error = ((False_Positive + False_Negative) / (True_Positive + True_Negative + False_Positive + False_Negative)) 
        return Error 

def false_negative_rate(True_Positive, False_Negative):
        FalseNegativeRate = (False_Negative) / (False_Negative + True_Positive)
        return FalseNegativeRate 

def false_positive_rate(False_Positive, True_Negative):
        FalsePositiveRate = (False_Positive) / (False_Positive + True_Negative)
        return FalsePositiveRate 

def performance_metrics_data_frame(Accuracy, Precision, Sensitivity,  Specificity, F1Score, Error, False_Negative_Rate, False_Positive_Rate):
        MetricsValues = pd.DataFrame(columns=['Values'], index = ['Accuracy', 'Precision', 'Sensitivity', 'Specificity', 'F1Score', 'Error', 'False Negative Rate', 'False Positive Rate'], data=[Accuracy, Precision, Sensitivity,  Specificity, F1Score, Error, False_Negative_Rate, False_Positive_Rate])
        return MetricsValues

