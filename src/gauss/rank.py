import numpy as np
import gauss

def rank(matrix: np.ndarray | list[list[float]]) -> int:
    """
    Returns the rank of a matrix
    """

    U = gauss.rref(matrix)
    rank = 0

    for row in U:
        if not all(np.allclose(x, 0) for x in row):
            rank += 1

    return rank
