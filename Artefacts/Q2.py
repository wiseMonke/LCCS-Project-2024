import pandas as pd

# Read the CSV file
df = pd.read_csv("data.csv")

# Get the most recent happiness value
most_recent_happiness = df[" Happiness"].iloc[-1]

# Calculate the difference
difference = 100 - (most_recent_happiness * 10)


# Function to get valid input for activity
def get_activity():
    while True:
        activity = input(
            "Which activity are you planning to do? (music/sport/meditation): "
        ).lower()
        if activity in ["music", "sport", "meditation"]:
            return activity
        else:
            print(
                "Invalid input. Please choose from 'music', 'sport', or 'meditation'."
            )


# Function to get valid input for time
def get_time():
    while True:
        try:
            time = float(
                input("How many hours will you spend on this activity? (0-4): ")
            )
            if 0 <= time <= 4:
                return time
            else:
                print("Invalid input. Please enter a value between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Get valid user inputs
activity = get_activity()
time = get_time()

# Dictionary to store bias values for each activity
bias_values = {"music": 0.7, "sport": 0.8, "meditation": 0.9}

# Calculate the increase in happiness
increase_in_happiness = time * bias_values[activity] / 100
increase_in_happiness *= difference

# Output
print(
    f"With {time} hours of {activity}, you can expect an increase in happiness of {increase_in_happiness:.2f}%."
)
