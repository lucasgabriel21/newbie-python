def applyToEach(L, f):
    """Changes each element of a list accordingly to the function f"""
    for i in range(len(L)):
        L[i] = f(L[i])


def module(e):
    """Returns the absolute value of an element"""
    return abs(e)


def plus_one(e):
    """Returns the the element added to 1"""
    return e + 1


def square(e):
    """Returns element^2"""
    return e * e


testList = [1, -4, 8, -9]
applyToEach(testList, module)
print(testList)

testList = [1, -4, 8, -9]
applyToEach(testList, plus_one)
print(testList)

testList = [1, -4, 8, -9]
applyToEach(testList, square)
print(testList)
