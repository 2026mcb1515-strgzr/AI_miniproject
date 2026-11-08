import joblib
import pandas as pd

# Load trained model and test data
data = joblib.load("outputs/titanic_model.pkl")

model = data["model"]
X_test = data["X_test"]

# Select one sample passenger
sample_passenger = X_test.iloc[[0]]

# Predict survival
prediction = model.predict(sample_passenger)

print("Passenger Details:")
print(sample_passenger)

if prediction[0] == 1:
    print("Prediction: Survived")
else:
    print("Prediction: Did Not Survive")
