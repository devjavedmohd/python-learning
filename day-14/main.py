import random
from game_data import data

# Display art


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"


# score keeping
score = 0

# Make the game repeatable.
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    def check_answer(guess, a_followers, b_followers):
        """ Use if statement to check if user"""
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"


    # Generate random Account 1
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess.
    guess: str = input("Who has more followers? Type A or B: ").lower()

    # Check if user is correct.

    # Get follower account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Use if statement of check if user is correct.

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print("++++++++++++++++++++++++++++++++++++++++")
        print(f"You are right!. Current score: {score}")
        print("----------------------------------------")
    else:
        game_should_continue = False
        print("++++++++++++++++++++++++++++++++++++++++")
        print(f"Sorry, That's wrong. Final score {score}")
        print("----------------------------------------")

    # Make the account position B become the next account position A.

    # Clear the screen between round.































