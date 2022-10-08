animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati', 'cat', 'crocodile']}

def count(dict):
    """Count the number of values within a dictionary"""
    counter = 0
    for subelement in dict.values():
        counter += len(subelement)
    return counter

print(count(animals))