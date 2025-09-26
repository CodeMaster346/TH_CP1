# TH 2nd Fix the Game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess =2 #random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        # runtime error - the input needs to be a number, so it must be either int or float
        guess = float(input("Enter your guess: "))
        #logic error - the attempts will not go up without this so it will go on forever
        attempts += 1
        # logic error - it doesnt break anything, but if you use your tenth attempt it automatically says you used all attempts and you cant really use your tenth attempt
        if attempts > max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            # doesnt need the continue, because it runs fine eitherway
    print("Game Over. Thanks for playing!")
start_game()