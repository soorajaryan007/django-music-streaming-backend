
````md
# 🎧 AI Music Streaming Backend — Django + DRF

A production-oriented backend system for a music streaming platform built using **Django + Django REST Framework (DRF)**.

Designed with **clean architecture principles**, this project separates concerns into **API, service, repository, and storage layers**, and integrates **AI-powered natural language search** using Groq.

---

# 🚀 Features

### 🎵 Core Backend
- Song upload & streaming APIs
- JWT-based authentication
- Secure APIs with permissions & throttling
- Storage abstraction (Local + S3 ready)

### 🔍 Search System
- **v1:** Keyword-based search  
- **v2:** Natural language search using LLM (Groq)

### ⚡ Performance & Observability
- API latency tracking
- Redis caching support (extensible)

### 🧠 Architecture
- Service-oriented design
- Clean separation of concerns
- Scalable backend patterns

---

# 🏗️ Architecture Overview

```text
Client 🌍
   ↓
DRF API Layer (Views)
   ↓
Service Layer (Business Logic)
   ↓
Repository Layer (DB Access)
   ↓
Database / Storage (PostgreSQL / S3 / Local)
````

---

# 📂 Project Structure

```
.
├── root/                  # Core Django project
│   ├── settings/          # Environment-based settings
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│
├── users/                 # Authentication & user management
│   ├── models.py
│   ├── serializers.py
│   ├── authentication.py
│   ├── utils/jwt.py
│   └── views.py
│
├── songs/                 # Song domain
│   ├── models.py
│   ├── views.py
│   ├── services/
│   ├── repositories/
│   ├── storage/
│   ├── cache/
│   ├── api_latency/
│   └── utils/
│
├── media/
├── requirements.txt
└── manage.py
```

---

# 🔍 Search APIs

## v1 — Keyword Search

```http
GET /api/v1/search/?title=bhala
```

* Uses Django ORM (`icontains`)
* Fast and deterministic

---

## v2 — Natural Language Search (Groq)

```http
GET /api/v2/search/?q=romantic songs
```

### Flow:

```text
User Query
   ↓
LLM (Groq)
   ↓
Structured Filters
   ↓
Django ORM
   ↓
Results
```

Example response:

```json
{
  "version": "v2",
  "query": "romantic songs",
  "interpreted_filters": {
    "title": "romantic",
    "genre": "romantic"
  },
  "results": [...]
}
```

---

# 🧠 AI Integration

* Uses **Groq (LLM inference)** for query understanding
* Converts natural language → structured filters
* Hybrid system:

  * Short queries → keyword search
  * Complex queries → LLM-powered parsing

---

# 🔐 Authentication Flow

```text
Client → Login → JWT Token
        ↓
Request with Authorization Header
        ↓
JWT Authentication
        ↓
request.user populated
        ↓
Permission check
```

---

# ⚙️ Key Design Decisions

### ✅ DRF-first architecture

* Authentication handled via DRF (no middleware coupling)

### ✅ Service-Oriented Design

* Thin views, logic in services

### ✅ Storage Abstraction

* Easily switch between local and S3

### ✅ Versioned APIs

* v1: deterministic search
* v2: AI-powered search

---

# 🔥 Performance & Scaling

* DRF throttling (`UserRateThrottle`)
* Redis caching support
* Latency tracking for endpoints

---

# 🛠️ Setup Instructions

## 1️⃣ Clone repo

```bash
git clone <repo-url>
cd django-spotify
```

## 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Configure environment

Create `.env`:

```env
DB_NAME=spotify_clone
DB_USER=user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5433

SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_key
```

## 5️⃣ Run migrations

```bash
python manage.py migrate --settings=root.settings.local
```

## 6️⃣ Start server

```bash
python manage.py runserver --settings=root.settings.local
```

---

# 📡 API Endpoints

## 🔐 Auth

* `POST /login/`
* `POST /register/`

## 🎵 Songs

* `GET /songs/`
* `GET /api/v1/search/`
* `GET /api/v2/search/`
* `POST /songs/upload/` (Auth required)
* `GET /songs/<id>/play/`

---

# 🧪 Future Improvements

### 🚀 AI & Search

* Semantic search (FAISS)
* Embeddings-based retrieval
* Query ranking system

### 🎵 Product Features

* AI playlist generator
* Music agent (auto playlist creation)
* Better metadata (mood, genre tagging)

### ⚙️ Backend Scaling

* Async processing (Celery)
* Distributed caching (Redis cluster)
* CDN for media delivery

---

# ⚠️ Known Limitations

* Semantic search not implemented yet
* Results depend on text matching
* Limited dataset for meaningful AI inference

---

# 🧠 Key Learning Highlights

This project demonstrates:

* Clean architecture in Django
* DRF internals (auth, permissions, throttling)
* LLM integration in backend systems
* API versioning strategies
* Scalable backend design patterns

---

# 👨‍💻 Author

Built with focus on **backend engineering, system design, and AI-powered search systems**.

````

---

# 🔥 What changed (and why it matters)

I:

- Removed duplication  
- Structured it like a **real product doc**  
- Highlighted **AI + versioning (your USP)**  
- Made it **recruiter-friendly in <30 sec scan**  

---

# 🎯 Honest verdict

If you push this:

👉 You won’t look like “just another Django dev”  
👉 You’ll look like:

```text
Backend Engineer → with AI system thinking
````

---
