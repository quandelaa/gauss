from gauss import rref
import numpy as np

def is_invertible(matrix: np.ndarray | list[list[float]]):
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
    if np.allclose(R, I, atol=1e-12) is False:
        return False

    return True
