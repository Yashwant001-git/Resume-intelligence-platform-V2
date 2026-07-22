# Resume Intelligence Platform - Frontend

## Overview

The frontend is built using **Streamlit** and provides an interactive interface for uploading resumes and visualizing extracted candidate information.

The frontend communicates with the FastAPI backend through REST APIs.

---

## Features

- Resume upload
- Candidate profile visualization
- Skills dashboard
- Education cards
- Experience timeline
- Project details
- Certification details
- Excel download
- Responsive layout

---

## Technology Stack

- Python 3.10
- Streamlit
- Requests

---

## Folder Structure

```text
frontend/
│
├── components/
│   ├── upload.py
│   ├── personal_info.py
│   ├── skills.py
│   ├── education.py
│   ├── experience.py
│   ├── projects.py
│   └── certifications.py
│
├── services/
│
├── utils/
│
├── app.py
│
├── Dockerfile
│
└── requirements.txt
```

---

## Application Flow

```text
User
 │
 ▼
Upload Resume
 │
 ▼
FastAPI Backend
 │
 ▼
Extract Candidate Information
 │
 ▼
Streamlit Components
 │
 ├── Personal Information
 ├── Skills
 ├── Education
 ├── Experience
 ├── Projects
 └── Certifications
```

---

## Run Locally

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

## Docker

```bash
docker build -t resume-frontend .

docker run -p 8501:8501 resume-frontend
```

---

## Components

### Upload Component

Handles resume upload and API communication.

### Personal Information Component

Displays candidate personal information.

### Skills Component

Displays categorized technical and soft skills.

### Education Component

Displays educational qualifications.

### Experience Component

Displays professional experience using expandable sections.

### Projects Component

Displays project details, technologies, and GitHub links.

### Certifications Component

Displays certification details.

---

## Future Improvements

- Dark mode
- Dashboard analytics
- Resume comparison
- Candidate search
- Authentication
- Recruiter dashboard
