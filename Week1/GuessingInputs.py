# input() function is used to take input from the user.

# Guess a number game

# THis program will allow the user to select a number in a given range
# The program will then generate a random number in the that range.

# the user will try to guess this number
# after each guess, the program will provide clues indicating whether
# the guess was too high or too low.

# what is my data? - int
# how can I take that data to generate a random number?
            # query on google: how to generate a random number in python

# how can I continously run the program until the user guesses the correct number? - YES while loop or some kind of loop - until certain condition is met


# import the random module

import random

# print(random.randint(1, 10))

def guess_the_number():
# set the range for the random number

    low = int(input("Enter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))

#handle the edge case where the low is greater than the high
    if low > high:
        low, high = high, low
        print("I think you meant to say the other way.")

    # Generate a random number within the given range
    number_to_guess = random.randint(low, high)
    print("the random number", number_to_guess)

    # initialize the user guess to 0 (attempts = 0)
    attempts = 0
    # provide user acknowledgement
    print(f"You have selected a number between {low} and {high}. Can you try to guess it?")

    while True:
        # increment the attempt count by 1
        attempts += 1

        # get the users guess
        guess = int(input("Enter your guess: "))
        print("attempts", attempts)
        print("the guess", guess)
        # break

        if guess < number_to_guess:
            print("Your guess is too low. Try again.")
        elif guess > number_to_guess:
            print("Your guess is too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_the_number()