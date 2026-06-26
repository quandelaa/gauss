"""
Gauss - a linear algebra library
"""

from gauss.elimination import ref
from gauss.elimination import rref
from gauss.solvers import inverse
from gauss.elimination import gauss_jordan
from gauss.decomposition import lu
from gauss import utils
from gauss.exceptions import (
        GaussError,
        NotSquareError,
        DimensionMismatchError,
        NonInvertibleError,
)

__all__ = [
    "NonInvertibleError",
    "DimensionMismatchError",
    "NotSquareError",
    "GaussError",

    "lu",
    "utils",
    "gauss_jordan",
    "inverse",
    "ref",
    "rref",
]
