from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

# Gemini API key set karo
genai.configure(api_key="AIzaSyBj5cn7xliPYpmgQt1ZKUHm51gJW0_cPTU")

# Model choose karo
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# FastAPI instance
app = FastAPI()

# CORS allow karo takay Android app access kar sake
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Android app ke liye allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict_risk(
    age: str = Form(...),
    anaemia: str = Form(...),
    cpk: str = Form(...),
    diabetes: str = Form(...),
    ejection: str = Form(...),
    bp: str = Form(...),
    platelets: str = Form(...),
    sex: str = Form(...),
    creatinine: str = Form(...),
    sodium: str = Form(...),
    smoking: str = Form(...),
):
    prompt = f"""
    Predict heart failure risk level based on the following patient information:

    - Age: {age}
    - Anaemia: {anaemia}
    - Creatinine Phosphokinase: {cpk} mcg/L
    - Diabetes: {diabetes}
    - Ejection Fraction: {ejection}%
    - High Blood Pressure: {bp}
    - Platelets: {platelets} kiloplatelets/mL
    - Sex: {sex}
    - Serum Creatinine: {creatinine} mg/dL
    - Serum Sodium: {sodium} mEq/L
    - Smoking: {smoking}

    Only respond with: High Risk / Moderate Risk / Low Risk.
    Do not provide any tips, explanation, or additional notes.
    """
    
    response = model.generate_content(prompt)
    result = response.text.strip()
    return {"prediction": result}
