# 🔳 QR Code Generator API
### Prompt-Powered Kickstart: Building a Beginner's Toolkit for FastAPI

A beginner-friendly REST API built with **FastAPI** that generates real, scannable QR codes from any text or URL. Built as part of the Moringa AI Capstone Project.

---

## 🎯 Title & Objective

**Project Title:** Getting Started with FastAPI – A Beginner's Guide to Building a QR Code Generator API

**Technology chosen:** FastAPI (Python web framework)

**Why FastAPI?**
FastAPI is a modern Python framework for building APIs, widely used in cloud services, microservices, and DevSecOps pipelines. I chose it because I am self-learning cloud security and APIs are the backbone of cloud infrastructure — understanding how they are built and secured is directly relevant to my goal of working as a Cloud Security Engineer. The intention was to build a working REST API that accepts any text or URL and returns a real scannable QR code image as output.

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

### What it does
This API has two endpoints. The `/health` endpoint is the Hello World of APIs — it confirms the server is running and responding. The `/generate` endpoint is the core feature — send any text or URL, get back a real scannable QR code image.

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Hello World — confirms API is running |
| POST | `/generate` | Generate a QR code from text or URL |

### Health Check (Hello World)

```
GET /health
```

**Response:**
```json
{
  "status": "API is running"
}
```

### Generate a QR Code

**Request:**
```json
POST /generate
{
  "text": "https://github.com/Emma-coder-dev"
}
```

**Response:** Returns a `.png` QR code image file that can be scanned with any phone camera.

---

## 🖥️ How to Use the Swagger UI at /docs

When you run the server and open `http://127.0.0.1:8000/docs`, FastAPI shows an interactive page called **Swagger UI** — a built-in tool to test your API directly from the browser without Postman or any other tool.

### What you will see

At the top:
```
QR Code Generator API  1.0.0
A simple API to generate scannable QR codes from any text or URL
```

Two endpoints listed:
```
GET   /health     Health Check
POST  /generate   Generate Qr
```

---

### Testing GET /health

1. Click **GET /health** to expand it
2. Click **Try it out**
3. Click **Execute**
4. Check the **Response body**

Expected response:
```json
{
  "status": "API is running"
}
```
A **200** code means success.

---

### Testing POST /generate

1. Click **POST /generate** to expand it
2. Click **Try it out**
3. Replace `"string"` in the request body with your input
4. Click **Execute**
5. Click the **Download file** link under Response body
6. Open the image and scan with your phone

---

### What you can encode — Examples

**Website URL:**
```json
{ "text": "https://github.com/Emma-coder-dev" }
```

**Plain text:**
```json
{ "text": "Hello Moringa School" }
```

**Email address:**
```json
{ "text": "mailto:kagenineema@gmail.com" }
```

**Phone number:**
```json
{ "text": "tel:+254700000000" }
```

**WiFi credentials:**
```json
{ "text": "WIFI:S:NetworkName;T:WPA;P:yourpassword;;" }
```

**Contact card (vCard):**
```json
{ "text": "BEGIN:VCARD\nVERSION:3.0\nFN:Neema Kageni\nTEL:+254700000000\nEMAIL:kagenineema@gmail.com\nEND:VCARD" }
```

---

### Response codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request — empty or invalid input |
| 422 | Unprocessable Entity — wrong request format |
| 500 | Server Error |

---

## 🧪 Testing & Iteration

All testing was done using the FastAPI Swagger UI at `http://127.0.0.1:8000/docs`.

| # | Input | Endpoint | Result |
|---|-------|----------|--------|
| 1 | GET `/health` | `/health` | ✅ `{"status": "API is running"}` |
| 2 | `{"text": "https://github.com"}` | `/generate` | ✅ QR generated, scanned, opened GitHub |
| 3 | `{"text": "Hello Moringa School"}` | `/generate` | ✅ QR generated, scanned, showed text |
| 4 | `{"text": "mailto:kagenineema@gmail.com"}` | `/generate` | ✅ QR generated, prompted email client |
| 5 | `{"text": "tel:+254700000000"}` | `/generate` | ✅ QR generated, prompted phone dialer |
| 6 | `{"text": ""}` | `/generate` | ⚠️ Originally blank QR — fixed with validation |

**Iteration after Test 6:**
Empty strings originally produced a blank QR code with no error. Input validation was added using `HTTPException` to reject empty strings with a `400 Bad Request` response, making the API more robust.

---

## 🧠 AI Prompt Journal

Prompts are split into two parts — **Learning FastAPI** (conceptual) and **Building the Project** (implementation). Each includes a short response summary and evaluation.

---

### 📖 Part A — Learning FastAPI

---

**Prompt 1:** "What is FastAPI and how is it different from regular Python scripts?"

**Summary:** The AI explained that FastAPI is a web framework that runs as a continuous server listening for HTTP requests, unlike a plain Python script that runs once and exits. It uses type hints to validate incoming data automatically.

**Evaluation:** Perfect starting point. It removed the intimidation of starting a new framework by making it clear FastAPI is still Python — just with web handling built on top.

---

**Prompt 2:** "What problem does FastAPI solve that plain Python cannot handle on its own?"

**Summary:** Plain Python has no built-in way to listen for HTTP requests, validate incoming data, or return structured responses. FastAPI handles all of that with minimal code.

**Evaluation:** Helped me understand the gap FastAPI fills — before this I did not know why a framework was even needed.

---

**Prompt 3:** "How does FastAPI compare to Flask? When should I use one over the other?"

**Summary:** Flask is older, simpler, and better for traditional web apps. FastAPI is faster, has built-in validation and auto docs, and is better suited for pure API development and microservices.

**Evaluation:** Useful for justifying my technology choice. The comparison table the AI provided became part of this documentation.

---

**Prompt 4:** "What is an API and what does REST mean in REST API?"

**Summary:** An API is an interface that lets two systems communicate. REST is an architectural style that uses HTTP methods (GET, POST, PUT, DELETE) and URLs to define how that communication works.

**Evaluation:** Foundational. I needed this to understand what I was actually building before writing any code.

---

**Prompt 5:** "What is HTTP and what are the differences between GET, POST, PUT, and DELETE methods?"

**Summary:** HTTP is the protocol that powers web communication. GET retrieves data, POST sends new data, PUT updates existing data, and DELETE removes data. Each maps to a different type of operation.

**Evaluation:** Directly applicable — I used this to decide that `/health` should be GET and `/generate` should be POST.

---

**Prompt 6:** "What is a route in FastAPI and how do I define one?"

**Summary:** A route is a URL path that the API listens on. In FastAPI you define routes using decorators like `@app.get("/path")` above a function. That function runs whenever a matching request arrives.

**Evaluation:** Critical concept. Understanding routes made the structure of `main.py` immediately clear.

---

**Prompt 7:** "What does the @app.get and @app.post decorator do in FastAPI?"

**Summary:** These are Python decorators that register a function as the handler for a specific HTTP method and URL. When a request matches, FastAPI calls that function and returns its output as the HTTP response.

**Evaluation:** The decorator syntax was confusing at first. This prompt made it click — decorators are just route registration in FastAPI.

---

**Prompt 8:** "What is Pydantic and why does FastAPI use it for data validation?"

**Summary:** Pydantic is a Python library that validates data using type hints. FastAPI uses it to automatically check that incoming request data matches the expected format before the function even runs.

**Evaluation:** Explained why FastAPI gives clean error messages automatically — it is Pydantic doing the validation before my code runs.

---

**Prompt 9:** "What is BaseModel in Pydantic and how do I use it to define a request body?"

**Summary:** BaseModel is the base class from Pydantic. You create a class that inherits from it and declare fields with type hints. FastAPI reads this class to know what JSON fields to expect in the request.

**Evaluation:** Directly used in the project — `QRRequest(BaseModel)` with a `text: str` field came from understanding this prompt.

---

**Prompt 10:** "What is uvicorn and why do I need it separately from FastAPI to run my server?"

**Summary:** Uvicorn is an ASGI server — it listens on a port and handles HTTP connections, then passes requests to the FastAPI app. FastAPI is just a Python object, it needs a server to actually run.

**Evaluation:** Cleared up a major confusion. I initially did not understand why two things needed to be installed. Now I know FastAPI is the logic layer and uvicorn is the network layer.

---

**Prompt 11:** "What does the --reload flag do in uvicorn and when should I not use it?"

**Summary:** `--reload` makes uvicorn watch for file changes and restart automatically. It is useful during development but adds overhead and should be removed in production deployments.

**Evaluation:** Small but important detail — noted in the common issues section and relevant for future deployment.

---

**Prompt 12:** "What is the FastAPI /docs page and how does Swagger UI work?"

**Summary:** The `/docs` page is a Swagger UI automatically generated from the route definitions. It lets you test every endpoint interactively from the browser without any extra tooling.

**Evaluation:** One of the best discoveries in this project. Built-in testing saved a lot of time and made the demo much easier to present.

---

**Prompt 13:** "What is an HTTP status code? What do 200, 400, 404, and 422 mean?"

**Summary:** Status codes are numbers in HTTP responses that tell the client what happened. 200 means success, 400 means bad request, 404 means not found, and 422 means the request data was in the wrong format.

**Evaluation:** Used directly in the testing section and the Swagger UI guide. Essential knowledge for anyone working with APIs.

---

**Prompt 14:** "What is the difference between a query parameter and a request body in FastAPI?"

**Summary:** A query parameter is appended to the URL (e.g. `/generate?text=hello`) and is best for simple optional filters. A request body is sent as JSON in the request and is better for structured or longer data.

**Evaluation:** Helped me confirm that using a request body with Pydantic was the right choice for sending text to the `/generate` endpoint.

---

**Prompt 15:** "What is async and await in Python and does FastAPI require me to use them?"

**Summary:** Async and await enable non-blocking code execution, allowing the server to handle multiple requests at once without waiting. FastAPI supports both async and regular functions — async is optional for beginners.

**Evaluation:** Reassuring. I was worried I needed to learn async before starting. Knowing regular functions work fine let me focus on building first.

---

**Prompt 16:** "How does FastAPI automatically generate documentation from my code?"

**Summary:** FastAPI reads the route decorators, function signatures, Pydantic models, and docstrings to build an OpenAPI schema, which Swagger UI then renders as the interactive `/docs` page.

**Evaluation:** Interesting to understand the mechanism behind the magic. It reinforced why keeping code clean and typed matters in FastAPI.

---

**Prompt 17:** "What is ASGI and how is it different from WSGI?"

**Summary:** WSGI is an older Python web server standard that handles one request at a time synchronously. ASGI is the modern standard that supports async operations and can handle multiple concurrent requests.

**Evaluation:** Background knowledge relevant to cloud and DevSecOps contexts. FastAPI is ASGI-based, which is why it is fast and scalable.

---

**Prompt 18:** "What is a virtual environment in Python and should I use one with FastAPI?"

**Summary:** A virtual environment is an isolated Python environment that keeps project dependencies separate from the global Python installation. It is best practice for every Python project to avoid version conflicts.

**Evaluation:** Good practice note. For this project I installed globally for simplicity, but future projects will use virtual environments.

---

**Prompt 19:** "What is a virtual environment in Python and should I use one with FastAPI?"

**Summary:** The AI recommended separating routes into different files using `APIRouter` as a project grows, keeping models in a separate `schemas.py` and business logic in a `services.py` file.

**Evaluation:** Not needed for this project but useful to know for when the QR API grows into a larger service.

---

**Prompt 20:** "How do I structure a FastAPI project as it grows bigger?"

**Summary:** The AI recommended separating routes into different files using `APIRouter`, keeping models in a `schemas.py` file, and business logic in a `services.py` file for maintainability.

**Evaluation:** Not needed for this project's scope but valuable for future reference when building larger cloud-facing APIs.

---

### 🔨 Part B — Building the QR Code Generator Project

---

**Prompt 21:** "Give me step by step instructions to install FastAPI and run my first server"

**Summary:** The AI provided the exact pip install commands for fastapi and uvicorn, the minimum code for a running app, and the uvicorn command to start the server including the `--reload` flag for development.

**Evaluation:** Got the server running in under 10 minutes. The most immediately productive prompt of the project.

---

**Prompt 22:** "How do I create a POST endpoint in FastAPI that accepts a JSON body with a text field?"

**Summary:** The AI showed how to combine a Pydantic BaseModel class with a `@app.post` decorator. The model defines the expected JSON fields and FastAPI handles validation automatically.

**Evaluation:** This was the core of the `/generate` endpoint. Without this prompt I would not have known how to accept structured JSON input.

---

**Prompt 23:** "How do I use the Python qrcode library to generate and save a QR code as a PNG image?"

**Summary:** `qrcode.make(text)` generates a QR code image object and `.save("filename.png")` writes it to disk as a PNG file.

**Evaluation:** Simple and accurate. Two lines of code from this prompt handled the entire QR generation logic.

---

**Prompt 24:** "What is the difference between qrcode and qrcode[pil] when installing? Why does [pil] matter?"

**Summary:** The base `qrcode` package generates QR data but cannot save it as an image without Pillow. The `[pil]` extra installs Pillow automatically, enabling image file output.

**Evaluation:** Critical detail. Installing without `[pil]` causes a runtime error that is not obvious from the error message. This prompt saved debugging time.

---

**Prompt 25:** "How do I return an image file as a response from a FastAPI endpoint instead of JSON?"

**Summary:** FastAPI's default response is JSON. To return a file, import `FileResponse` from `fastapi.responses`, save the file to disk first, then return `FileResponse(path, media_type, filename)`.

**Evaluation:** This unblocked the entire project. Without knowing about `FileResponse` I would have had no way to return the QR image to the client.

---

**Prompt 26:** "What is FileResponse in FastAPI and how do I use it to return a PNG image?"

**Summary:** `FileResponse` is a response class that reads a file from disk and streams it as the HTTP response body. It accepts the file path, a media type string, and an optional download filename.

**Evaluation:** Follow-up to Prompt 25 for deeper understanding. The `media_type="image/png"` parameter was important for the browser to handle the response correctly.

---

**Prompt 27:** "How do I add a title, description, and version to my FastAPI app?"

**Summary:** Pass `title`, `description`, and `version` as arguments to the `FastAPI()` constructor. These appear at the top of the auto-generated `/docs` page.

**Evaluation:** Small touch but made the API look professional and complete in the Swagger UI.

---

**Prompt 28:** "How do I validate that the text field in my request body is not an empty string?"

**Summary:** Use `.strip()` on the text field to remove whitespace, then check if the result is falsy. If it is empty, raise an `HTTPException` with a 400 status code.

**Evaluation:** Applied directly after Test 6 revealed the empty string issue. Improved the API from a basic demo to a more production-ready implementation.

---

**Prompt 29:** "How do I raise an HTTPException in FastAPI to return a 400 error with a custom message?"

**Summary:** Import `HTTPException` from `fastapi`, then raise it inside the endpoint function with `status_code=400` and a `detail` string containing the error message.

**Evaluation:** Clean error handling that returns proper JSON error responses. Made the API behave correctly for invalid input.

---

**Prompt 30:** "How do I test my FastAPI endpoints using the built-in Swagger UI at /docs?"

**Summary:** Navigate to `/docs`, expand an endpoint, click Try it out, fill in the request body or parameters, click Execute, and read the response body and status code shown below.

**Evaluation:** Confirmed the testing workflow I was already using. The detailed walkthrough helped me document the testing section of this README accurately.

---

**Prompt 31:** "My FastAPI server says port 8000 is already in use. How do I fix this?"

**Summary:** Add `--port 8001` (or any free port) to the uvicorn command: `uvicorn main:app --reload --port 8001`.

**Evaluation:** Quick fix for a common error. Added to the Common Issues section so other beginners can resolve it immediately.

---

**Prompt 32:** "Why does my browser open the URL instead of downloading the QR code image?"

**Summary:** Browsers handle PNG responses by displaying or opening them rather than downloading. The QR code is still generated correctly — the file exists in the project folder and can be scanned directly.

**Evaluation:** Resolved confusion during testing. Confirmed that the API was working correctly and the browser behavior was expected.

---

**Prompt 33:** "How do I create a requirements.txt file for my FastAPI project?"

**Summary:** Run `pip freeze > requirements.txt` in the project directory. This writes all installed packages and their versions to a file that others can use to replicate the environment.

**Evaluation:** Standard practice for any Python project shared on GitHub. Makes the repo reproducible for anyone who clones it.

---

**Prompt 34:** "How do I create a .gitignore file for a Python project before pushing to GitHub?"

**Summary:** Create a `.gitignore` file and list files or folders to exclude — typically `__pycache__/`, `*.pyc`, `.env`, and generated output files like `qrcode_output.png`.

**Evaluation:** Kept the GitHub repo clean by excluding the generated QR image and Python cache files from version control.

---

**Prompt 35:** "How do I push my FastAPI project to a new GitHub repository from the terminal?"

**Summary:** Initialize git with `git init`, add a remote with `git remote add origin <url>`, stage files with `git add .`, commit with `git commit -m "message"`, and push with `git push -u origin main`.

**Evaluation:** Straightforward workflow. The project is now live at [github.com/Emma-coder-dev/qr-code-api](https://github.com/Emma-coder-dev/qr-code-api).

---

## ❓ Project FAQ

**Q: Why FastAPI and not Flask?**
Flask is older and more commonly taught, but FastAPI is faster, has built-in data validation, and auto-generates documentation. For a pure API project, FastAPI is the cleaner choice.

**Q: Why a QR Code Generator?**
QR codes are used in real-world systems — payments, 2FA, marketing, logistics. The project produces a visual, scannable output that is easy to demo and immediately useful.

**Q: Do I need a database?**
No. The API is stateless — it generates the QR code on the fly per request. No storage is needed.

**Q: What types of input does the API accept?**
Any string — URLs, plain text, email addresses, phone numbers, WiFi credentials, vCards, or any other text.

**Q: Can I deploy this API online?**
Yes. Platforms like Railway, Render, or AWS can host it. No database dependency makes deployment straightforward.

**Q: What happens if I send an empty string?**
The API rejects it with a `400 Bad Request` error and a clear message asking you to provide valid text.

**Q: What is the Hello World of this project?**
The `GET /health` endpoint is the Hello World — it is the simplest possible API response confirming the server is alive and responding.

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