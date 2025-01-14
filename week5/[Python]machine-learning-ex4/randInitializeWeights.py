import numpy as np
def randInitializeWeights(L_in, L_out):
    """
    RANDINITIALIZEWEIGHTS Randomly initialize the weights of a layer with L_in
    incoming connections and L_out outgoing connections
       W = RANDINITIALIZEWEIGHTS(L_in, L_out) randomly initializes the weights 
       of a layer with L_in incoming connections and L_out outgoing 
       connections. 
    
       Note that W should be set to a matrix of size(L_out, 1 + L_in) as
       the first column of W handles the "bias" terms

    Args
    L_in: incoming connections (số node input)
    L_out: incomming connections (số node output)

    Return: weights matrix (numpy array)
    """
    # You need to return the following variables correctly 
    # W = zeros(L_out, 1 + L_in);

    W = np.zeros((L_out, 1 + L_in))

    #  ====================== YOUR CODE HERE ======================
    #  Instructions: Initialize W randomly so that we break the symmetry while
    #                training the neural network.
    # 
    #  Note: The first column of W corresponds to the parameters for the bias unit
    # 

    # Randomly initialize the weights to small values
    epsilon_init = 0.12
    W = np.random.rand(L_out, 1 + L_in)*(2*epsilon_init) - epsilon_init

    return W

