import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    pass

    max_length = 0
    for seq in seqs: 
        max_length = max(max_length, len(seq))

    max_length = max_len if (max_len is not None) else max_length
    padded_seqs = []
    for seq in seqs:
        current_seq = []
        for i in range(max_length):
            if (i < len(seq)):
                current_seq.append(seq[i])
            else:
                current_seq.append(pad_value)
        padded_seqs.append(current_seq)
    
    return np.asarray(padded_seqs)