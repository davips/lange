from lange_.ap import AP
from lange_.gp import GP


class APwithBrackets:
    def __getitem__(self, item):
        """Helper class to allow overriding square brackets.

        Import object 'h' from module 'lange' to use it implicitly.

        Usage:
            >>> from lange_ import a_
            >>> (a_[0.6, 0.8, ..., 2])
            [0.6 0.8 .+. 2.0]
            >>> print(a_[0.6, 0.8, ..., 2])
            [0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0]
        """
        if isinstance(item, tuple):
            return AP(*item)
        else:
            return AP(item)


class GPwithBrackets:
    def __getitem__(self, item):
        """Helper class to allow overriding square brackets.

        Import object 'h_' from module 'lange' to use it implicitly.

        Usage:
            >>> from lange_ import g_
            >>> (g_[0.3, 0.6, ..., 2])
            [0.3 0.6 .*. 2.0]
            >>> print(g_[0.3, 0.6, ..., 2])
            [0.3 0.6 1.2]
        """
        if isinstance(item, tuple):
            return GP(*item)
        else:
            return GP(item)
