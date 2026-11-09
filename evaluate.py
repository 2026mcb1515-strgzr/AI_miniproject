import joblib
import os
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# Load the trained model and test data
data = joblib.load("outputs/titanic_model.pkl")

model = data["model"]
X_test = data["X_test"]
y_test = data["y_test"]

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Calculate confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:",cm)

os.makedirs("outputs", exist_ok=True)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Not Survived", "Survived"]
)

disp.plot()
plt.title("Titanic Survival Confusion Matrix")
plt.savefig("outputs/confusion_matrix.png")
plt.close()

print("Plot saved successfully!")
