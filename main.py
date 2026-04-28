from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import qrcode
import os

# Initialize FastAPI app
app = FastAPI(
    title="QR Code Generator API",
    description="A simple API to generate scannable QR codes from text or URLs",
    version="1.0.0"
)

# Define request body structure
class QRRequest(BaseModel):
    text: str

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "API is running"}

# QR code generator endpoint
@app.post("/generate")
def generate_qr(request: QRRequest):
    # Generate QR code
    qr = qrcode.make(request.text)
    
    # Save the image
    file_path = "qrcode_output.png"
    qr.save(file_path)
    
    # Return the image file
    return FileResponse(file_path, media_type="image/png", filename="qrcode.png")