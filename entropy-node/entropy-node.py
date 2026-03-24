import numpy as np
import math
from collections import defaultdict
def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    pass

    instances= len(y)
    if (instances == 0): return 0.0

    unique, counts = np.unique(y, return_counts = True)
    probs = counts / instances
    
    # print(entrophy)
    return -np.sum(probs * np.log2(probs))
    