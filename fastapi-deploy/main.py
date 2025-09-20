from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import joblib

# FastAPI instance
app = FastAPI()

# CORS allow (Android app connect kar sake)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Server start hote hi model load hoga
model = joblib.load("heart_failure_model.pkl")

@app.post("/predict")
async def predict_risk(
    age: int = Form(...),
    anaemia: int = Form(...),
    cpk: int = Form(...),
    diabetes: int = Form(...),
    ejection: int = Form(...),
    bp: int = Form(...),
    platelets: float = Form(...),
    sex: int = Form(...),
    creatinine: float = Form(...),
    sodium: int = Form(...),
    smoking: int = Form(...),
):
    # Features ko arrange karo
    features = [[
        age, anaemia, cpk, diabetes, ejection,
        bp, platelets, sex, creatinine, sodium, smoking
    ]]

    # Model se prediction lo
    prediction = model.predict(features)[0]

    return {"prediction": prediction}
