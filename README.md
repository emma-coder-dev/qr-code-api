# QR Code Generator API

A beginner-friendly REST API built with FastAPI that generates scannable QR codes from any text or URL.

---

## 🎯 Objective

The goal of this project is to learn and demonstrate FastAPI — a modern, high-performance Python web framework — by building a minimal but functional QR Code Generator API.

---

## ⚡ Quick Summary of FastAPI

FastAPI is a modern Python web framework used for building APIs quickly and efficiently. It is widely used in backend development, microservices, and data science applications. For example, companies like Uber and Netflix use similar API-first architectures in production.

---

## 🖥️ System Requirements

- OS: Windows / Mac / Linux
- Python 3.10+
- pip
- VS Code (recommended)

---

## 📦 Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/Emma-coder-dev/qr-code-api.git
cd qr-code-api
```

**2. Install dependencies**

```bash
pip install fastapi uvicorn qrcode[pil]
```

**3. Run the server**

```bash
uvicorn main:app --reload
```

**4. Open the API docs**

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Minimal Working Example

### Endpoints

| Method | Endpoint    | Description                        |
|--------|-------------|------------------------------------|
| GET    | `/health`   | Check if API is running            |
| POST   | `/generate` | Generate a QR code from text or URL |

### Generate a QR Code

**Request:**

```json
POST /generate
{
  "text": "https://github.com/Emma-coder-dev"
}
```

**Response:** Returns a `.png` QR code image file that can be scanned with any phone camera.

### Health Check

**Request:**

```
GET /health
```

**Response:**

```json
{
  "status": "API is running"
}
```

---

## 🧠 AI Prompt Journal

### Prompt 1

**Prompt used:** "What is FastAPI and how is it different from regular Python?"

**AI response summary:** FastAPI is a web framework that lets you build APIs using Python. Unlike writing plain Python scripts, FastAPI handles HTTP requests, automatic documentation, and data validation out of the box.

**Evaluation:** This was helpful as a starting point. It gave me a clear mental model before touching any code.

---

### Prompt 2

**Prompt used:** "Give me a step by step guide to install FastAPI and run a basic server"

**AI response summary:** The AI walked me through installing fastapi and uvicorn via pip, creating a main.py file with a basic app instance, and running it with `uvicorn main:app --reload`.

**Evaluation:** Very useful. I had the server running within minutes. The `--reload` flag explanation was especially helpful for development.

---

### Prompt 3

**Prompt used:** "How do I return an image file as a response in FastAPI?"

**AI response summary:** The AI introduced `FileResponse` from `fastapi.responses`, which allows returning files directly from an endpoint. It showed how to save the file locally first then return it.

**Evaluation:** This solved my biggest question. Without this I would not have known how to return the QR image instead of just a JSON response.

---

### Prompt 4

**Prompt used:** "How do I use the qrcode library in Python to generate and save a QR code image?"

**AI response summary:** The AI showed that `qrcode.make(text)` generates a QR code object and calling `.save(filename)` writes it as a PNG file. It also mentioned installing `qrcode[pil]` for image support.

**Evaluation:** Straightforward and accurate. The `pil` dependency note saved me from an installation error.

---

## 🐛 Common Issues & Fixes

**Issue 1: `ModuleNotFoundError: No module named 'qrcode'`**

```
Fix: pip install qrcode[pil]
Make sure to include [pil] — without it the image generation fails.
```

**Issue 2: `ModuleNotFoundError: No module named 'pydantic'`**

```
Fix: pip install pydantic
FastAPI depends on pydantic for request validation.
```

**Issue 3: Port already in use**

```
Fix: uvicorn main:app --reload --port 8001
Change the port number if 8000 is already occupied.
```

**Issue 4: Browser opens URL instead of downloading image**

```
This is normal browser behavior for image responses.
The QR code is still generated correctly — check your project
folder for qrcode_output.png and scan it with your phone.
```

---

## 📚 References

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [qrcode Library on PyPI](https://pypi.org/project/qrcode/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [FastAPI Tutorial - FreeCodeCamp YouTube](https://www.youtube.com/watch?v=0sOvCWFmrtA)