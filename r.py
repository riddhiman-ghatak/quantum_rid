import pandas as pd
import numpy as np

# Load the provided seed dataset
seed_data = pd.read_csv("Data.csv")

# Initialize counts for each category
population_counts = {
    'sex': {'Male': 0, 'Female': 0},
    'age_group': {'Below 22 years': 0, '22-60 years': 0, 'Above 60 years': 0},
    'highest_education_level': {'No formal education': 0, 'Primary education': 0,
                                'Secondary education': 0, 'Graduation and above': 0}
}

# Define the target population size
target_population_size = 50000

# Initialize empty lists to store synthesized individuals
synthesized_data = []

# Repeat until the desired population size is reached
while len(synthesized_data) < target_population_size:
    # Sample randomly from the seed dataset
    sampled_individual = seed_data.sample(n=1, replace=True).iloc[0]

    # Update counts based on the sampled individual
    population_counts['sex'][sampled_individual['Sex']] += 1
    population_counts['age_group'][sampled_individual['Age_group']] += 1
    population_counts['highest_education_level'][sampled_individual['Highest_education_level']] += 1

    # Append the sampled individual to the synthesized data
    synthesized_data.append(sampled_individual)

# Adjust the synthesized data to match the desired population characteristics
# This could involve oversampling or undersampling certain categories.

# Convert synthesized data to DataFrame
synthesized_data = pd.DataFrame(synthesized_data)

# Print the frequency of every class
print("Frequency of every class:")
for category, counts in population_counts.items():
    print(f"{category}:")
    for class_name, count in counts.items():
        print(f" - {class_name}: {count}")

# Check if the synthesized data matches the desired population characteristics
# (Optional step)

# Save the synthesized data to a CSV file
synthesized_data.to_csv("Synthesized_population.csv", index=False)
