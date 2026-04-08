import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    pass

    N = len(seqs)

    if (N == 0):
        L = max_len if max_len is not None else 0
        return np.empty((0, L)) 

    L = 0
    for seq in seqs: 
        L = max(L, len(seq))
    L = max_len if (max_len is not None) else L

    padded_seqs = np.full((N, L), pad_value)
    for i, seq in enumerate(seqs):
        truncated_seq = seq[:L]
        padded_seqs[i, :len(truncated_seq)] = truncated_seq
    
    return np.asarray(padded_seqs)