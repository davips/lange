from hange.ap import AP
from hange.gp import GP


class APwithBrackets:
    def __getitem__(self, item):
        """Helper class to allow overriding square brackets.

        Import object 'h' from module 'hange' to use it implicitly.

        Usage:
            >>> from hange import h
            >>> (h[0.6, 0.8, ..., 2])
            [0.6 0.8 .+. 2.0]
            >>> print(h[0.6, 0.8, ..., 2])
            [0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0]
        """
        return AP(*item)


class GPwithBrackets:
    def __getitem__(self, item):
        """Helper class to allow overriding square brackets.

        Import object 'h_' from module 'hange' to use it implicitly.

        Usage:
            >>> from hange import h_
            >>> (h_[0.3, 0.6, ..., 2])
            [0.3 0.6 .*. 2.0]
            >>> print(h_[0.3, 0.6, ..., 2])
            [0.3 0.6 1.2]
        """
        return GP(*item)

