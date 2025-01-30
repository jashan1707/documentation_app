import requests
import os
from dotenv import load_dotenv

load_dotenv()
CONFLUENCE_URL = os.getenv("CONFLUENCE_URL")
CONFLUENCE_API_KEY = os.getenv("CONFLUENCE_API_KEY")

def upload_to_confluence(title, content):
    url = f"{CONFLUENCE_URL}/rest/api/content/"
    headers = {
        "Authorization": f"Bearer {CONFLUENCE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "title": title,
        "content": content
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.text