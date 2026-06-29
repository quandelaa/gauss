from gauss import rref
import numpy as np

def is_invertible(matrix: np.ndarray | list[list[float]]) -> bool:
    """
    Returns whether a matrix is invertible or not
    """
    
    A = np.array(matrix)
    rows, cols = A.shape

    if not rows == cols:
        return False

    raw_I = np.eye(rows)

    I = np.array(raw_I)

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
