import os
import json
import requests

def summarize_text(text):
    # Prepare the data for the POST request
    data = {
        "inputs": text,
        "parameters": {
            "max_length": 100,
            "min_length": 30
        }
    }

    # Configure the request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("access_token")}'
    }

    # Make the POST request to the Hugging Face API
    try:
        response = requests.post('https://api-inference.huggingface.co/models/facebook/bart-large-cnn',
                                 headers=headers,
                                 data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for HTTP errors
        summary_text = response.json()[0]['summary_text']
        return summary_text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
