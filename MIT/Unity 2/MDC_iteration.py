def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    min_value = min(a, b)
    max_value = max(a, b)
    divisor = 1

    while divisor <= min_value:
        if min_value % divisor == 0:
            min_value_divisor = divisor
        if max_value % min_value_divisor == 0:
            max_value_divisor = min_value_divisor

        divisor += 1

    return min(min_value_divisor, max_value_divisor)
