# numerical method for cube root bisection

x = 27
epsilon = 0.01

if x > 1:
    lower = 0
    upper = x
    guess = (lower + upper)/2

elif abs(x) > 0 and abs(x) <= 1:
    lower = x
    upper = 1
    guess = (lower + upper) / 2

elif x < 0:

while abs(guess**3 - x) >= epsilon:
    if guess**3 > x:
        upper = guess
        guess = (lower + upper) / 2.0
    else:
        lower = guess
        guess = (lower + lower * 2) / 2.0

if x < 0:
    guess = -guess

print(guess)