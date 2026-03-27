import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    pass

    x = np.asarray(x)
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))