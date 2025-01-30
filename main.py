from fastapi import FastAPI, HTTPException, Header
import secrets
from transformers import pipeline
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Generate API token (store securely in .env file)
API_TOKEN = os.getenv("API_TOKEN") or secrets.token_hex(16)
print(f"Generated API Token: {API_TOKEN}")

# Initialize FastAPI
app = FastAPI()

# Load translation model (English → Spanish by default, change as needed)
translator = pipeline("translation_en_to_fr")  # French translation

@app.get("/")
def home():
    return {"message": "Welcome to the Translation API!"}

@app.post("/translate/")
def translate_text(text: str, authorization: str = Header(None)):
    # Check API token
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Invalid API Token")

    # Translate text
    translated_text = translator(text)[0]['translation_text']
    return {"original_text": text, "translated_text": translated_text}
