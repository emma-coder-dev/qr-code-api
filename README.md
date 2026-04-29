# 🔳 QR Code Generator API
### Prompt-Powered Kickstart: Building a Beginner's Toolkit for FastAPI

A beginner-friendly REST API built with **FastAPI** that generates real, scannable QR codes from any text or URL. Built as part of the Moringa AI Capstone Project.

---

## 🎯 Title & Objective

**Project Title:** Getting Started with FastAPI – A Beginner's Guide to Building a QR Code Generator API

**Technology chosen:** FastAPI (Python web framework)

**Why FastAPI?**
FastAPI was chosen because it is one of the fastest-growing Python frameworks in the industry, used heavily in backend development, cloud services, and microservices architecture. It is beginner-friendly yet production-ready, making it the perfect technology to learn as a first framework. It also generates automatic interactive API documentation out of the box — meaning you can test your API without writing a single line of frontend code.

**End goal:** Build a working REST API that accepts any text or URL and returns a real scannable QR code image as output.

---

## ⚡ Quick Summary of FastAPI

**What is it?**
FastAPI is a modern, high-performance Python web framework for building APIs. It is built on top of Starlette (for web handling) and Pydantic (for data validation). It was created by Sebastián Ramírez and first released in 2018.

**Where is it used?**
FastAPI is used in backend development, data science APIs, microservices, cloud-native applications, and machine learning model serving. It is one of the most downloaded Python packages on PyPI.

**Key features:**
- Automatic interactive API docs (Swagger UI at `/docs`)
- Built-in data validation using Pydantic
- Asynchronous support out of the box
- Very fast — comparable to Node.js and Go in benchmarks
- Minimal boilerplate code

**Real-world example:**
Microsoft uses FastAPI internally for some of their machine learning services. Many startups and data teams use it to expose ML models as APIs that frontend apps or mobile apps can consume.

**FastAPI vs Flask (Quick Comparison):**

| Feature | FastAPI | Flask |
|---------|---------|-------|
| Auto docs | ✅ Built-in Swagger UI | ❌ Needs extension |
| Data validation | ✅ Pydantic built-in | ❌ Manual |
| Performance | ⚡ Very fast (async) | 🐢 Slower (sync) |
| Learning curve | Easy | Easy |
| Best for | APIs, microservices | Web apps, simple APIs |

---

## 🖥️ System Requirements

- **OS:** Windows / Mac / Linux
- **Python:** 3.10 or higher
- **pip:** Latest version
- **Editor:** VS Code (recommended)
- **Packages:** fastapi, uvicorn, qrcode[pil]

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

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

**3. Run the server**

```bash
uvicorn main:app --reload
```

**4. Open the interactive API docs**

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Minimal Working Example

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Check if API is running |
| POST | `/generate` | Generate a QR code from text or URL |

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

## 🖥️ How to Use the Swagger UI at /docs

When you run the server and open `http://127.0.0.1:8000/docs` in your browser, FastAPI automatically shows an interactive page called **Swagger UI**. This page lets you test your API directly from the browser without needing any extra tools like Postman.

Here is what you will see and how to use it:

---

### What the /docs page shows

At the top you will see the API name, version, and description:
```
QR Code Generator API  1.0.0
A simple API to generate scannable QR codes from any text or URL
```

Below that, you will see two endpoints listed:

```
GET   /health     Health Check
POST  /generate   Generate Qr
```

Each endpoint shows its HTTP method (GET or POST) and a short description.

---

### How to test the GET /health endpoint

The health endpoint checks that your API is running. Here is how to use it:

1. Click on **GET /health** to expand it
2. Click the **Try it out** button on the right
3. Click the blue **Execute** button
4. Scroll down to see the **Response body**

You should see:
```json
{
  "status": "API is running"
}
```

A **200** response code means the request was successful and the API is working.

---

### How to test the POST /generate endpoint

The generate endpoint creates a QR code from whatever text or URL you send. Here is how to use it:

1. Click on **POST /generate** to expand it
2. Click the **Try it out** button
3. You will see a **Request body** text box with this default content:
```json
{
  "text": "string"
}
```
4. Replace `"string"` with whatever you want to encode. See examples below.
5. Click the blue **Execute** button
6. Scroll down — under **Response body** you will see a **Download file** link
7. Click it to download the QR code image
8. Open the image and scan it with your phone camera

---

### What you can encode — Examples

**A website URL:**
```json
{
  "text": "https://github.com/Emma-coder-dev"
}
```
Scanning opens the URL in the phone browser.

---

**Plain text:**
```json
{
  "text": "Hello Moringa School"
}
```
Scanning displays the text on the phone screen.

---

**An email address:**
```json
{
  "text": "mailto:kagenineema@gmail.com"
}
```
Scanning prompts the phone to open the email app with the address pre-filled.

---

**A phone number:**
```json
{
  "text": "tel:+254700000000"
}
```
Scanning prompts the phone to dial the number.

---

**WiFi credentials:**
```json
{
  "text": "WIFI:S:NetworkName;T:WPA;P:yourpassword;;"
}
```
Scanning prompts the phone to connect to the WiFi network automatically.

---

**A vCard (contact information):**
```json
{
  "text": "BEGIN:VCARD\nVERSION:3.0\nFN:Neema Kageni\nTEL:+254700000000\nEMAIL:kagenineema@gmail.com\nEND:VCARD"
}
```
Scanning prompts the phone to save the contact.

---

### Reading the response codes

After executing a request, Swagger UI shows a **Code** field under the response. Here is what each code means:

| Code | Meaning |
|------|---------|
| 200 | Success — request worked correctly |
| 400 | Bad Request — you sent invalid data (e.g. empty text) |
| 422 | Unprocessable Entity — request body format is wrong |
| 500 | Server Error — something went wrong on the API side |

---

### What happens if you send empty text

If you send an empty string:
```json
{
  "text": ""
}
```

The API returns a **400 Bad Request** error:
```json
{
  "detail": "Text cannot be empty. Please provide a URL or text to encode."
}
```

This is intentional — empty input produces a blank QR code that cannot be scanned.

---

## 🧪 Testing & Iteration

All testing was done using the built-in FastAPI Swagger UI at `http://127.0.0.1:8000/docs`.

| # | Input | Endpoint | Result |
|---|-------|----------|--------|
| 1 | GET `/health` | `/health` | ✅ `{"status": "API is running"}` |
| 2 | `{"text": "https://github.com"}` | `/generate` | ✅ QR generated, scanned, opened GitHub |
| 3 | `{"text": "Hello Moringa School"}` | `/generate` | ✅ QR generated, scanned, showed text |
| 4 | `{"text": "mailto:kagenineema@gmail.com"}` | `/generate` | ✅ QR generated, prompted email client |
| 5 | `{"text": "tel:+254700000000"}` | `/generate` | ✅ QR generated, prompted phone dialer |
| 6 | `{"text": ""}` | `/generate` | ⚠️ Originally blank QR — fixed with validation |

**Iteration after Test 6:**
Empty strings originally produced a blank QR code with no error. Input validation was added using `HTTPException` to reject empty strings with a `400 Bad Request` response.

---

## 🧠 AI Prompt Journal

Prompts are grouped into two categories — **Learning FastAPI** (conceptual and foundational) and **Building the Project** (implementation and problem-solving).

---

### 📖 Part A — Learning FastAPI

1. "What is FastAPI and how is it different from regular Python scripts?"
2. "What problem does FastAPI solve that plain Python cannot handle on its own?"
3. "How does FastAPI compare to Flask? When should I use one over the other?"
4. "What is an API and what does REST mean in REST API?"
5. "What is HTTP and what are the differences between GET, POST, PUT, and DELETE methods?"
6. "What is a route in FastAPI and how do I define one?"
7. "What does the @app.get and @app.post decorator do in FastAPI?"
8. "What is Pydantic and why does FastAPI use it for data validation?"
9. "What is BaseModel in Pydantic and how do I use it to define a request body?"
10. "What is uvicorn and why do I need it separately from FastAPI to run my server?"
11. "What does the --reload flag do in uvicorn and when should I not use it?"
12. "What is the FastAPI /docs page and how does Swagger UI work?"
13. "What is an HTTP status code? What do 200, 400, 404, and 422 mean?"
14. "What is middleware in FastAPI and when would I need it?"
15. "What is the difference between a query parameter and a request body in FastAPI?"
16. "What is async and await in Python and does FastAPI require me to use them?"
17. "How does FastAPI automatically generate documentation from my code?"
18. "What is ASGI and how is it different from WSGI?"
19. "What is a virtual environment in Python and should I use one with FastAPI?"
20. "How do I structure a FastAPI project as it grows bigger?"

---

### 🔨 Part B — Building the QR Code Generator Project

21. "Give me step by step instructions to install FastAPI and run my first server"
22. "How do I create a POST endpoint in FastAPI that accepts a JSON body with a text field?"
23. "How do I use the Python qrcode library to generate and save a QR code as a PNG image?"
24. "What is the difference between qrcode and qrcode[pil] when installing? Why does [pil] matter?"
25. "How do I return an image file as a response from a FastAPI endpoint instead of JSON?"
26. "What is FileResponse in FastAPI and how do I use it to return a PNG image?"
27. "How do I add a title, description, and version to my FastAPI app?"
28. "How do I validate that the text field in my request body is not an empty string?"
29. "How do I raise an HTTPException in FastAPI to return a 400 error with a custom message?"
30. "How do I test my FastAPI endpoints using the built-in Swagger UI at /docs?"
31. "My FastAPI server says port 8000 is already in use. How do I fix this?"
32. "Why does my browser open the URL instead of downloading the QR code image?"
33. "How do I create a requirements.txt file for my FastAPI project?"
34. "How do I create a .gitignore file for a Python project before pushing to GitHub?"
35. "How do I push my FastAPI project to a new GitHub repository from the terminal?"

---

## ❓ Project FAQ

**Q: Why FastAPI and not Flask?**
Flask is older and more commonly taught, but FastAPI is faster, has built-in data validation, and auto-generates documentation. For a pure API project, FastAPI is the cleaner choice.

**Q: Why a QR Code Generator?**
QR codes are used in real-world systems — payments, 2FA, marketing, logistics. The project produces a visual, scannable output that is easy to demo and immediately useful.

**Q: Do I need a database?**
No. The API is stateless — it generates the QR code on the fly per request. No storage is needed.

**Q: What types of input does the API accept?**
Any string — URLs, plain text, email addresses (`mailto:`), phone numbers (`tel:`), WiFi credentials, vCards, or any other text. The qrcode library encodes whatever string you send.

**Q: Can I deploy this API online?**
Yes. Platforms like Railway, Render, or AWS can host it. The API has no database dependency, making deployment straightforward.

**Q: What happens if I send an empty string?**
The API rejects it with a `400 Bad Request` error and a clear message asking you to provide valid text.

---

## 🐛 Common Issues & Fixes

**Issue 1: `ModuleNotFoundError: No module named 'qrcode'`**
```
Fix: pip install qrcode[pil]
Include [pil] — without it image generation fails silently.
```

**Issue 2: `ModuleNotFoundError: No module named 'pydantic'`**
```
Fix: pip install pydantic
Usually installed automatically with FastAPI — reinstalling fixes it.
```

**Issue 3: Port already in use**
```
Fix: uvicorn main:app --reload --port 8001
Switch to a different port number.
```

**Issue 4: Browser opens URL instead of downloading image**
```
Normal browser behavior for image responses.
Check the project folder for qrcode_output.png and scan with your phone.
```

**Issue 5: `422 Unprocessable Entity`**
```
Request body format is wrong.
Send: {"text": "your content here"}
```

**Issue 6: uvicorn not recognized as a command**
```
Fix: python -m uvicorn main:app --reload
```

---

## 📚 References

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [qrcode Library on PyPI](https://pypi.org/project/qrcode/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [FastAPI Full Course - FreeCodeCamp YouTube](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- [HTTP Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [What is a REST API - Red Hat](https://www.redhat.com/en/topics/api/what-is-a-rest-api)
- [Swagger UI Documentation](https://swagger.io/tools/swagger-ui/)

---

## 👤 Author

**Majira Neema Kageni**
GitHub: [Emma-coder-dev](https://github.com/Emma-coder-dev)