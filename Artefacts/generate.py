import numpy as np
import pandas as pd

# Generate hypothetical data
np.random.seed(42)

num_samples = 170
sleep = np.random.uniform(1, 10, num_samples)
light = np.random.uniform(1, 10, num_samples)
stress = np.random.uniform(1, 10, num_samples)
happiness = (
    5 + 0.6 * sleep + 0.5 * light - 0.3 * stress + np.random.normal(0, 1, num_samples)
)

# Convert happiness to percentage
happiness_percent = (happiness / 16) * 100

# Create a DataFrame
df = pd.DataFrame(
    {"Sleep": sleep, "Light": light, "Stress": stress, "Happiness": happiness_percent}
)

# Write data to CSV file
df.to_csv("simulated.csv", index=False)
print("Hypothetical data saved to simulated.csv")
