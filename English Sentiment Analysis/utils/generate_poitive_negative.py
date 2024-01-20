def false_true_positive(Confusin_Matrix):
        False_Postive = Confusin_Matrix[0][1]
        True_Positive = Confusin_Matrix[0][0]
        return False_Postive, True_Positive


def false_true_negative(Confusin_Matrix):
        False_Negative = Confusin_Matrix[1][0]
        True_Negative = Confusin_Matrix[1][1]
        return False_Negative, True_Negative
