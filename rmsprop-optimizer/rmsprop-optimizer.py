import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    pass

    s = np.asarray(s, dtype = float)
    w = np.asarray(w, dtype = float)
    g = np.asarray(g, dtype = float)

    s = beta * s + (1.0 - beta) * g * g
    w = w - lr / (np.sqrt(s + eps)) * g

    return (w, s)