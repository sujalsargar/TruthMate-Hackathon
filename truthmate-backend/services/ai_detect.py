import requests
import os

HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')

def detect_ai_generated(content):
    """Use Hugging Face API to detect AI-generated content"""
    try:
        API_URL = "https://api-inference.huggingface.co/models/roberta-base-openai-detector"
        
        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
        }
        
        payload = {
            "inputs": content[:2000]
        }
        
        response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        data = response.json()
        
        # Parse response
        if isinstance(data, list) and len(data) > 0:
            result = data[0]
            ai_probability = 0
            for item in result:
                if item.get('label') == 'Fake':
                    ai_probability = item.get('score', 0) * 100
                    break
            return ai_probability
        
        return 15
        
    except Exception as e:
        return 0