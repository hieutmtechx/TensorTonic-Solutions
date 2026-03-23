import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    pass

    np_x = np.asarray(x, dtype = float)

    return (np.ones(1) / (np.ones(1) + np.exp(-np_x)))



def main():
    # Main logic of your program goes here
    print(sigmoid([[-1, 0], [1, 2]]))

if __name__ == "__main__":
    main()

    