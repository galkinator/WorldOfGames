from Utils import SCORES_FILE_NAME
import os

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    score = 0

    if os.path.exists(SCORES_FILE_NAME):
        try:
            with open(SCORES_FILE_NAME, "r") as file:
                score = int(file.read().strip())  # Read and convert to int
        except ValueError:
            score = 0  # Reset if file is corrupted

        # Update the score
    score += POINTS_OF_WINNING

        # Save the new score
    with open(SCORES_FILE_NAME, "w") as file:
        file.write(str(score))

