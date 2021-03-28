from flask import Flask, jsonify, request
from typing import Literal
from sklearn.ensemble import RandomForestClassifier
from data_preprocessor import text_preprocessing
import joblib
app = Flask(__name__)

def predict(trial_obs: str):
    """
    Function that should take in the description text and return the prediction
    for the class that we identify it to.
    The possible classes are: ['Dementia', 'ALS',
    'Obsessive Compulsive Disorder',
    'Scoliosis', 'Parkinson's Disease']
    """
    trial_obs = text_preprocessing(trial_obs)
    trial_obs = ' '.join(trial_obs)
    loaded_model = joblib.load("randomforest.pkl")
    pred_obs = loaded_model.predict([trial_obs])
    trial_dict = {
    0: "ALS",
    1: "Dementia",
    2: "Obsessive Compulsive Disorder",
    3: "Scoliosis",
    4: "Parkinson's Disease"
    }
    return trial_dict[pred_obs[0]]
    
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/predict", methods=["POST"])
def identify_condition():
    data = request.get_json(force=True)

    prediction = predict(data["description"])
    return jsonify({"prediction": prediction})
if __name__ == "__main__":
    app.run()