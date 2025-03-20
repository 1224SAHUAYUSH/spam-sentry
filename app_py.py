# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W9TEbbfbpaldhnONKcoRTP8v99mlWV5b
"""

from flask import Flask, request, jsonify
import pickle
import numpy as np
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "IMDB Sentiment Analysis API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["text"]
    prediction = model.predict([data])[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)