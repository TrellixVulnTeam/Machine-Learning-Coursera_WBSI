from numpy import exp
def sigmoid(z):
    """
    SIGMOID Compute sigmoid functoon
    J = SIGMOID(z) computes the sigmoid of z.
    """

    return 1.0/(1.0 + exp(-z))
