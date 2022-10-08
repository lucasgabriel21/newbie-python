# numerical method for square root using bisection

x = 25
epsilon = 0.01
lower = 0
upper = x
guess = (lower + upper)/2.0

while abs(guess**2 - x) >= epsilon:

    if guess**2 > x:
        upper = guess
        guess = (lower + upper)/2.0
    elif guess**2 < x:
        lower = guess
        guess = (lower + lower*2)/2.0

print(guess)