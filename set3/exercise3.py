"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    while True:
        try:
            lowerBound = int(input("Enter a lower bound: "))
            upperBound = int(input("Enter an upper bound: "))
            print(f"OK then, a number between {lowerBound} and {upperBound} ?")

        except Exception as e:
            print(f"Sorry. That is not a number. Try again. ({e})")
        upperBound = int(upperBound)

        actualNumber = random.randint(lowerBound, upperBound)

        guessed = False

        while not guessed:
            try:
                guessedNumber = int(input("Guess a number: "))
                if lowerBound <= guessedNumber <= upperBound:
                    print(f"You guessed {guessedNumber},")
                else:
                    print(
                        f"{guessedNumber} is not between {lowerBound} and {upperBound}, you silly goose!. Try again."
                    )
            except Exception as e:
                print(f"Sorry. That is not a number. Try again. ({e})")

            if guessedNumber == actualNumber:
                print(f"You got it!! It was {actualNumber}")
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
        return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
