from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Extract features from request
    features = [
        float(data["area"]),
        int(data["bedrooms"]),
        int(data["bathrooms"]),
        int(data["stories"]),
        int(data["mainroad"]),
        int(data["guestroom"]),
        int(data["basement"]),
        int(data["hotwaterheating"]),
        int(data["airconditioning"]),
        int(data["parking"]),
        int(data["prefarea"]),
        int(data["furnishingstatus"])
    ]

    # Predict price
    prediction = model.predict(np.array([features]))[0]

    return jsonify({"predicted_price": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)
