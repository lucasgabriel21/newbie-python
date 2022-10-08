from math import tan, pi


def poly_area(n, s):
    """Returns the area of a polygon with n sides of length s"""
    return (0.25 * n * s**2) / tan(pi / n)


def poly_perimeter(n, s):
    """Returns the perimeter of a polygon with n sides of length s"""
    return n * s


def polysum(n, s):
    """Returns the sum of the area and square
    of the perimeter of a regular polygon
    with n sides of length s"""
    return round(poly_area(n, s) + poly_perimeter(n, s)**2, 4)
