# Step 1: Problem Definition
# Example: Predicting house prices (Regression Problem)

"""
Problem Statement:
- Objective: Predict house prices based on features like size, location, etc.
- Type: Regression problem (continuous output)
- Success Metrics: 
    - Mean Absolute Error (MAE)
    - Root Mean Squared Error (RMSE)
    - R-squared Score
"""

# Project Configuration
PROJECT_NAME = "House Price Prediction"
PROJECT_TYPE = "Regression"
TARGET_VARIABLE = "price"
METRICS = ["mae", "rmse", "r2_score"]

# Define expected features
FEATURES = [
    "square_feet",
    "num_bedrooms",
    "num_bathrooms",
    "location",
    "year_built"
]

if __name__ == "__main__":
    print(f"Project: {PROJECT_NAME}")
    print(f"Type: {PROJECT_TYPE}")
    print(f"Target Variable: {TARGET_VARIABLE}")
    print("Features:", FEATURES)