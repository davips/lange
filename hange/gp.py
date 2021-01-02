import math

from hange.abs.progression import Progression


class GP(Progression):
    """Geometric Progression. A flexible inductive sequence of numbers based on Haskell interval notation.

    maxdigits: maximum amount of digits verified during precision detection
                (includes numbers to the left and to the right of the decimal separator, if any)

    Usage:
        >>> print(GP(5))
        [5]
        >>> print(GP(5, 1))
        [5 1]
        >>> gp = GP(0.3, 0.6, ..., 6)
        >>> gp
        [0.3 0.6 .*. 6.0]
        >>> print(gp)
        [0.3 0.6 1.2 2.4 4.8]
        >>> gp[1]
        0.6
        >>> print(GP(0.2, 4.1, 0.9))
        [0.2 4.1 0.9]
        >>> gp = GP(0.3, 0.6, ...)
        >>> gp
        [0.3 0.6 .*. inf]
        >>> GP(0.3, 0.6, ...)[:8]
        [0.3 0.6 .*. 38.4]
        >>> list(GP(0.3, 0.6, ...)[:8])
        [0.3, 0.6, 1.2, 2.4, 4.8, 9.6, 19.2, 38.4]

    Usage (square brackets syntax):
        >>> from hange import h_
        >>> h_[0.3, 0.6, ..., 2]
        [0.3 0.6 .*. 2.0]
    """

    def __init__(self, *args, maxdigits=28):
        super().__init__(
            "*",
            lambda a, b: a * b,
            lambda a, b: a / b,
            lambda a, b: a ** b,
            lambda a, b, c: (b / a).log10() / c.log10(),
            args,
            maxdigits
        )
