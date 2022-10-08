# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secret_chars = list(secretWord)
    for char in secret_chars:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secret_chars = list(secretWord)
    for i in range(len(secret_chars)):
        if secret_chars[i] not in lettersGuessed:
            secret_chars[i] = '_ '
    return ''.join(secret_chars)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = list(string.ascii_lowercase)
    for i in range(len(alphabet)):
        if alphabet[i] in lettersGuessed:
            alphabet[i] = ''
    return ''.join(alphabet)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    space = '-----------'
    print(space)  # new trial
    remaining_guesses = 8  # initial number of guesses
    lettersGuessed = []  # appends the letters already guessed
    # while the user has guesses and has not found the correct answer
    while remaining_guesses > 0 and not isWordGuessed(secretWord, lettersGuessed):
        av_letters = getAvailableLetters(lettersGuessed)  # letters that can be guessed
        print('You have {} guesses left.'.format(remaining_guesses))
        print('Available Letters: {}'.format(av_letters))
        letter = input('Please guess a letter: ').lower()  # get the guess as input

        while letter in lettersGuessed:  # if the letter is repeated
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            print(space)
            print('You have {} guesses left.'.format(remaining_guesses))
            print('Available Letters: {}'.format(av_letters))
            letter = input('Please guess a letter: ').lower()

        lettersGuessed.append(letter)  # letter guessed goes into the list
        if letter in list(secretWord):  # if the letter guessed is in the word
            print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
        else:  # if the letter guessed is not in the word
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            remaining_guesses -= 1
        print(space)

    if isWordGuessed(secretWord, lettersGuessed):  # if the word is discovered
        print('Congratulations, you won!')
    else:  # if you fail
        print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
