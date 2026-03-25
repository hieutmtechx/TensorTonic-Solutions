import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    pass

    n = len(x)
    percentiles = []
    x = np.sort(np.asarray(x))

    for _ in range(len(q)):
        L = (n - 1) * q[_] / 100

        if (L > n):
            percentiles.append(x[n - 1])
            continue

        if (L == 0):
            percentiles.append(x[0])
            continue
        
        loL = int(np.floor(L))
        hiL = int(np.ceil(L))

        if (loL == hiL):
            percentiles.append(x[loL])
        else:
            percentiles.append(x[loL] + (L - loL) * (x[hiL] - x[loL]))

        print(L, loL, hiL)

    print(percentiles)
    return np.asarray(percentiles)
    

percentiles([4,1,3,2], [0, 100])