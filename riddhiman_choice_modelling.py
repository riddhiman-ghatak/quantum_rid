import numpy as np

def calculate(coefficients, data, utility_functions):
    """
    Calculate probabilities of each alternative using multinomial logit model.
    
    Args:
    - coefficients (dict): A dictionary containing the coefficients for the model.
    - data (dict): A dictionary containing the independent variables.
    - utility_functions (list): A list of functions defining the deterministic utilities for each alternative.
    
    Returns:
    - probabilities (dict): A dictionary containing calculated probabilities for each alternative.
    """
    # Extract coefficients
    beta_0_1 = coefficients.get('beta_0_1')
    beta_1 = coefficients.get('beta_1')
    beta_2 = coefficients.get('beta_2')
    beta_0_2 = coefficients.get('beta_0_2')
    beta_0_3 = coefficients.get('beta_0_3')
    beta_s1_13 = coefficients.get('beta_s1_13')
    beta_s1_23 = coefficients.get('beta_s1_23')
    
    # Extract data
    feature_x1 = data.get('feature_x1')
    feature_x2 = data.get('feature_x2')
    feature_sero = data.get('feature_sero')
    feature_s1 = data.get('feature_s1')
    indicator_av1 = data.get('indicator_av1')
    indicator_av2 = data.get('indicator_av2')
    indicator_av3 = data.get('indicator_av3')
    
    # Error handling for mismatched dimensions
    data_dimensions = [len(x) for x in [feature_x1, feature_x2, feature_sero, feature_s1, indicator_av1, indicator_av2, indicator_av3]]
    if len(set(data_dimensions)) != 1:
        raise ValueError("Mismatched dimensions between data points.")
    
    probabilities = {}
    
    # Define utility functions
    utility_1 = lambda x1, s1: beta_0_1 + beta_1 * x1 + beta_s1_13 * s1
    utility_2 = lambda x2, s1: beta_0_2 + beta_2 * x2 + beta_s1_23 * s1
    utility_3 = lambda sero: beta_0_3
    
    # Calculate probabilities for each alternative
    for i in range(len(feature_sero)):
        exp_utility_1 = indicator_av1[i] * np.exp(utility_1(feature_x1[i], feature_s1[i]))
        exp_utility_2 = indicator_av2[i] * np.exp(utility_2(feature_x2[i], feature_s1[i]))
        exp_utility_3 = indicator_av3[i] * np.exp(utility_3(feature_sero[i]))
        denominator = exp_utility_1 + exp_utility_2 + exp_utility_3
        probability_1 = exp_utility_1 / denominator
        probability_2 = exp_utility_2 / denominator
        probability_3 = exp_utility_3 / denominator
        probabilities[i+1] = [probability_1, probability_2, probability_3]
    
    return probabilities

# Sample Data
coefficients = {
    'beta_0_1': 0.1, 'beta_1': -0.5, 'beta_2': -0.4, 'beta_0_2': 1, 'beta_0_3': 0, 'beta_s1_13': 0.33, 'beta_s1_23': 0.58
}

data = {
    'feature_x1': [2,1,3,4,2,1,8,7,3,2],
    'feature_x2': [8,7,4,1,4,7,2,2,3,1],
    'feature_sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'feature_s1': [3,8,4,7,1,6,5,9,2,3],
    'indicator_av1': [1,1,1,1,1,0,0,1,1,0],
    'indicator_av2': [1,1,1,0,0,1,1,1,0,1],
    'indicator_av3': [1,1,0,0,1,1,1,1,1,1]
}

utility_functions = [None, None, None]  # Assuming deterministic utilities are defined elsewhere

# Calculate probabilities
probabilities = calculate(coefficients, data, utility_functions)

# Writing probabilities to a .txt file
with open("riddhiman_probability.txt", "w") as file:
    for key, value in probabilities.items():
        file.write(f"Alternative {key}: {value}\n")
