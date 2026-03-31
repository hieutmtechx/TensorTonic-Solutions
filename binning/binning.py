import numpy as np 
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here

    max_val = np.max(values) 
    min_val = np.min(values)
    w = (max_val - min_val) / num_bins

    if (min_val == max_val):
        return [0 for i in range(len(values))]

    bins = []
    for value in values:
        bin = min(np.floor((value - min_val) / w), num_bins - 1)
        bins.append(bin)
    
    return bins

binning([5, 5, 5], 3)