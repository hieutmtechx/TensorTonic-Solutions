import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    pass

    exp = 0
    prob_sum = 0
    for i in range(len(x)):
        exp += x[i] * p[i]
        prob_sum += p[i]
    if (prob_sum != 1): raise ValueError("Invalid")
    return exp
    