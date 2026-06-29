import numpy as np
import gauss

def lu_test():
    A_matrices = []

    for _ in range(50):
        current = np.random.randint(1, 10)

        A = np.random.randint(0, 9, (current, current))
        A_matrices.append(A)

    corrects = 0

    for A in A_matrices:
        P, L, U = gauss.lu(A)

        PA = P@A
        LU = L@U

        if np.allclose(PA, LU) is True:
            corrects += 1

    return corrects

def test_lu():
    assert lu_test() >= 40
