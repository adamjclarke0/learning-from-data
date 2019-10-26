import numpy as np

def generate_target_function(a, b):
    """ Given two points a, b in X = [-1, 1]^2,
    this defines a line in X passing through a and b.
    We return the function f where f(x) = 1 if x is
    "above" the line and -1 if x is "below" the line.
    """
    q = b[0] - a[0]
    r = (b[1] - a[1])
    s = ((a[1] * b[0]) - (a[0] * b[1]))
    def f(x):
        if q * x[1] > (r * x[0]) + s:
            return 1
        else:
            return -1
    return f

def generate_training_data(f, n):
    """ Generates n training data points [x, y] for the given target function f,
    where x = [x1, x2] is a random point in X = [-1, 1]^2 and y = f(x).
    """
    X = 2 * np.random.random((n, 2)) - 1
    Y = np.apply_along_axis(f, axis=1, arr=X)
    return X, Y
