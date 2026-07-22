<div align="center">

# Resume Intelligence Platform

### AI-Powered Resume Parsing and Candidate Information Extraction

A hybrid information extraction system that combines rule-based techniques with Large Language Models (LLMs) to transform unstructured resumes into structured candidate profiles.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square&logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## Overview

Resume Intelligence Platform is an AI-powered application that extracts structured information from resumes using a hybrid information extraction pipeline.

The system combines deterministic rule-based extraction with local Large Language Models (LLMs) to identify, organize, and structure candidate information for recruiters and hiring teams.

---

## Features

- Resume upload through a Streamlit interface
- PDF parsing using Docling
- Automatic resume section detection
- Hybrid information extraction pipeline
- Rule-based extraction for structured sections
- LLM-powered extraction using Ollama
- Structured candidate profile generation
- REST API built with FastAPI
- Excel export functionality
- Modular and scalable architecture

---

## Architecture

```text
                           Resume (PDF)
                                 │
                                 ▼
                          PDF Loader
                                 │
                                 ▼
                         Docling Parser
                                 │
                                 ▼
                     Markdown Representation
                                 │
                                 ▼
                        Section Detection
                                 │
                                 ▼
                       Resume Section Builder
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
                ▼                                 ▼
      Rule-Based Extraction            LLM-Based Extraction
                │                                 │
                └────────────────┬────────────────┘
                                 ▼
                         Candidate Object
                                 │
                                 ▼
                           FastAPI Backend
                                 │
                                 ▼
                        Streamlit Frontend
```

---

## Technology Stack

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Frontend

- Streamlit

### AI

- Ollama
- Docling
- Regular Expressions

### Data Processing

- Pandas
- OpenPyXL

### DevOps

- Docker
- Docker Compose

---

## Project Structure

```text
resume-intelligence-platform/
│
├── backend/
│   ├── app/
│   ├── api/
│   ├── models/
│   ├── pipeline/
│   ├── services/
│   ├── utils/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── components/
│   ├── services/
│   ├── utils/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── docker/
│   └── docker-compose.yml
│
├── docs/
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Information Extraction Pipeline

The application uses a hybrid extraction strategy.

### Rule-Based Extraction

- Skills
- Experience
- Projects

### LLM-Based Extraction

- Personal Information
- Education
- Certifications

The extracted information is consolidated into a structured candidate profile before being returned through the REST API.

---

## Extracted Information

The platform extracts the following information:

- Personal Information
- Professional Summary
- Skills
- Education
- Experience
- Projects
- Certifications
- Languages
- Achievements
- Interests

---

## REST API

### Upload Resume

```http
POST /api/v1/resume/upload
```

### Sample Response

```json
{
  "success": true,
  "message": "Resume processed successfully",
  "data": {
    "personal_info": {},
    "skills": {},
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
  }
}
```

---

## Getting Started

### Clone Repository

```bash
git clone https://github.com/<username>/resume-intelligence-platform.git

cd resume-intelligence-platform
```

### Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

## Docker

Build and run the complete application using Docker Compose.

```bash
cd docker

docker compose up --build
```

---

## Screenshots

### Dashboard

_Add screenshot_

### Candidate Profile

_Add screenshot_

### Skills

_Add screenshot_

### Experience

_Add screenshot_

### Projects

_Add screenshot_

---

## Future Enhancements

- Resume ranking
- ATS compatibility scoring
- Resume similarity search
- Candidate recommendation engine
- Multi-language resume support
- Authentication and authorization
- Recruiter dashboard
- Cloud deployment

---

## License

This project is licensed under the MIT License.

---

## Author

**Yashwant Raj**

GitHub: https://github.com/<username>

LinkedIn: https://linkedin.com/in/<username>