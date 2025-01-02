def machine_learning_model(algorithm):       
        """
        Initializes and returns a machine learning model using the specified algorithm.

        Args:
                algorithm: A machine learning algorithm or model instance to be used.

        Returns:
                The initialized machine learning model.
        """
        model = algorithm
        return model
        
def fit_model(model, X_train, y_train):
        """
        Fits the given machine learning model to the training data.

        Parameters:
        model (object): The machine learning model to be trained.
        X_train (array-like or DataFrame): The training input samples.
        y_train (array-like or Series): The target values (class labels) for the training input samples.

        Returns:
        object: The trained machine learning model.
        """
        model.fit(X_train, y_train)
        return model
        