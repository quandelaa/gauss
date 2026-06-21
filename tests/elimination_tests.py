import numpy as np
from gauss import ref

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

def test_ref():
    assert ref_test() == 10
