import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def machine_learning_model(algorithm):
        model = algorithm
        return model
        

def fit_model(model, X_train, y_train):
        model.fit(X_train, y_train)
        return model
        