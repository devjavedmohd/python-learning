import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """ Returns the number of turns left """
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Please type your difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(0, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(answer=answer, guess=guess, turns=turns)

        if turns == 0:
            print("You run out of the guess you will loose!")
            return
        elif guess != answer:
            print("Guess again.")


game()

