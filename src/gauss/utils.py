from gauss import rref
import numpy as np

def is_invertible(matrix: np.ndarray | list[list[float]]) -> bool:
    """
    Returns whether a matrix is invertible or not
    """
    
    A = np.array(matrix)
    rows, cols = A.shape

    if rows != cols:
        return False

    I = np.eye(rows)
    R = rref(A)

    return(np.allclose(R, I))

def is_square(matrix: np.ndarray | list[list[float]]) -> bool:
    """
    Returns whether a matrix is square or not
    """

    A = np.array(matrix)
    rows, cols = A.shape

    if rows == cols:
        return True

    return False

