from lange.abs.progression import Progression


class AP(Progression):
    """Arithmetic Progression. A flexible inductive sequence of numbers based on Haskell interval notation.

    maxdigits: maximum amount of digits verified during precision detection
                (includes numbers to the left and to the right of the decimal separator, if any)

    Usage:
        >>> print(AP(5))
        [5]
        >>> print(AP(5, 1))
        [5 1]
        >>> print(AP(1, 3, ..., 10))
        [1 3 5 7 9]
        >>> ap = AP(0.6, 0.8, ..., 1.2)
        >>> ap
        [0.6 0.8 .+. 1.2]
        >>> print(ap)
        [0.6 0.8 1.0 1.2]
        >>> ap[1]
        0.8
        >>> print(AP(0.2, 4.1, 0.9))
        [0.2 4.1 0.9]
        >>> ap = AP(0.6, 0.8, ...)
        >>> ap
        [0.6 0.8 .+. inf]
        >>> print(ap[:5])
        [0.6 0.8 1.0 1.2 1.4]
        >>> AP()
        []
        >>> print(AP())
        []

    Usage (square brackets syntax):
        >>> from lange import ap
        >>> (ap[0.6, 0.8, ..., 2])
        [0.6 0.8 .+. 2.0]
        >>> ap[1, 2]
        [1 2 .+. 2]
        >>> list(ap[1, 2])
        [1, 2]
        >>> ap[1]
        [1 1 .+. 1]
        >>> list(ap[1])
        [1]
        >>> ap[3, 1, 6, 7, 0]
        [3 1 6 7 0]
        >>> list(ap[3, 1, 6, 7, 0])
        [3, 1, 6, 7, 0]
        >>> ap[4, 5, 2, 9, 4, 7, 3, 3][2:6]
        [2 9 4 7]
        >>> ap[4, 5, 2, 9, 4, 7, 3, 3][5]
        [7 7 .+. 7]
        >>> list(ap[3, 2, 6666, 7, 8, 6, 5555, 7, 3, 9][2:9:4])
        [6666, 5555]
        >>> print(ap[0.1, 0.2, ...][2:8])
        [0.3 0.4 0.5 0.6 0.7 0.8]
        >>> ap[0.1, 0.2, ...][2:8:2]
        [0.3 0.5 .+. 0.7]
    """

    def __init__(self, *args, maxdigits=28):
        super().__init__(
            "+", 0,
            lambda a, b: a + b,
            lambda a, b: a - b,
            lambda a, b: a * b,
            lambda a, b, c: (b - a) / c,
            args,
            maxdigits
        )
