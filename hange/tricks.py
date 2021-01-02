import decimal as dec


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

    https://stackoverflow.com/questions/3018758/determine-precision-and-ret-of-particular-number-in-python
    """
    ctx = dec.Context()
    ctx.prec = maxdigits
    d1 = ctx.create_decimal(repr(float(x)))
    txt = format(d1, 'f')
    l = len(txt) - 1
    if int(x) == x:
        l -= 1
    return l
