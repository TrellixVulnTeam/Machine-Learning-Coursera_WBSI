function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1)); % 25x401

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1)); % 10x26

% Setup some useful variables
m = size(X, 1); % 5000
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1)); % 25x401
Theta2_grad = zeros(size(Theta2)); % 10x26

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

% Part 1:
a1 = [ones(rows(X), 1) X]; % add bias 1 -> 5000 x401
z2 = a1*Theta1'; % 5000 x25
a2 = sigmoid(z2);
a2 = [ones(rows(a2), 1) a2]; % add bias 1 -> 5000 x26
z3 = a2*Theta2'; % 5000 x 10
a3 = sigmoid(z3);
h_x = a3; % 5000 x 10
onehot_y=  y == 1:max(y); #one hot encode shape 5000x10

reg = lambda/(2*m)*(sum(sum(Theta1(:, 2:end).^2)) + sum(sum(Theta2(:, 2:end).^2))); % regularization

J = (-1/m)*sum(sum((onehot_y.*log(h_x)) + ((1-onehot_y).*log(1 - h_x)))) + reg; %scalar

% Part 2:
delta3 = a3 - onehot_y; % 5000 x 10
delta2 = delta3*Theta2(:,2:end) .* sigmoidGradient(z2); % 5000 x 25
%delta2 = delta3*Theta2(:,:25) .*[ones(rows(sigmoidGradient(z2)), 1) sigmoidGradient(z2)]; % 5000 x 26
%delta2 = delta2(:, 2:end); % 5000x25 remove delta2 for bias 1

Theta1_grad = (1/m) * (delta2' * a1); % 25 x 401
Theta2_grad = (1/m) * (delta3' * a2); % 10 x 26

% Part 3:
%Calculating gradients for the regularization
Theta1_grad_reg_term = (lambda/m) * [zeros(size(Theta1, 1), 1) Theta1(:,2:end)]; % 25 x 401
Theta2_grad_reg_term = (lambda/m) * [zeros(size(Theta2, 1), 1) Theta2(:,2:end)]; % 10 x 26

%Adding regularization term to earlier calculated Theta_grad
Theta1_grad = Theta1_grad + Theta1_grad_reg_term;
Theta2_grad = Theta2_grad + Theta2_grad_reg_term;
















% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
