def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here

    diff = []
    for d in range(order):
        for i in range(1, len(series)):
            diff.append(series[i] - series[i - 1]) 
            print(i, i - 1)
        series = diff.copy()
        diff.clear()
    
    return series