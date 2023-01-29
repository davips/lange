# Based on:
# https://stackoverflow.com/questions/3018758/determine-precision-and-ret-of-particular-number-in-python


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

import decimal as dec
from functools import partial
from math import nan


def detect_precision(x, maxdigits=28):
    """
    Detect the precision (include digits before and after the decimal separator).

    The checking only works if 'max_digits' is large enough.

    Usage:
        >>> detect_precision(3)
        1
        >>> detect_precision(3.7)
        2
        >>> detect_precision(3.0)
        1
        >>> detect_precision(30.0e-4)
        4
        >>> detect_precision(30.0e4)
        6

    Based on:
    https://stackoverflow.com/questions/3018758/determine-precision-and-ret-of-particular-number-in-python
    """
    if x is ...:
        return 0
    ctx = dec.Context()
    ctx.prec = maxdigits
    d1 = ctx.create_decimal(repr(float(x)))
    txt = format(d1, "f")
    l = len(txt) - 1
    if int(x) == x:
        l -= 1
    return l


def list2progression(lst, maxdigits=28):
    """Convert list representing A. or G. progression to lange

    >>> list2progression([0,1,2,...,9])
    [0 1 .+. 9]
    >>> list2progression([1,2,4,...,16])
    [1 2 .*. 16]

    Parameters
    ----------
    lst

    Returns
    -------

    """
    if len(lst) < 3:  # pragma: no cover
        raise Exception(
            f"Cannot guess if you want an arithmetic or a geometric projection. Provide 3 numbers, not {len(lst)}."
        )

    # Protect diffs and ratios from floating point inequality issues (e.g. 0.8 - 0.6 != 0.2).
    precision = max(map(partial(detect_precision, maxdigits=maxdigits), lst))
    decctx = dec.Context()
    decctx.prec = precision
    lst_dec = [decctx.create_decimal(x) for x in lst if x is not ...]

    # Calculate diffs and ratios.
    try:
        diff1 = lst_dec[1] - lst_dec[0]
        diff2 = lst_dec[2] - lst_dec[1]
        ratio1 = nan if lst_dec[0] == 0 else lst_dec[1] / lst_dec[0]
        ratio2 = nan if lst_dec[1] == 0 else lst_dec[2] / lst_dec[1]
    except:  # pragma: no cover
        raise InconsistentLange(f"Cannot identify whether this is a G. or A. progression: {lst}")
    newlst = lst[0:2] + lst[3:]

    if diff1 == diff2:
        from lange.ap import AP

        return AP(*newlst)
    elif ratio1 == ratio2:
        from lange.gp import GP

        return GP(*newlst)
    else:  # pragma: no cover
        raise InconsistentLange(
            f"Cannot identify whether this is a G. or A. Progression: {lst}", diff1, diff2, ratio1, ratio2
        )


class InconsistentLange(Exception):
    pass
