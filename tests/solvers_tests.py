import numpy as np
from gauss import inverse

def inverse_test():
    test_matrices = [
        [[2, 1],
         [1, 1]],
        
        [[4, 7],
        [2, 6]],

        [[2, 3],
         [5, 7]],

        [[5, 2],
         [2, 1]],

        [[1, 2, 3],
         [0, 1, 4],
         [5, 6, 0]],
        
        [[3, 1, 1],
         [2, 2, 5],
         [1, 3, 4]],

        [[1, 1, 0],
         [0, 1, 1],
         [1, 0, 1]],

        [[1, -2, 3],
         [4, 0, -1],
         [2, 3, -4]],
        
        [[0, 1, 2],
         [1, 0, 3],
         [4, 5, 6]],

        [[1, 2, 3],
         [0, 4, 5],
         [0, 0, 6]],

        [[7, 0, 0],
         [8, 9, 0],
         [1, 2, 3]
        ],

        [[1, 2, 1],
         [2, 1, 3],
         [1, 4, 5]],
        
        [[1, 2, 1],
         [1, 1, 3],
         [1, 10, 5]],

        [[10, 20, 30],
         [20, 50, 70],
         [30, 70, 110]],

        [[1, 0.5, 1/3],
         [0.5, 1/3, 0.25],
         [1/3, 0.25, 0.2]],

        [[2, 0, 0, 0],
         [0, 3, 0, 0],
         [0, 0, 4, 0],
         [0, 0, 0, 5]]
    ]

    corrects = 0

    for matrix in test_matrices:
        inv = inverse(matrix)
        arr = np.array(matrix)

        check = arr@inv
        
        if np.allclose(check, np.eye(arr.shape[0])):
            corrects += 1

    return corrects

def test_inverse():
    assert inverse_test() == 16
