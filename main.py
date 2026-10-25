from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train the model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Make a prediction
flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(flower)

print("Predicted flower:", iris.target_names[prediction[0]])
