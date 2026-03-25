import numpy as np
from collections import Counter

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    pass

    rater1 = np.asarray(rater1)
    rater2 = np.asarray(rater2)

    counter1 = Counter(rater1)
    counter2 = Counter(rater2)

    n = len(rater1)

    pO = np.sum(rater1 == rater2) / n
    pE = sum(counter1[x] / n * counter2[x] / n for x in counter1.keys() & counter2.keys())

    if (pE == 1): return 1
    kappa = (pO - pE) / (1 - pE)
    return kappa


print(cohens_kappa([0, 0, 1, 1], [0, 1, 1, 0]))