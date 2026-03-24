import numpy as np
import math
from collections import defaultdict
def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    pass

    instance_count = len(y)

    if (instance_count == 0): return 0.0
    
    classes = defaultdict(int)

    for _ in range(instance_count):
        classes[y[_]] += 1

    entrophy = 0
    for className, classPortion in classes.items():
        classProb = classPortion / instance_count
        entrophy = entrophy - (classProb * math.log2(classProb))

    # print(entrophy)
    return entrophy
    