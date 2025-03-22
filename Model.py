import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("Housing.csv")

# Convert categorical features ('yes'/'no') to numeric (1/0)
binary_columns = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea"]
for col in binary_columns:
    data[col] = data[col].map({"yes": 1, "no": 0})

# Convert 'furnishingstatus' to numeric values
data["furnishingstatus"] = data["furnishingstatus"].map({"unfurnished": 0, "semi-furnished": 1, "furnished": 2})

# Select features and target variable
X = data.drop(columns=["price"])  # Features
y = data["price"]  # Target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model as a .pkl file
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model training complete! 'house_price_model.pkl' saved.")
