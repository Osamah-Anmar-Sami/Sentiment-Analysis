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
    
def metrics_values(model, X_test, y_test):
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1score = f1_score(y_test, y_pred, average = 'macro')
        precision = precision_score(y_test, y_pred, average = 'macro')
        recall = recall_score(y_test, y_pred, average = 'macro')
        error = 1-accuracy
        MetricsValues = pd.DataFrame(index=['Accuracy', 'Precision','Recall', 'F1Score', 'Error'], columns=['Values'], data=[accuracy, precision, recall, f1score, error])
        return MetricsValues

def confusion_matrix_(model, X_test, y_test, name):
        y_pred = model.predict(X_test)
        confusionmatrix = confusion_matrix(y_pred, y_test)
        disp = ConfusionMatrixDisplay(confusion_matrix=confusionmatrix, display_labels=['Negative', 'Positive', 'Neutral'])
        disp.plot(cmap='YlGnBu_r', colorbar=False, xticks_rotation='vertical', values_format='d')
        plt.title('{} Confusion Matrix with Labels'.format(name))
        plt.rcParams['font.size'] = '10'
        plt.grid(None)
        return plt.show()
        