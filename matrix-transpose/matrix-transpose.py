import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    pass

    row = len(A)
    col = len(A[0])

    AT = [[0 for _ in range(row)] for _ in range(col)] 

    for i in range(row):
        for j in range(col):
            AT[j][i] = A[i][j]
    
    return np.asarray(AT)

def main():
    print(matrix_transpose([[1,2,3],[4,5,6]]))
    
if __name__ == "__main__":
    main()