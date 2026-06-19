import numpy as np

def ref(matrix: list):
    """
    Returns the row-echelon-form of a matrix
    """

    try:
        A = np.array(matrix, float)
    except Exception as e:
        return e

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
