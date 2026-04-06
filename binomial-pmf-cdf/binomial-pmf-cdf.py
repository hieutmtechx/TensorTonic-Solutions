import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pass

    pmf = comb(n, k) * np.power(p, k) * np.power(1 - p, n - k)

    i = np.arange(k + 1)
    cdf = np.sum(comb(n, i) * np.power(p, i) * np.power(1 - p, n - i))

    return (pmf, cdf)
