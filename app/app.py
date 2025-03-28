from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
import tensorflow as tf
import xgboost as xgb

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load models
xgb_model = joblib.load("xgb_model.pkl")
lstm_model = tf.keras.models.load_model("lstm_model.h5")
gru_model = tf.keras.models.load_model("gru_model.h5")

models = {
    "xgboost": xgb_model,
    "lstm": lstm_model,
    "gru": gru_model
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        model_name = data.get("model")
        features = np.array(data.get("features"), dtype=np.float32).reshape(1, -1)

        if model_name not in models:
            return jsonify({"error": "Invalid model name"}), 400

        model = models[model_name]

        if model_name == "xgboost":
            prediction = model.predict(features)[0]
        else:
            # Reshape for LSTM & GRU
            prediction = model.predict(features.reshape(1, features.shape[1], 1))[0][0]

        return jsonify({"model": model_name, "power_prediction": float(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
