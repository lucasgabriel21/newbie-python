def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    if a == 0 or b == 0:
        return max(a, b)
    else:
        return gcdRecur(b, a % b)
