import numpy as np
from collections import Counter

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    pass

    tokenCount = Counter(tokens)
    bow = []
    for x in vocab:
        bow.append(tokenCount[x])

    return np.asarray(bow, dtype = int)