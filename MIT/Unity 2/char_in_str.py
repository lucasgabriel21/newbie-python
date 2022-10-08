def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) == 0:
        return False

    guess = aStr[len(aStr)//2]

    if guess == char:
        return True
    elif char < guess:
        return isIn(char, aStr = aStr[:len(aStr)//2])
    else:
        return isIn(char, aStr = aStr[len(aStr)+1//2:])

print(isIn('d','abcefghi'))