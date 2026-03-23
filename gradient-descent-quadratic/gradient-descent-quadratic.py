
def func(a, b, c, x):
    return (a * x * x + b * x + c)

def derivate(a, b, c, x):
    return (2 * a * x + b)

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    pass

    x = x0
    while (steps > 0):

        nx = x - lr * derivate(a, b, c, x)

        x = nx
        steps -= 1
        
    return x