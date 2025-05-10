import random
def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Enter a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print(f"Please enter a number within the range 1 to {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return

def compare_results(secret_number, user_guess):
    return secret_number == user_guess


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)

    if compare_results(secret_number, user_guess):
        print("Congratulations! You guessed the correct number. ")
        return True
    else:
        print(f"Sorry, the correct number was {secret_number}. Better luck next time! ❌")
        return False

