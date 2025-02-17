import numpy as np
from sigmoid import sigmoid
from sigmoidGradient import sigmoidGradient
def nnCostFunction(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, lbd):

    """
    NNCOSTFUNCTION Implements the neural network cost function for a two layer
    %neural network which performs classification
    %   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
    %   X, y, lambda) computes the cost and gradient of the neural network. The
    %   parameters for the neural network are "unrolled" into the vector
    %   nn_params and need to be converted back into the weight matrices. 
    % 
    %   The returned parameter grad should be a "unrolled" vector of the
    %   partial derivatives of the neural network.
    %

    Args
    nn_params          : numpy array (unrolled)
    input_layer_size   : integer, size of input layer
    hidden_layer_size  : integer, size of hiddenlayer
    num_labels         : integer, number of labels
    X                  : numpy array, input
    y                  : numpy array, output (haven't one hot encoded yet)
    lbd                : scalar for regularization

    Return
    J                  : value of cost function
    Grad               : gradient descent

    """
    #  Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
    #  for our 2 layer neural network
    Theta1 = nn_params[0: hidden_layer_size*(input_layer_size+1)].reshape(hidden_layer_size, input_layer_size + 1) #25x401

    Theta2 = nn_params[Theta1.shape[0]*Theta1.shape[1]:].reshape(num_labels, hidden_layer_size + 1) #10x26

    # Setup some useful variables
    m = X.shape[0] # 5000

    # You need to return the following variables correctly 
    J = 0
    Theta1_grad = np.zeros(Theta1.shape) # 25x401
    Theta2_grad = np.zeros(Theta2.shape) # 10x26

    #  ====================== YOUR CODE HERE ======================
    #  Instructions: You should complete the code by working through the
    #                following parts.
    # 
    #  Part 1: Feedforward the neural network and return the cost in the
    #          variable J. After implementing Part 1, you can verify that your
    #          cost function computation is correct by verifying the cost
    #          computed in ex4.m

    a1 = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1) #add bias 1 -> 5000x401
    z2 = a1.dot(Theta1.T) # 5000x25
    a2 = sigmoid(z2)
    a2 = np.concatenate((np.ones((a2.shape[0], 1)), a2), axis=1) #add bias 1 -> 5000x26
    z3 = a2.dot(Theta2.T) # 5000x10
    a3 = sigmoid(z3)

    h_x = a3 #5000x10
    
    reg = lbd/(2*m)* (sum(sum(Theta1[:, 1:]**2)) + sum(sum(Theta2[:, 1:]**2)))
    # one hot encode y
    origin_labels = y

    encoded_y = np.zeros((y.shape[0],num_labels)) # 5000x10

    for i in range(y.shape[0]):
        encoded_y[i, origin_labels[i]-1] = 1


    J = (-1/m)* sum(sum(encoded_y*np.log(h_x) + (1-encoded_y)*np.log(1- h_x))) + reg

    #  Part 2: Implement the backpropagation algorithm to compute the gradients
    #          Theta1_grad and Theta2_grad. You should return the partial derivatives of
    #          the cost function with respect to Theta1 and Theta2 in Theta1_grad and
    #          Theta2_grad, respectively. After implementing Part 2, you can check
    #          that your implementation is correct by running checkNNGradients
    # 
    #          Note: The vector y passed into the function is a vector of labels
    #                containing values from 1..K. You need to map this vector into a 
    #                binary vector of 1's and 0's to be used with the neural network
    #                cost function.
    # 
    #          Hint: We recommend implementing backpropagation using a for-loop
    #                over the training examples if you are implementing it for the 
    #                first time.

    delta3 = a3 - encoded_y # 5000x10
    delta2 = delta3.dot(Theta2[:, 1:]) * sigmoidGradient(z2) #5000x25

    Theta1_grad = (1/m) * delta2.T.dot(a1)
    Theta2_grad = (1/m) * delta3.T.dot(a2)
    
    #  Part 3: Implement regularization with the cost function and gradients.
    # 
    #          Hint: You can implement this around the code for
    #                backpropagation. That is, you can compute the gradients for
    #                the regularization separately and then add them to Theta1_grad
    #                and Theta2_grad from Part 2.
    
    # Calculating gradients for the regularization
    Theta1 = np.concatenate((np.zeros((Theta1.shape[0], 1)), Theta1[:, 1:]), axis=1)
    Theta1_grad_reg_term = (lbd/m) * Theta1
    Theta2 = np.concatenate((np.zeros((Theta2.shape[0], 1)), Theta2[:, 1:]), axis=1)
    Theta2_grad_reg_term = (lbd/m) * Theta2

    # Adding regularization term to earlier calculated Theta_grad
    Theta1_grad = Theta1_grad + Theta1_grad_reg_term
    Theta2_grad = Theta2_grad + Theta2_grad_reg_term

    grad = np.concatenate((Theta1_grad.ravel(), Theta2_grad.ravel()))
    return J, grad


