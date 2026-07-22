# Resume Intelligence Platform - Backend

## Overview

The backend is built using **FastAPI** and is responsible for processing resumes, extracting structured candidate information, and exposing REST APIs consumed by the frontend.

The extraction pipeline combines rule-based techniques with a local Large Language Model (LLM) to generate accurate candidate profiles.

---

## Features

- FastAPI REST API
- Resume upload
- PDF parsing using Docling
- Resume section detection
- Hybrid extraction pipeline
- Rule-based information extraction
- LLM-based information extraction using Ollama
- Excel export
- Modular architecture
- Logging and error handling

---

## Technology Stack

- Python 3.10
- FastAPI
- Uvicorn
- Pydantic
- Docling
- Ollama
- Pandas
- OpenPyXL

---

## Architecture

```text
Resume
   │
   ▼
PDF Loader
   │
   ▼
Docling Parser
   │
   ▼
Markdown Document
   │
   ▼
Section Detection
   │
   ▼
Extraction Manager
   │
   ├── Rule-Based Extraction
   └── LLM-Based Extraction
   │
   ▼
Candidate Model
   │
   ▼
REST API Response
```

---

## Project Structure

```text
backend/
│
├── app/
│
├── api/
│
├── models/
│
├── pipeline/
│
├── services/
│
├── utils/
│
├── output/
│
├── requirements.txt
│
├── Dockerfile
│
└── main.py
```

---

## API

### Upload Resume

```http
POST /api/v1/resume/upload
```

### Response

```json
{
  "success": true,
  "message": "Resume processed successfully",
  "data": {}
}
```

---

## Run Locally

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Docker

```bash
docker build -t resume-backend .

docker run -p 8000:8000 resume-backend
```

---

## Future Improvements

- Authentication
- PostgreSQL
- Background task processing
- Cloud storage integration
- Resume ranking
- ATS score generation
