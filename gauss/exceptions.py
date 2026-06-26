class GaussError(Exception):
    """
    Base exception for all gauss exceptions
    """
    
class NonInvertibleError(GaussError):
    """
    Raised when an operation requires an invertible matrix
    """

class NotSquareError(GaussError):
    """
    Raised when an operation requires a square matrix
    """

class DimensionMismatchError(GaussError):
    """
    Raised when an operation failed because of a dimension mismatch
    """
