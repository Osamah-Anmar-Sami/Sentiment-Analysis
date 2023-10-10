import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def machine_learning_model(algorithm):
        model = algorithm
        return model
        

def fit_model(model, X_train, y_train):
        model.fit(X_train, y_train)
        return model
    
def metrics_values(model, X_test, y_test):
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1score = f1_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        error = 1-accuracy
        MetricsValues = pd.DataFrame(index=['Accuracy', 'Precision','Recall', 'F1Score', 'Error'], columns=['Values'], data=[accuracy, precision, recall, f1score, error])
        return MetricsValues