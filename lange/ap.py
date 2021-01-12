#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the lange project.
#  Please respect the license - more about this in the section (*) below.
#
#  lange is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  lange is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with lange.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.

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
