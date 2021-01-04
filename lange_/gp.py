from lange_.abs.progression import Progression


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
        >>> GP()
        []
        >>> print(GP())
        []

    Usage (square brackets syntax):
        >>> from lange_ import g_
        >>> g_[0.3, 0.6, ..., 2]
        [0.3 0.6 .*. 2.0]
        >>> g_[1, 2]
        [1 2 .*. 2]
        >>> list(g_[1, 2])
        [1, 2]
        >>> g_[1]
        [1 1 .*. 1]
        >>> list(g_[1])
        [1]
        >>> g_[3, 1, 6, 7, 0]
        [3 1 6 7 0]
        >>> list(g_[3, 1, 6, 7, 0])
        [3, 1, 6, 7, 0]
        >>> g_[4, 5, 2, 9, 4, 7, 3, 3][2:6]
        [2 9 4 7]
        >>> g_[4, 5, 2, 9, 4, 7, 3, 3][5]
        [7 7 .*. 7]
        >>> list(g_[3, 2, 6666, 7, 8, 6, 5555, 7, 3, 9][2:9:4])
        [6666, 5555]
        >>> print(g_[0.1, 0.2, ...][2:8])
        [0.4 0.8 1.6 3.2 6.4 12.8]
        >>> g_[0.1, 0.2, ...][2:8:2]
        [0.4 1.6 .*. 6.4]
        >>> list(g_[2,3,...,14])
        [2.0, 3.0, 4.5, 6.75, 10.125]
    """

    def __init__(self, *args, maxdigits=28):
        super().__init__(
            "*", 1,
            lambda a, b: a * b,
            lambda a, b: a / b,
            lambda a, b: a ** b,
            lambda a, b, c: (b / a).log10() / c.log10(),
            args,
            maxdigits
        )
