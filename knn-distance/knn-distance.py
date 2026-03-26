import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    # Write code here
    pass

    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)

    if (np.ndim(X_train) == 1): X_train = X_train.reshape(-1, 1)
    if (np.ndim(X_test) == 1): X_test = X_test.reshape(-1, 1)
    
    
    X_train_sq = np.sum(X_train**2, axis = 1)
    X_test_sq = np.sum(X_test**2, axis = 1)

    print(X_train_sq)

    dis = X_test_sq[:,None] + X_train_sq[None,:] - 2 * X_test @ X_train.T
    dis = np.sqrt(np.maximum(dis, 0))
    print(dis)
    idx = np.argsort(dis, axis = 1)[:, :k]

    
    if (k > len(X_train)): 
        complement = np.full((len(X_test), k - len(X_train)), -1, dtype = int)
        complement = complement.reshape(1, -1)
        idx = np.concatenate([idx, complement], axis = 1)
    
    return idx

# knn_distance()
