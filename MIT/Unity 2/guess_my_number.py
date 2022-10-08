# you think about an integer in the interval [0,100) and the computer guess the answer

print('Please think of a number between 0 and 100!')

# guessing
lower = 0
upper = 100
guess = (lower + upper)//2

print('Is your secret number ' + str(guess) + '?')
ans = input("Enter 'h' to indicate the guess is too high. "
            "Enter 'l' to indicate the guess is too low. "
            "Enter 'c' to indicate I guessed correctly. ")

while ans != 'c':

    while ans != 'h' and ans != 'l' and ans != 'c':
        print('Sorry, I did not understand your input.')
        print('Is your secret number ' + str(guess) + '?')
        ans = input("Enter 'h' to indicate the guess is too high. "
                    "Enter 'l' to indicate the guess is too low. "
                    "Enter 'c' to indicate I guessed correctly. ")

    while ans == 'h':
        upper = guess
        guess = (lower + upper)//2
        print('Is your secret number ' + str(guess) + '?')
        ans = input("Enter 'h' to indicate the guess is too high. "
                    "Enter 'l' to indicate the guess is too low. "
                    "Enter 'c' to indicate I guessed correctly. ")

    while ans == 'l':
        lower = guess
        guess = (lower + upper)//2
        print('Is your secret number ' + str(guess) + '?')
        ans = input("Enter 'h' to indicate the guess is too high. "
                    "Enter 'l' to indicate the guess is too low. "
                    "Enter 'c' to indicate I guessed correctly. ")

print('Game over. Your secret number was: ' + str(guess))