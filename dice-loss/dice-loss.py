import numpy as np

def dice_loss(p, y, eps = 1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    pass

    p = np.asarray(p, dtype = float)
    y = np.asarray(y, dtype = float)

    dice = 0
    dice = 2 * np.sum(p * y) + eps 
    dice = dice / (np.sum(p) + np.sum(y) + eps)

    return (1 - dice)
