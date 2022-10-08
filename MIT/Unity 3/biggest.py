animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

def biggest(aDict):
    """Returns the biggest entry within a dictionary"""
    biggest_value = 0
    for value in aDict.values():  # get us the biggest number of info within an entry
        temp = len(value)
        if temp > biggest_value:
            biggest_value = temp

    for key in aDict.keys():  # analises each key info len to find the correspondent to biggest_value
        if len(aDict[key]) == biggest_value:
            return key

biggest(animals)
