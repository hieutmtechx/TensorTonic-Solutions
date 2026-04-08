import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    pass

    X = np.asarray(X)
    y = np.asarray(y)
    n, d = X.shape
    w = np.zeros(d)
    b = 0.0

    for _ in range(steps):
        p = _sigmoid(np.dot(X, w) + b)
        dL_w = (1 / n) * np.dot(X.T, (p - y))
        dL_b = (1 / n) * (np.sum(p - y))

        w = w - lr * dL_w
        b = b - lr * dL_b    

    return (list(w), float(b))

