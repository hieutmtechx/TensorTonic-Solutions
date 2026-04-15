import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    pass

    # y_true = np.asarray(y_true, dtype = float)
    y_pred = np.asarray(y_pred, dtype = float)

    N = y_pred.shape[0]

    probs = y_pred[np.arange(N), y_true]
    ce = -np.mean(np.log(probs))
    
    return ce
    