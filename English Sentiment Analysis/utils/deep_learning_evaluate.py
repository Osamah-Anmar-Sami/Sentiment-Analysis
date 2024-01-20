def deep_learning_evaluate_(model, x, y, train_test):
           loss, accuracy = model.evaluate(x, y, verbose=False)
           print(" ")
           print('The Evaluation Of {} Is {:.4f} For Loss And {:.4f} For Accuracy'.format(train_test, loss,  accuracy))
