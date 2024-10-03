from random import randint
from art import logo



EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    user_guess = int(user_guess)
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")  

    turns = set_difficulty()  
    guess = None
    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = input("Make a guess: ")

        turns = check_answer(guess, answer, turns)  

        if int(guess) == answer:
            break  
        elif turns == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")


game()
