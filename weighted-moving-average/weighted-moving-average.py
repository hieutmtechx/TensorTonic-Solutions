import numpy as np
def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here

    n = len(values)
    k = len(weights)

    wma = []

    W = np.sum(np.asarray(weights))
    for i in range(n - k + 1):
        x = 0
        for j in range(k):
            x += weights[j] * values[i + j]
        x /= W
        wma.append(x)

    return wma