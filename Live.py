import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Score import add_score

def welcome(name):
    output = (f"hello {name} and welcome to World Of Games (WOG).\n"
              f"here you can find many cool gams to play")

    return output

def load_game():
    while True:
        try:
            game_to_play = int(input(f"Please choose a game to play:\n"
                                 f"    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                                 f"    2. Guess Game - guess a number and see if you chose like the computer\n"
                                 f"    3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n"))

            if game_to_play not in range(1, 4):
                print("please type a number between 1 to 3")
                continue
            break

        except ValueError:
            print("invalid input, please type a *number* between 1 to 3")


    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))

            if difficulty not in range(1, 6):
                print("please type a number between 1 to 5")
                continue
            break

        except ValueError:
            print("invalid input, please type a *number* between 1 to 5")

    result = 0
    if game_to_play == 2:
        print("\nStarting Guess Game...")
        result = GuessGame.play(difficulty)

    if game_to_play == 1:
        print("\nStarting Memory Game...")
        result = MemoryGame.play(difficulty)

    if game_to_play == 3:
        print("\nStarting Currency Roulette game...")
        result = CurrencyRouletteGame.play(difficulty)


    if result == 1:
        add_score(difficulty)

