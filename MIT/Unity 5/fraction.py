class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerator = self.getNumer() * other.getDenom() \
                    + other.getNumer() * self.getDenom()
        denominator = self.getDenom() * other.getDenom()
        return fraction(numerator, denominator)
    def __sub__(self, other):
        numerator = self.getNumer() * other.getDenom() \
                    - other.getNumer() * self.getDenom()
        denominator = self.getDenom() * other.getDenom()
        return fraction(numerator, denominator)
    def convert(self):
        return self.getNumer() / self.getDenom()

oneHalf = fraction(1,2)
twoThirds = fraction(2,3)
print(oneHalf)
print(twoThirds)
print(oneHalf+twoThirds)
print(oneHalf.getNumer())
print(twoThirds.getDenom())
print(twoThirds-oneHalf)
print(oneHalf.convert())
print(twoThirds.convert())
