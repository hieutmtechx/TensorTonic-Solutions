import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    pass

    v = np.asarray(v)

    if (v.ndim == 1):
        norm_v = np.linalg.norm(v)
        if (norm_v < 10**(-10)): 
            return v
        else: 
            return v / norm_v
    else:
        norm_v = np.linalg.norm(v, axis = 1, keepdims = True) 
        norm_v[norm_v < 1e-10] = 1
        return v / norm_v
    
