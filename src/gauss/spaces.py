import numpy as np
import gauss

def column_space(matrix: np.ndarray | list[list[float]]) -> np.ndarray:
    """
    Returns basis vectors of the column space of the matrix
    """

    A = np.array(matrix, float)
    rows, cols = A.shape
    
def row_space(matrix: np.ndarray | list[list[float]]) -> np.ndarray:
    """
    Returns basis vectors of the row space of the matrix
    """

    A = np.array(matrix, float)
    rows, cols = A.shape
