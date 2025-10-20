import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

# Read data from CSV file
try:
    df = pd.read_csv("simulated.csv")
except FileNotFoundError:
    print("Error: File not found. Make sure the file name is correct.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: File is empty.")
    exit()

# Linear regression models
model_sleep = LinearRegression()
model_light = LinearRegression()
model_stress = LinearRegression()

# Fit the models
model_sleep.fit(df[["Sleep"]], df["Happiness"])
model_light.fit(df[["Light"]], df["Happiness"])
model_stress.fit(df[["Stress"]], df["Happiness"])


# Equations for the regression planes
def sleep_plane(sleep):
    return model_sleep.coef_[0] * sleep + model_sleep.intercept_


def light_plane(light):
    return model_light.coef_[0] * light + model_light.intercept_


def stress_plane(stress):
    return model_stress.coef_[0] * stress + model_stress.intercept_


def sleep_light_plane(sleep, light):
    return (
        model_sleep.coef_[0] * sleep
        + model_light.coef_[0] * light
        + model_sleep.intercept_
    )


def sleep_stress_plane(sleep, stress):
    return (
        model_sleep.coef_[0] * sleep
        + model_stress.coef_[0] * stress
        + model_sleep.intercept_
    )


def light_stress_plane(light, stress):
    return (
        model_light.coef_[0] * light
        + model_stress.coef_[0] * stress
        + model_stress.intercept_
    )


def plot_3d_graph(x, y, z, xlabel, ylabel, zlabel, title, colour, plot_plane=True):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, c=colour, marker="o", label="Actual Data")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)

    if plot_plane:
        # Plot regression plane
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        x_surf, y_surf = np.meshgrid(
            np.linspace(xlim[0], xlim[1], 100), np.linspace(ylim[0], ylim[1], 100)
        )
        if xlabel == "Sleep":
            z_surf = sleep_plane(x_surf)
        elif xlabel == "Light":
            z_surf = light_plane(x_surf)
        elif xlabel == "Stress":
            z_surf = stress_plane(x_surf)
        ax.plot_surface(x_surf, y_surf, z_surf, alpha=0.3, color="cyan")

    plt.show()


# Menu options
while True:
    print("\nChoose an option:")
    print("1. 3D Sleep")
    print("2. 3D Light")
    print("3. 3D Stress")
    print("4. All 3D Graphs Together")
    print("5. 3D Graphs for All Combinations of 2 Factors")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
        if choice == 1:
            plot_3d_graph(
                df["Sleep"],
                df["Light"],
                df["Happiness"],
                "Sleep",
                "Light",
                "Happiness (%)",
                "3D Sleep & Light",
                "Blue",
            )
        elif choice == 2:
            plot_3d_graph(
                df["Light"],
                df["Stress"],
                df["Happiness"],
                "Light",
                "Stress",
                "Happiness (%)",
                "3D Light & Stress",
                "Green",
            )
        elif choice == 3:
            plot_3d_graph(
                df["Stress"],
                df["Sleep"],
                df["Happiness"],
                "Stress",
                "Sleep",
                "Happiness (%)",
                "3D Stress & Sleep",
                "Red",
            )
        # Option 4: All 3D Graphs Together
        elif choice == 4:
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection="3d")

            # Scatter plots for each factor
            ax.scatter(
                df["Sleep"],
                df["Light"],
                df["Happiness"],
                c="blue",
                marker="o",
                label="Sleep vs Light",
            )
            ax.scatter(
                df["Sleep"],
                df["Stress"],
                df["Happiness"],
                c="green",
                marker="o",
                label="Sleep vs Stress",
            )
            ax.scatter(
                df["Light"],
                df["Stress"],
                df["Happiness"],
                c="red",
                marker="o",
                label="Light vs Stress",
            )

            # Plotting regression planes
            sleep_vals = np.linspace(min(df["Sleep"]), max(df["Sleep"]), 100)
            light_vals = np.linspace(min(df["Light"]), max(df["Light"]), 100)
            stress_vals = np.linspace(min(df["Stress"]), max(df["Stress"]), 100)

            sleep_plane_vals, light_plane_vals = np.meshgrid(sleep_vals, light_vals)
            happiness_plane_vals = sleep_light_plane(sleep_plane_vals, light_plane_vals)
            ax.plot_surface(
                sleep_plane_vals,
                light_plane_vals,
                happiness_plane_vals,
                alpha=0.3,
                color="cyan",
                label="Sleep vs Light Plane",
            )

            sleep_plane_vals, stress_plane_vals = np.meshgrid(sleep_vals, stress_vals)
            happiness_plane_vals = sleep_stress_plane(
                sleep_plane_vals, stress_plane_vals
            )
            ax.plot_surface(
                sleep_plane_vals,
                stress_plane_vals,
                happiness_plane_vals,
                alpha=0.3,
                color="lime",
                label="Sleep vs Stress Plane",
            )

            light_plane_vals, stress_plane_vals = np.meshgrid(light_vals, stress_vals)
            happiness_plane_vals = light_stress_plane(
                light_plane_vals, stress_plane_vals
            )
            ax.plot_surface(
                light_plane_vals,
                stress_plane_vals,
                happiness_plane_vals,
                alpha=0.3,
                color="pink",
                label="Light vs Stress Plane",
            )

            ax.set_xlabel("Sleep")
            ax.set_ylabel("Light / Stress")
            ax.set_zlabel("Happiness (%)")
            ax.set_title("All 3D Graphs Together")
            ax.legend()
            plt.show()
        elif choice == 5:
            fig, axes = plt.subplots(1, 3, figsize=(20, 6))

            # Sleep vs Light
            ax1 = fig.add_subplot(131, projection="3d")
            ax1.scatter(
                df["Sleep"],
                df["Light"],
                df["Happiness"],
                c="blue",
                marker="o",
                label="Sleep vs Light",
            )
            ax1.set_xlabel("Sleep")
            ax1.set_ylabel("Light")
            ax1.set_zlabel("Happiness (%)")
            ax1.set_title("Sleep vs Light")

            # Sleep vs Stress
            ax2 = fig.add_subplot(132, projection="3d")
            ax2.scatter(
                df["Sleep"],
                df["Stress"],
                df["Happiness"],
                c="green",
                marker="o",
                label="Sleep vs Stress",
            )
            ax2.set_xlabel("Sleep")
            ax2.set_ylabel("Stress")
            ax2.set_zlabel("Happiness (%)")
            ax2.set_title("Sleep vs Stress")

            # Light vs Stress
            ax3 = fig.add_subplot(133, projection="3d")
            ax3.scatter(
                df["Light"],
                df["Stress"],
                df["Happiness"],
                c="red",
                marker="o",
                label="Light vs Stress",
            )
            ax3.set_xlabel("Light")
            ax3.set_ylabel("Stress")
            ax3.set_zlabel("Happiness (%)")
            ax3.set_title("Light vs Stress")

            plt.tight_layout()
            plt.show()

        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
