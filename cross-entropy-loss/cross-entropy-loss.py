import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    pass

    ce = 0
    N = len(y_true)
    y_pred = np.asarray(y_pred, dtype = float)
    for i, label in enumerate(y_true):
        ce += (-np.log(y_pred[i, label]))
    ce /= N

    return ce
    