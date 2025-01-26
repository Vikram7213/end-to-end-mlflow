from flask import Flask, render_template, request, jsonify
from ml_project.pipeline.prediction import PredictionPipeline
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def pred():
    try:
        data = request.get_json()

        # Validate input keys and handle missing keys with default values
        features = [
            float(data.get("fixed acidity", 0.0)),
            float(data.get("volatile acidity", 0.0)),
            float(data.get("citric acid", 0.0)),
            float(data.get("residual sugar", 0.0)),
            float(data.get("chlorides", 0.0)),
            float(data.get("free sulfur dioxide", 0.0)),
            float(data.get("total sulfur dioxide", 0.0)),
            float(data.get("density", 0.0)),
            float(data.get("pH", 0.0)),
            float(data.get("sulphates", 0.0)),
            float(data.get("alcohol", 0.0)),
        ]

        # Prepare input features for prediction
        input_features = np.array([features])
        model = PredictionPipeline()

        # Perform prediction
        prediction = model.predict(input_features)[0]

        return jsonify({"quality": int(prediction)})
    except KeyError as e:
        # Handle missing keys
        return jsonify({"error": f"Missing key in request data: {str(e)}"}), 400
    except ValueError:
        # Handle incorrect data types
        return jsonify({"error": "Invalid input type; please send numeric values."}), 400
    except Exception as e:
        # General exception handler
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
