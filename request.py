import requests

API_URL = "http://127.0.0.1:8000/translate/"
API_TOKEN = "replace-with-your-api-token"

headers = {"Authorization": f"Bearer {API_TOKEN}"}
data = {"text": "Hello, how are you?"}

response = requests.post(API_URL, headers=headers, params=data)
print(response.json())  # Output: {"original_text": "Hello, how are you?", "translated_text": "Bonjour, comment ça va?"}
