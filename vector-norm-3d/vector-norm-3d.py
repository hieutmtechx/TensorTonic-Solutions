import numpy as np
import math
def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    pass

    v = np.asarray(v)
    norm = math.sqrt(np.sum(v**2)) if (v.ndim == 1) else np.sqrt(np.sum(v**2, axis = 1))
    return norm