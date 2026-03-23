
def func(a, b, c, x):
    return (a * x * x + b * x + c)

def derivate(a, b, c, x):
    return (2 * a * x + b)

def gradient_descent_quadratic(a, b, c, x0, lr0, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    pass

    x = x0
    lr = lr0
    for i in range(steps):

        nx = x - lr * derivate(a, b, c, x)

        lr = lr0 / (1 + (i / 50))
        x = nx
        
    return x