import numpy as np 

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here

    x = np.asarray(x, dtype = float)

    _x = []
    for i in x:
        _x.append(i if (i > 0) else alpha * (np.exp(i) - 1))

    return _x
