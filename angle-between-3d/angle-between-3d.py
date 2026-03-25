import numpy as np
import math

def norm(a):
    return np.sqrt(np.sum(a**2)) if (a.ndim == 1) else np.sqrt(np.sum(a**2, axis = 1))

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    pass

    v = np.asarray(v)
    w = np.asarray(w)

    cosPhi = np.dot(v, w) / (norm(v) * norm(w))
    return np.acos(cosPhi)