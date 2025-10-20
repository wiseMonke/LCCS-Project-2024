import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


def plot_regression(df, feature, title, ax):
    sns.regplot(x=feature, y="Happiness", data=df, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(feature)
    ax.set_ylabel("Happiness")

    X = df[feature].values.reshape(-1, 1)
    y = df["Happiness"].values

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    ax.plot(df[feature], y_pred, color="red", linewidth=2, label="Linear Regression")
    ax.legend()

    ax.text(
        0.1,
        0.9,
        f"y = {model.coef_[0]:.4f}x + {model.intercept_:.4f}",
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top",
    )


# Read data from CSV file
try:
    df = pd.read_csv("simulated.csv")
except FileNotFoundError:
    print("Error: File not found. Make sure the file name is correct.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: File is empty.")
    exit()

# Menu
while True:
    print("\nChoose an option:")
    print("1. Sleep Regression")
    print("2. Light Regression")
    print("3. Stress Regression")
    print("4. All Regressions")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            plot_regression(df, "Sleep", "Sleep vs Happiness", plt.gca())
            plt.show()
        elif choice == 2:
            plot_regression(df, "Light", "Light vs Happiness", plt.gca())
            plt.show()
        elif choice == 3:
            plot_regression(df, "Stress", "Stress vs Happiness", plt.gca())
            plt.show()
        elif choice == 4:
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            plot_regression(df, "Sleep", "Sleep vs Happiness", axes[0])
            plot_regression(df, "Light", "Light vs Happiness", axes[1])
            plot_regression(df, "Stress", "Stress vs Happiness", axes[2])
            plt.tight_layout()
            plt.show()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
