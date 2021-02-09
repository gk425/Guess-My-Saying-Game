# Giwon Kim (Soka University of America, 19')
# Computer Science, Mini project 1
# Prof. Anna Varvak

# GuessMySaying.py
# This is an initial file for the python code that implements the game
# "Just Saying!", where the player needs to guess a popular saying
# one letter at a time in fewer than 10 wrong guesses.


# ---------------------------------------------------------------------- #
# Here are some functions that you will need to implement.
# You are welcome to write more functions, of course.
# ---------------------------------------------------------------------- #

# getSaying
# Returns a string which is a popular saying
# For basic-level program, the saying is written into the code.
# For higher level programs, the function should go into "Sayings.txt"
# and return a randomly picked line.
def getSaying() :
    # Selects a random saying from Sayings.txt
    import random

    fhandle = open('Sayings.txt')
    # how many sayings are there?
    # store the result in numSayings
    numSayings = 0
    for line in fhandle :
        numSayings = numSayings + 1        # numSayings += 1 is the same
    # pick an integer from 1 to numSayings at random
    # store the result in chosenSayingNum

    chosenSayingNum = random.randint(1, numSayings)

    # actually find and print out the chosen Saying
    fhandle = open('Sayings.txt')
    n = 0
    for line in fhandle :
        n  = n + 1
        if n == chosenSayingNum :
            return(line)
            break

# blankSaying
# Parameters: saying (a string)
# Returns a string that is like the saying, but with every letter replaced
# with '_'.
# Example: if saying = "That's all, folks!", returns "____'_ ___, _____!"
def blankSaying(saying) :
    allUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allLower = 'abcdefghijklmnopqrstuvwxyz'
    index = 0         # index is an index number
    displayStr = ''   # displayStr is displaying the result
    while index < len(saying) :
        # This is for the marks e.g. ? ! . , ''
        if not (saying[index] in allUpper) and not (saying[index] in allLower) :
            displayStr = displayStr + saying[index]
        # Making letters to blanks.
        elif saying[index] in allUpper :
            n = 0
            while n < len(allUpper) :
                if allUpper[n] == saying[index] :
                    break
                n = n + 1
            displayStr = displayStr + "_"
        else :
            n = 0
            while n < len(allLower) :
                if allLower[n] == saying[index] :
                    break
                n = n + 1
            displayStr = displayStr + "_"
        index = index + 1
    return displayStr


# getGuess
# Prompts the player to guess a letter.
# Returns the player's guessed letter.
# For basic or intermediate level program, you can assume that the player will
# always give exactly one letter as an input.
# advanced-level program should be able to handle other inputs.
def getGuess() :
    allUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allLower = 'abcdefghijklmnopqrstuvwxyz'
    guess = input ("Please make a guess: ")
    while True :
        # if the guess is more than one letter or just enter, ask to guess again!
        if len(guess) != 1 :
            print("Please guess one letter at a time! Or please don't just hit Enter.")
            guess = input ("Please make a guess: ")
        # if the guess is puctuation, ask to guess again!
        elif not (guess in allUpper) and not (guess in allLower) :
            print("Please only guess letters!")
            guess = input ("Please make a guess: ")
        # if the guess is a letter, then return!
        else :
            message = guess
            break
    return message

# checkGuess
# Parameters: guess (a single character string), saying (a string)
# Checks if the guess is in the saying.
# Returns True if it is, False if it isn't.
def checkGuess(guess, saying) :
    allUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allLower = 'abcdefghijklmnopqrstuvwxyz'
    # Recognize uppercase and lowercase indifferent
    newguess = ''   # newguess is for Uppercase or Lowercase guess.
    if guess in saying :
        newguess = guess
    else :
        if guess in allUpper :
            k = 0   # k is another index
            while k < len(allUpper) :  # find where in allUpper is the letter guess
                if (allUpper[k] == guess) :
                    q = k
                    if (allLower[q] in saying) :
                        break
                k = k + 1
            newguess = newguess + allLower[q]
        else :
            k = 0   # k is another index
            while k < len(allLower) :  # find where in allLower is the letter guess
                if (allLower[k] == guess) :
                    q = k
                    if (allUpper[q] in saying) :
                        break
                k = k + 1
            newguess = newguess + allUpper[q]
    # Main checkGuess function codes
    n = 0                         # n is the n-est letter of bigstr
    m = len(newguess)             # m is the m-est letter of bigstr
    correct_guess = False
    while m <= len(saying) :
        if saying[n:m] == newguess :
            correct_guess = True
        n = n + 1
        m = m + 1
    return correct_guess

# indifferent
# Duplicate a single alphabet, so that the main function can recognize uppercase and lowercase letter indifferently
# e.g. if guess is 'w' and the saying is "Wherer are we going?". Then indifferent function duplicates 'w' as 'W' and 'w'.
def indifferent(guess) :
    allUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allLower = 'abcdefghijklmnopqrstuvwxyz'
    duplguess = ""  # duplicate guess e.g. guess = "ab" then, duplguess = "AaBb"
    k = 0  # k is index for guess
    while k < len(guess) :
        if guess[k] in allUpper :
            n = 0   # n is an index
            while n < len(allUpper) :  # find where in allUpper is the letter guess
                if (allUpper[n] == guess[k]) :
                        break
                n = n + 1
            duplguess = duplguess + allUpper[n] + allLower[n]
        else :
            n = 0   # n is an index
            while n < len(allLower) :  # find where in allUpper is the letter guess
                if (allLower[n] == guess[k]) :
                        break
                n = n + 1
            duplguess = duplguess + allLower[n] + allUpper[n]
        k = k + 1
    return duplguess


# revealGuessedLetter
# Intended to reveal the guessed letter in the string displayed to the player.
# Parameters: guess (a signle character string), saying (a string),
#       displayStr (a string)
# Assumes: guess is in the saying
# For every place where guess appears in saying, changes the character in
# displayStr to the character in the original saying.
def revealGuessedLetter(guess, saying, displayStr) :
    allUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allLower = 'abcdefghijklmnopqrstuvwxyz'
    k = 0     # k is an index number
    displayStr = ""    # displaying the result, after having a user's guess.
    newguess = indifferent(guess)    # Use a function 'indifferent', so that the program recognizes uppercase and lowercase both.
    while k < len(saying) :
        if not (saying[k] in allUpper) and not (saying[k] in allLower) :
            displayStr = displayStr + saying[k]
        elif (saying[k] in newguess) :               # From indifferent(guess), now user's guess is duplicated. So the function can recognize uppercase and lowercase both.
            displayStr = displayStr + saying[k]
        elif not (saying[k] in newguess) :
            displayStr = displayStr + "_"
        k = k + 1
    return displayStr

# sayingFullyGuessed
# parameters: saying and displayStr, both strings.
# If the saying and displayStr are the same string, return True, else return False
def sayingFullyGuessed(saying, displayStr) :
    if (saying == displayStr) :
        outcome = True
    else :
        outcome = False
    return outcome

# game
# It is the main codes for the project.
# This function helps the user restart their game.
# For example, if it returns option == True, then the game restarts, vice versa.
def game() :
    accumguessed = ''  # accumulated correct guesses from the user
    wrong_guess = ''   # accumulated wrong guesses from the user
    wrong = 0          # the number of wrong guesses
    limit = 10         # limitation of wrong guesses
    guessed_the_saying = False   # if the saying and displayStr are the same string, guessed_the_saying = True.

    print('You must guess a popular saying with fewer than 10 wrong guesses.')
    print('Let\'s start!')
    print('\n')

    random_saying = getSaying()
    displayStr = blankSaying(random_saying)
    print(displayStr)

    # if the saying and displayStr are not the same string, and wrong guesses is less than 10 chances, then keep playing!
    while (guessed_the_saying == False) and (wrong < limit) :
        user_guess = getGuess()    # Check the user's guess is a letter e.g. "a"
        accumguessed = accumguessed + user_guess   # accumulate the guesses from the user
        checking = checkGuess(user_guess, random_saying)  #Check the guess is in the saying. Return -> True / False
        # In order to let the user know that don't make the same mistake
        if user_guess in wrong_guess :
            wrong = wrong - 1   # doesn't count it again towards the number of guess, if this wrong guess is already made.
            print("You already tried this wrong word.")
        # If checkGuess is True, then display a result as 'filledblanks'
        if checking == True :
            filledblanks = revealGuessedLetter(accumguessed, random_saying, displayStr)
            print(filledblanks)
            # If the saying and filledblanks are the same string, then guessed_the_saying = True.
            if sayingFullyGuessed(random_saying, filledblanks) == True :
                guessed_the_saying = True
        # Counting the number of wrong guesses and save the wrong guessed letters.
        else :
            wrong = wrong + 1
            wrong_guess = wrong_guess + indifferent(user_guess)
            print('Wrong! Try again!' 'You make', wrong, 'mistakes.')   # Displaying the number of wrong guesses to the user.
    # Stop the game when the player guesses all the letters in the saying.
    if (guessed_the_saying == True) :
        print("Congrats! You win!")
        answer = input("Type 'yes' to play again, or type 'no' to quit > ")
        while True :
            if (answer == 'yes') or (answer == 'Yes') or (answer == 'YES') :
                option = True          # we're going to return 'option'.
                break
            elif (answer == 'no') or (answer == 'No') or (answer == 'NO') :
                option = False
                break
            else :
                print("Please type 'yes/no'.")
                answer = input("Type 'yes' to play again, or type 'no' to quit > ")

    # Stop the game when the player has made 10 wrong guesses.
    if wrong == limit :
        print("Sorry, you've got 10 wrong guesses.")
        print("The saying was:", random_saying)
        answer = input("Type 'yes' to play again, or type 'no' to quit > ")
        while True :
            if (answer == 'yes') or (answer == 'Yes') or (answer == 'YES') :
                option = True
                break
            elif (answer == 'no') or (answer == 'No') or (answer == 'NO') :
                option = False
                break
            else :
                print("Please type 'yes/no'.")
                answer = input("Type 'yes' to play again, or type 'no' to quit > ")

    return  option


# -------------------------------------------------------------------------- #
# Your main code should go below.
# -------------------------------------------------------------------------- #

k = 0  # k is an index number
numgame = game() # numgame is the variable name for the game.
while k >= 0 :
    # If the user wants to restart the game.
    if numgame == True :
        numgame = game()
    # If the user wants to quit the game.
    elif numgame == False :
        numgame = quit()
    k = k + 1
