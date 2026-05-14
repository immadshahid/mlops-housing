import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("models/model.pkl")

class InputData(BaseModel):
    features: list


@app.get("/")

def home():
    return {"message": "MLOps API running"}


@app.post("/predict")

def predict(data: InputData):

    prediction = model.predict([data.features])

    return {"Prediction": prediction[0]}

