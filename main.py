from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import qrcode

# Initialize the FastAPI application
# title, description and version are displayed in the auto-generated /docs page
app = FastAPI(
    title="QR Code Generator API",
    description="A simple API to generate scannable QR codes from any text or URL",
    version="1.0.0"
)

# Define the request body structure using Pydantic BaseModel
# FastAPI uses this to validate incoming JSON automatically
# The request must contain a "text" field of type string
class QRRequest(BaseModel):
    text: str

# GET endpoint at /health
# Used to verify the API is running without performing any heavy operations
# Returns a simple JSON response confirming the API status
@app.get("/health")
def health_check():
    return {"status": "API is running"}

# POST endpoint at /generate
# Accepts a QRRequest body, validates it, generates a QR code and returns it as a PNG image
@app.post("/generate")
def generate_qr(request: QRRequest):
    
    # Validate that the text field is not empty or just whitespace
    # If it is, raise a 400 Bad Request error with a descriptive message
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty. Please provide a URL or text to encode."
        )
    
    # Generate the QR code image from the provided text
    # qrcode.make() handles all encoding internally
    qr = qrcode.make(request.text)
    
    # Save the generated QR code as a PNG file in the current directory
    file_path = "qrcode_output.png"
    qr.save(file_path)
    
    # Return the PNG file as the HTTP response
    # media_type tells the client this is an image
    # filename sets the name of the downloaded file
    return FileResponse(
        file_path,
        media_type="image/png",
        filename="qrcode.png"
    )