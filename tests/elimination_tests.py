import numpy as np
from gauss import rref, ref

def ref_test():
    A_matrices = [
        [[1, 2],
         [3, 4]],

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],

        [[1, 2, 3],
         [4, 5, 6]],

        [[1, 1],
         [2, 2],
         [3, 3]],

        [[0, 2],
         [3, 4]],

        [[0, 1, 2],
         [1, 0, 3],
         [2, 3, 1]],

        [[0, 1, 2, 3],
         [0, 4, 5, 6],
         [0, 7, 8, 9],
         [0, 10, 11, 12]],

        [[1, 2, 1],
         [2, 4, 3],
         [3, 6, 4]],

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]],

        [[1, 1, 1],
         [1, 2, 3],
         [1, 3, 6]]
    ]

    REF_matrices = [
        [[1, 2],
         [0, -2]],

        [[1, 2, 3],
         [0, -3, -6],
         [0, 0, 0]],

        [[1, 2, 3],
         [0, -3, -6]],

        [[1, 1],
         [0, 0],
         [0, 0]],

        [[3, 4],
         [0, 2]],

        [[1, 0, 3],
         [0, 1, 2],
         [0, 0, -11]],

        [[0, 1, 2, 3],
         [0, 0, -3, -6],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[1, 2, 1],
         [0, 0, 1],
         [0, 0, 0]],

        [[1, 2, 3],
         [0, -3, -6],
         [0, 0, 0],
         [0, 0, 0]],

        [[1, 1, 1],
         [0, 1, 2],
         [0, 0, 1]]
    ]

    successes = 0

    for (A, ref_expected) in zip(A_matrices, REF_matrices):
        ref_expected_np = np.array(ref_expected, dtype=float)
        ref_computed = ref(A)

        if np.allclose(ref_computed, ref_expected_np, atol=1e-12) is True:
            successes += 1

    return successes

def rref_test():
    A_matrices = [
        [[0, 0, 0],
         [0, 0, 0]],

        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]],

        [[0, 1],
         [1, 0]],

        [[1, 2, 3],
         [4, 5, 6]],

        [[2, 4],
         [3, 6]],

        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]],

        [[1, 2, 3],
         [2, 4, 6]],

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]],

        [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15]]
    ]

    RREF_matrices = [
        [[0, 0, 0],
         [0, 0, 0]],

        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]],

        [[1, 0],
         [0, 1]],

        [[1, 0, -1],
         [0, 1,  2]],

        [[1, 2],
         [0, 0]],

        [[1, 0, -1, -2],
         [0, 1,  2,  3],
         [0, 0,  0,  0]],

        [[1, 2, 3],
         [0, 0, 0]],

        [[1, 0, -1],
         [0, 1,  2],
         [0, 0,  0]],

        [[1, 0, -1],
         [0, 1,  2],
         [0, 0,  0],
         [0, 0,  0]],

        [[1, 0, -1, -2, -3],
         [0, 1,  2,  3,  4],
         [0, 0,  0,  0,  0]]
    ]

    successes = 0

    for (A, rref_expected) in zip(A_matrices, RREF_matrices):
        rref_expected_np = np.array(rref_expected, dtype=float)
        rref_computed = rref(A)

        if np.allclose(rref_computed, rref_expected_np, atol=1e-12) is True:
            successes += 1

    return successes
            
def test_ref():
    assert ref_test() == 10

def test_rref():
    assert rref_test() == 10
