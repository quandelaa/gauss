import numpy as np
import gauss

def lu(matrix: np.ndarray | list[list[float]]) -> np.ndarray:
    """
    Returns the LU decomposition of a matrix
    """

    A = np.array(matrix)
    rows, cols = A.shape

    # SHITTTT
