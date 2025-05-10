import random, requests




def get_money_interval(difficulty):
    API_KEY = "e7e51e0532bf569933cad733"
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

    response = requests.get(URL)
    data = response.json()
    exchange_rate = data["conversion_rates"]["ILS"]
    usd_amount = random.randint(1,100)
    interval = (usd_amount * exchange_rate - (5-difficulty), usd_amount * exchange_rate + (5-difficulty))
    return interval, usd_amount

def get_guess_from_user(usd_amount):
    while True:
        try:
            guess = float(input(f"Guess the value of {usd_amount} USD in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play(difficulty):
    interval, usd_amount = get_money_interval(difficulty)
    guess = get_guess_from_user(usd_amount)
    print(interval)
    if interval[0] <= guess <= interval[1]:
        print("you hit the range")
        return True

    print("you're out of range :( ")
    return False





