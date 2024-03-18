def machine_learning_model(algorithm):
        """
                this function simply returns the provided algorithm as-is

                Args:
                        algorithm (object): any object representing a machine learning model

                Returns:
                        object: the input algorithm object
                """
        model = algorithm
        return model
        
def fit_model(model, X_train, y_train):
        """
                fits (trains) a provided machine learning model on the given training data

        Args:
                model (object): the machine learning model to be trained. It should have a `fit` method that takes training data features and labels as arguments.
                X_train (np.ndarray): training data features
                y_train (np.ndarray): training data labels

        Returns:
                object: The trained model object.
        """
        model.fit(X_train, y_train)
        return model
        