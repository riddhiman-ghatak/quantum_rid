import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Generate some synthetic data
np.random.seed(0)
X = np.random.rand(100, 1) * 10  # 100 samples, 1 feature
y = 0.5 * X**2 - 2*X + 3 + np.random.randn(100)  # Quadratic relationship with noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transform features to polynomial features
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Create an XGBoost regressor
model = xgb.XGBRegressor(objective='reg:squarederror')

# Fit the model to the training data
model.fit(X_train_poly, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test_poly)

# Calculate the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Plot the actual vs. predicted values
plt.scatter(X_test, y_test, label='Actual')
plt.scatter(X_test, y_pred, color='r', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Actual vs. Predicted values')
plt.legend()
plt.show()
