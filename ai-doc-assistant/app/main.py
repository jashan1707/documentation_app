from fastapi import FastAPI
from app.screen_monitor import ScreenMonitor  # Updated to match the folder structure
from pydantic import BaseModel
import json

app = FastAPI()

monitor = ScreenMonitor()

class DocumentationRequest(BaseModel):
    title: str
    content: str

@app.post("/generate")
async def generate_documentation():
    # Capture activity (simulate AI processing)
    monitor.capture_activity()

    # Simple documentation generation (this would normally be AI-driven)
    documentation = "Generated documentation based on user activity."

    # Return generated documentation
    return {"documentation": documentation}

@app.post("/upload")
async def upload_documentation(doc: DocumentationRequest):
    # In a real app, you would connect to Confluence API here
    print(f"Uploading doc: {doc.title}")
    
    # For now, just return a success message
    return {"message": f"Documentation titled '{doc.title}' has been uploaded successfully!"}

@app.get("/activity")
async def get_activity():
    # Return captured activities
    return monitor.get_activity()