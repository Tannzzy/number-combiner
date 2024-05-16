# import randint from random module
from random import randint


def answer():
    '''
    generate random number

    return:
    a random int between 1 and 100
    '''

    # select a random number between 1 and 100
    answer = randint(1, 100)
    return answer


def guessing(guess: int, answer: int) -> str:
    '''
    compares guess and answer value, see if guess is higher,
    lower or equal to answer

    arg:
    guess(int): the user's guessed number
    answer(int): the correct number

    return:
    a string representing if guess is higher, lower or equal
    to answer
    '''

    # if guess is less than the answer
    if guess > answer:
        return 'lower'
    # if guess is more than the answer
    elif guess < answer:
        return 'higher'
    # if guess equals answer
    else:
        return 'equal'


def printing(results: str) -> None:
    '''
    prints a response based on the value of 'results'

    arg:
    a string representing if guess is higher, lower or equal
    to answer
    '''

    # if result is 'lower'
    if results == 'lower':
        print('lower')

    # if result is 'higher'
    elif results == 'higher':
        print('higher')

    # if result is neither 'higher' nor 'lower'
    else:
        print('you won')


# generate a random number that the user is trying to guess
answer = answer()

# initialise guess string
guess = ''

# while user's guess is nto equal to the answer
while guess != answer:
    # prompt user to guess a number
    guess = int(input('guess the random number between 1 and 100: '))

    # calculate result
    results = guessing(guess, answer)

    # print the corresponding text message comparing guess and answer
    printing(results)
