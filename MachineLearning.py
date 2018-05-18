import numpy as np
import tensorflow as tf

np.random.seed(1)


def placeholders(numInp, numLabel):
    """
    Creates the placeholders for the input and label
    
    """
    inp = tf.placeholder(tf.float32, shape = [numInp, None], name = 'inp')
    label = tf.placeholder(tf.float32, shape = [numLabel, None], name = 'label')
    
    return inp, label

def initializeParameters():
    
    tf.set_random_seed(1)                   # so that your "random" numbers match ours
        
    Weight1 = tf.get_variable("Weight1", [100,64], initializer = tf.contrib.layers.xavier_initializer(seed = 1))
    bias1 = tf.get_variable("bias1", [100,1], initializer = tf.zeros_initializer())
    Weight2 = tf.get_variable("Weight2", [100,100], initializer = tf.contrib.layers.xavier_initializer(seed = 1))
    bias2 = tf.get_variable("bias2", [100,1], initializer = tf.zeros_initializer())
    Weight3 = tf.get_variable("Weight3", [100,100], initializer = tf.contrib.layers.xavier_initializer(seed = 1))
    bias3 = tf.get_variable("bias3", [100,1], initializer = tf.zeros_initializer())
    Weight4 = tf.get_variable("Weight4", [1,100], initializer = tf.contrib.layers.xavier_initializer(seed = 1))
    bias4 = tf.get_variable("bias4", [1,1], initializer = tf.zeros_initializer())

    parameters = {"Weight1": Weight1,
                  "bias1": bias1,
                  "Weight2": Weight2,
                  "bias2": bias2,
                  "Weight3": Weight3,
                  "bias3": bias3,
                  "Weight4": Weight4,
                  "bias4": bias4}
    
    return parameters

def network(inp, parameters):
    """
    Implements the neural network
    
    Inputs: inp(input data), parameters(weights and biases)
    
    Outputs: out(network output)
    """
    
    Weight1 = parameters['Weight1']
    bias1 = parameters['bias1']
    Weight2 = parameters['Weight2']
    bias2 = parameters['bias2']
    Weight3 = parameters['Weight3']
    bias3 = parameters['bias3']
    Weight4 = parameters['Weight4']
    bias4 = parameters['bias4']
    
    hiddenOut1 = tf.add(tf.matmul(Weight1, inp), bias1)       
    rel1 = tf.nn.relu(hiddenOut1)                            
    hiddenOut2 = tf.add(tf.matmul(Weight2, rel1), bias2)                
    rel2 = tf.nn.relu(hiddenOut2) 
    hiddenOut3 = tf.add(tf.matmul(Weight3, rel2), bias3)                
    rel3 = tf.nn.relu(hiddenOut3)                        
    out = tf.add(tf.matmul(Weight4, rel3), bias4)    
    
    return out


def compute_cost(out, label):
    
    cost = tf.reduce_mean(tf.squared_difference(out, label))
    
    return cost

