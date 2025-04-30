import requests
import os


class LLM:
    def __init__(self, api_key: str, model_name: str = "models/gemini-1.5-flash"):
        self.api_key = api_key
        self.model_name = model_name
        self.url = f"https://generativelanguage.googleapis.com/v1beta/{self.model_name}:generateContent?key={self.api_key}"

    def generate_response(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
        }
        
        body = {
        "contents": [{
        "parts":[{"text": prompt}]
         }]
        }

        try:
            response = requests.post(self.url, headers=headers, json=body)
            response.raise_for_status()  
            data = response.json()

            return data["candidates"][0]["content"]["parts"][0]["text"]
        
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] API request failed: {e}")
            return "Sorry, I couldn't generate a response."
