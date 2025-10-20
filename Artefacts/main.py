import csv
from datetime import datetime
import random
import graph
import picture


def validate_input(value, category):
    try:
        value = int(value)
        if 1 <= value <= 10:
            return True
    except ValueError:
        pass
    print(
        f"Invalid input for {category} level. Please enter an integer between 1 and 10."
    )
    return False


def get_user_input(category):
    while True:
        user_input = input(f"Enter {category} level (1-10): ")
        if validate_input(user_input, category):
            return int(user_input)


def save_to_csv(timestamp, stress, light, sleep, happiness):
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, stress, light, sleep, happiness])


def calculate_happiness(stress, light, sleep):
    # Use a more complex algorithm for happiness calculation
    happiness_score = (stress * 0.3 + light * 0.3 + sleep * 0.4) * random.uniform(
        0.8, 1.2
    )
    # Ensure the score is between 1 and 100
    happiness_score = min(100, max(1, happiness_score))
    return round(happiness_score, 2)


def print_divider():
    print("-" * 40)


if __name__ == "__main__":
    print("\nWelcome to the Mood Tracker!")
    print_divider()

    # Get stress level input from the user
    stress = get_user_input("Stress")

    # Get light level input from the user
    print_divider()
    light = get_user_input("Light")

    # Get sleep level input from the user
    print_divider()
    sleep = get_user_input("Sleep")

    # Calculate happiness
    print_divider()
    happiness = calculate_happiness(stress, light, sleep)

    # Save to CSV
    timestamp = datetime.now().strftime("%Y-%m-%d")
    save_to_csv(timestamp, stress, light, sleep, happiness)

    print_divider()
    # print("Data saved successfully.")
    print_divider()

    # These functions are called after obtaining user inputs
    picture.detect_faces_live()
    print(
        f"Your calculated happiness (%): {picture.read_latest_happiness_percentage()}%"
    )
    graph.main()

    print("The end")
