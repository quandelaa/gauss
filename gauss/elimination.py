import gauss
import numpy as np

def gauss_jordan(A: np.ndarray | list[list[float]], B: np.ndarray | list[list[float]]):
    """
    Returns the row-reduced-echelon form of augmented matrix A|B 
    """

    A = np.array(A)
    B = np.array(B)

    A_rows, A_cols = A.shape
    B_rows, _ = B.shape

    if B_rows != A_cols:
        raise gauss.DimensionMismatchError(f"A has {A_cols} columns while B has {A_rows} rows. Cannot solve Ax = B because B needs to be in the column space of A")

    aug = np.hstack([A, B])
    R = gauss.rref(aug)

    return R
    
def rref(matrix: np.ndarray | list[list[float]]) -> np.ndarray:
    """
    Returns the row-reduced-echelon form of a matrix
    """

    A = np.array(matrix)
    B = gauss.ref(A)
    
    rows, cols = B.shape
    col_pivot = cols-1

    for i in range(rows):
        for j in range(cols):
            if abs(B[i][j]) > 1e-12:
                col_pivot = j

                divider = B[i][j]

                new_row = B[i] / divider
                B[i] = new_row
                break

    for i in range(rows-1, 0, -1):
        next_row = i-1

        if B[i, col_pivot] == 0:
            if all(x == 0 for x in B[i]):
                continue

            had_change = False

            for piv in range(col_pivot, -1, -1):
                for piv_ in range(i, -1, -1):
                    if abs(B[piv_][col_pivot]) > 1e-12:
                        B[[piv_, i]] = B[[i, piv_]]
                        had_change = True
                        break

                if abs(B[i][piv]) > 1e-12:
                    col_pivot = piv
                    had_change = True
                    break

            if not had_change:
                return B

        for j in range(next_row, -1, -1):
            if j < 0:
                break

            multiplier = B[j][col_pivot] / B[i][col_pivot]

            new_row = B[j] - (B[i] * multiplier)
            B[j] = new_row

        col_pivot -= 1

    return B

def ref(matrix: np.ndarray | list[list[float]]) -> np.ndarray:
    """
    Returns the row-echelon form of a matrix (pivots aren't normalized)
    """

    A = np.array(matrix, float)

    rows, cols = A.shape
    col_pivot = 0
    
    for i in range(rows):
        next_row = i+1

        if next_row > rows-1 or col_pivot > cols-1:
            return A

        if A[i][col_pivot] == 0: 
            had_change = False

            for piv in range(col_pivot, cols):
                for piv_ in range(i, rows):
                    if abs(A[piv_][col_pivot]) > 1e-12:
                        A[[piv_, i]] = A[[i, piv_]]
                        had_change = True
                        break

                if abs(A[i][piv]) > 1e-12:
                    col_pivot = piv
                    had_change = True
                    break

            if not had_change:
                return A

        for j in range(next_row, rows):
            multiplier = A[j][col_pivot] / A[i][col_pivot]

            new_row = A[j] - (A[i] * multiplier)
            A[j] = new_row

        col_pivot += 1
