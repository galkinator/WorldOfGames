import os, platform
from time import sleep

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    """Clears the terminal screen, useful for Memory Game or resetting the UI."""
    system_name = platform.system()

    if system_name == "Windows":
        os.system("cls")  # Clear screen for Windows
    else:
        os.system("clear")  # Clear screen for macOS/Linux
