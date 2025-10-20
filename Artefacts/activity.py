import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Set random seed for reproducibility
np.random.seed(42)


# Function to generate random data
def generate_random_data(num_samples):
    activities = ["music", "sport", "meditation"]
    data = []

    for _ in range(num_samples):
        activity = np.random.choice(activities)
        time = np.random.uniform(0, 4)
        happiness = np.random.randint(1, 97)
        difference = 100 - happiness
        bias = {
            "music": 0.4,
            "sport": 0.7,
            "meditation": 0.2,
        }  # Adjusted biases for distinct slopes
        increase = (difference * time * bias[activity]) / 100

        data.append(
            {
                "Activity": activity,
                "Time": time,
                "Happiness": happiness,
                "Percentage_Increase": increase,
            }
        )

    df = pd.DataFrame(data)
    df.to_csv("generated_data.csv", index=False)  # Save data to CSV
    return df


# Generate random data
num_samples = 150
df = generate_random_data(num_samples)

# Set seaborn style
sns.set(style="whitegrid")

# Visualization with Seaborn
plt.figure(figsize=(15, 5))

# Music
plt.subplot(1, 3, 1)
sns.scatterplot(
    x="Time",
    y="Percentage_Increase",
    hue="Activity",
    data=df[df["Activity"] == "music"],
    palette="Blues",
)
sns.regplot(
    x="Time",
    y="Percentage_Increase",
    data=df[df["Activity"] == "music"],
    scatter=False,
    color="blue",
)
plt.ylim(
    df["Percentage_Increase"].min(), df["Percentage_Increase"].max()
)  # Set y-axis limits
plt.title("Music Percentage Increase")
model_music = LinearRegression().fit(
    df[df["Activity"] == "music"][["Time"]],
    df[df["Activity"] == "music"]["Percentage_Increase"],
)
plt.text(
    3,
    8,
    f"y = {model_music.coef_[0]:.2f}x + {model_music.intercept_:.2f}",
    color="blue",
)

# Sport
plt.subplot(1, 3, 2)
sns.scatterplot(
    x="Time",
    y="Percentage_Increase",
    hue="Activity",
    data=df[df["Activity"] == "sport"],
    palette="Greens",
)
sns.regplot(
    x="Time",
    y="Percentage_Increase",
    data=df[df["Activity"] == "sport"],
    scatter=False,
    color="green",
)
plt.ylim(
    df["Percentage_Increase"].min(), df["Percentage_Increase"].max()
)  # Set y-axis limits
plt.xlim(0, 4)  # Set x-axis limits
plt.title("Sport Percentage Increase")
model_sport = LinearRegression().fit(
    df[df["Activity"] == "sport"][["Time"]],
    df[df["Activity"] == "sport"]["Percentage_Increase"],
)
plt.text(
    3,
    8,
    f"y = {model_sport.coef_[0]:.2f}x + {model_sport.intercept_:.2f}",
    color="green",
)

# Meditation
plt.subplot(1, 3, 3)
sns.scatterplot(
    x="Time",
    y="Percentage_Increase",
    hue="Activity",
    data=df[df["Activity"] == "meditation"],
    palette="Oranges",
)
sns.regplot(
    x="Time",
    y="Percentage_Increase",
    data=df[df["Activity"] == "meditation"],
    scatter=False,
    color="orange",
)
plt.ylim(
    df["Percentage_Increase"].min(), df["Percentage_Increase"].max()
)  # Set y-axis limits
plt.title("Meditation Percentage Increase")
model_meditation = LinearRegression().fit(
    df[df["Activity"] == "meditation"][["Time"]],
    df[df["Activity"] == "meditation"]["Percentage_Increase"],
)
plt.text(
    3,
    8,
    f"y = {model_meditation.coef_[0]:.2f}x + {model_meditation.intercept_:.2f}",
    color="orange",
)

# Adjust layout to avoid warning
plt.subplots_adjust(wspace=0.5)

plt.show()
