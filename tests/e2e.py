from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def test_scores_service(url):
    try:
        # Launch browser
        driver = webdriver.Chrome()  # You can also use Firefox, Edge, etc.
        driver.get(url)
        sleep(2)  # Wait for page to load

        # Get score value from element
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text.strip())

        # Clean up
        driver.quit()

        # Check if score is a number between 1 and 1000
        return 1 <= score <= 1000

    except Exception as e:
        print(f"Test failed: {e}")
        return False


def main_function():
    url = "http://127.0.0.1:5001/"  # Change if using different host/port
    result = test_scores_service(url)
    if result:
        sys.exit(0)
    else:
        sys.exit(1)

main_function()