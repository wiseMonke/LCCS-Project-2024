import csv
import matplotlib.pyplot as plt


def read_data_from_csv(filename):
    data = {"Stress": [], "Light": [], "Sleep": [], "Happiness": []}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            happiness, stress, light, sleep = map(float, row[1:])
            data["Happiness"].append(happiness)
            data["Stress"].append(stress)
            data["Light"].append(light)
            data["Sleep"].append(sleep)
    return data


def create_bar_graph(data, factor):
    data_labels = list(range(1, len(data[factor]) + 1))
    data_values = data[factor]

    colors = ["b"] * (len(data_values) - 1) + ["r"]
    bars = plt.bar(range(len(data_values)), data_values, color=colors)

    max_value = max(data_values)
    max_indices = [i for i, value in enumerate(data_values) if value == max_value]
    max_recent_index = max(max_indices)
    bars[max_recent_index].set_color("g")

    min_value = min(data_values)
    min_indices = [i for i, value in enumerate(data_values) if value == min_value]
    min_recent_index = max(min_indices)
    bars[min_recent_index].set_color("y")

    plt.ylabel(factor)
    plt.title(f"{factor} Values")
    plt.xticks(range(len(data_labels)), data_labels, rotation=45, ha="right")
    plt.legend(
        [bars[0], bars[-1], bars[max_recent_index], bars[min_recent_index]],
        [
            "Previous Data Points",
            "Most Recent Data Point",
            "Highest Data Point",
            "Lowest Data Point",
        ],
        loc="upper left",
    )
    plt.show()


def overlay_happiness_with_factors(data):
    index = list(range(1, len(data["Happiness"]) + 1))
    bar_width = 0.2
    opacity = 0.7
    offset = bar_width * 1.5

    for i, factor in enumerate(["Stress", "Light", "Sleep"]):
        plt.bar(
            [x + (i * offset) for x in index],
            data[factor],
            bar_width,
            alpha=opacity,
            label=factor,
        )

    plt.plot(index, data["Happiness"], marker="o", color="b", label="Happiness")

    plt.ylabel("Value")
    plt.title("Factors vs Happiness")
    plt.xticks([x + (offset / 2) for x in index], index)
    plt.legend()
    plt.show()


def get_user_choice():
    print("\nSelect an option:")
    print("1. Show Happiness graph")
    print("2. Show Stress graph")
    print("3. Show Light graph")
    print("4. Show Sleep graph")
    print("5. Show Happiness overlay with factors")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    filename = "data.csv"
    data = read_data_from_csv(filename)

    while True:
        print("\n===============================")
        choice = get_user_choice()

        if choice == "1":
            create_bar_graph(data, "Happiness")
        elif choice == "2":
            create_bar_graph(data, "Stress")
        elif choice == "3":
            create_bar_graph(data, "Light")
        elif choice == "4":
            create_bar_graph(data, "Sleep")
        elif choice == "5":
            overlay_happiness_with_factors(data)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
