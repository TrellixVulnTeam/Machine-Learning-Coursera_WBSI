from trainLinearReg import trainLinearReg
from linearRegCostFunction import linearRegCostFunction
import numpy as np
def validationCurve(X, y, Xval, yval):
    """
    VALIDATIONCURVE Generate the train and validation errors needed to
    plot a validation curve that we can use to select lambda
    [lambda_vec, error_train, error_val] = ...
    VALIDATIONCURVE(X, y, Xval, yval) returns the train
    and validation errors (in error_train, error_val)
    for different values of lambda. You are given the training set (X,
    y) and validation set (Xval, yval).

    Args
    X: numpy array (X train)
    y: numpy array (y train)
    Xval: numpy array (X validation)
    yval: numpy array (y validation)

    Return
    lambda_vec: numpy array (selected values of lambda)
    error_train: numpy array (train errors)
    error_val: numpy array (val errors)
    """
    # Selected values of lambda (you should not change this)
    lambda_vec = np.array([0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10])
    # You need to return these variables correctly.
    error_train = np.zeros((len(lambda_vec), 1))
    error_val = np.zeros((len(lambda_vec), 1))
    
    #      ====================== YOUR CODE HERE ======================
    #  Instructions: Fill in this function to return training errors in 
    #                error_train and the validation errors in error_val. The 
    #                vector lambda_vec contains the different lambda parameters 
    #                to use for each calculation of the errors, i.e, 
    #                error_train(i), and error_val(i) should give 
    #                you the errors obtained after training with 
    #                lambda = lambda_vec(i)
    for i in range(len(lambda_vec)):
        lbd = lambda_vec[i]
        
        theta = trainLinearReg(X, y, lbd)
        
        error_train[i] = linearRegCostFunction(X, y, theta, 0)[0] # lambda = 0
        error_val[i] = linearRegCostFunction(Xval, yval, theta, 0)[0] # lambda = 0
    
    return lambda_vec, error_train, error_val