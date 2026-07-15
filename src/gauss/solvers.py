import gauss
import numpy as np

def inverse(matrix: np.ndarray | list[list[float]]) -> np.ndarray:
    """
    Returns the inverse of a square matrix
    """
    
    A = np.array(matrix, float)
    rows, _ = A.shape

    if gauss.utils.is_invertible(A) is False:
        raise gauss.NonInvertibleError(f"A is a non-invertible matrix. Cannot get the inverse of A because A is invertible")

    I = np.eye(rows)

    raw_aug = gauss.gauss_jordan(A, I)
    inverse_matrix = raw_aug[:, rows:]

    return inverse_matrix
