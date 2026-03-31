import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    pass

    y_true = np.asarray(y_true, dtype = float)
    y_pred = np.asarray(y_pred, dtype = float)

    y_mean = np.mean(y_true)

    r_square = np.sum((y_true - y_mean)**2)

    if (r_square == 0): return 1.0 if (np.all(y_true == y_pred)) else 0.0
        
    r_square = np.sum((y_true - y_pred)**2) / r_square
    r_square = 1 - r_square

    return r_square
