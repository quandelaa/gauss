import numpy as np
import gauss

def lu(matrix: np.ndarray | list[list[float]]) -> np.ndarray:
    """
    Returns P, L, U of PA = LU
    """

    A = np.array(matrix, float)
    rows, cols = A.shape

    if rows != cols:
        raise gauss.NotSquareError(f"A has {rows} rows and {cols} columns. Cannot get the LU decomposition of A because A needs to be square")

    L = np.eye(rows)
    P = np.eye(cols)

    col_pivot = 0
    
    for i in range(rows):
        next_row = i+1

        if next_row > rows-1 or col_pivot > cols-1:
            return P, L, A

        if A[i][col_pivot] == 0: 
            had_change = False

            for piv in range(col_pivot, cols):
                for piv_ in range(i, rows):
                    if abs(A[piv_][col_pivot]) > 1e-12:
                        A[[piv_, i]] = A[[i, piv_]]
                        P[[piv_, i]] = P[[i, piv_]]
                        had_change = True
                        break

                if abs(A[i][piv]) > 1e-12:
                    col_pivot = piv
                    had_change = True
                    break

            if not had_change:
                return P, L, A

        for j in range(next_row, rows):
            multiplier = A[j][col_pivot] / A[i][col_pivot]

            L[j][i] = multiplier 

            new_row = A[j] - (A[i] * multiplier)
            A[j] = new_row

        col_pivot += 1
