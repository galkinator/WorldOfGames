from random import  randint
from time import sleep
import sys


def generate_sequence(difficulty):
    sequence = [randint(1, 101) for _ in range(difficulty)]

    print("Memorize the sequence:")
    for number in sequence:
        sys.stdout.write(f"\r{number}   ")  # Print number without a newline
        sys.stdout.flush()  # Force print update
        sleep(2)

    sys.stdout.write("\r" + " " * 10 + "\r")  # Clear the last number
    sys.stdout.flush()

    return sequence


def get_list_from_user(difficulty):
    user_list = []

    print(f"Enter {difficulty} numbers one by one:")

    for i in range(difficulty):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                user_list.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return user_list


def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    sequence = generate_sequence(difficulty)
    user_sequence = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_sequence):
        print("well done, you memorized perfectly!\n")
        return True
    print("not the same numbers, try better next time :)\n")
    return False

