def genPrimes():
    """Generator function of prime numbers"""
    number = 2
    yield number
    primes = [2]
    while True:
        number += 1
        isPrime = True  # starts suposing that the number is a prime
        for p in primes:  # testing if it is a prime
            if number % p == 0:
                isPrime = False
        if isPrime:  # if it passes all tests
            primes.append(number)  # enters in the primes list
            yield number  # generated using next() method

gen = genPrimes()