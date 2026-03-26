# 🎧 AI Music Streaming Backend

### Django • DRF • AI Search • Scalable Architecture

> A production-grade backend system that combines **clean architecture** with **AI-powered search** to simulate how modern music platforms work.

---

## ✨ Why this project?

Most backend projects stop at CRUD.

This one goes further:

* ⚡ Designed for **scale**
* 🧠 Integrates **LLM-based natural language search**
* 🏗️ Follows **real-world backend architecture patterns**

---

## 🚀 Core Features

### 🎵 Music Backend

* Upload & stream songs
* Secure APIs with authentication & permissions
* Storage abstraction (Local + S3 ready)

### 🔍 Intelligent Search

* **v1:** Fast keyword search
* **v2:** Natural language search (AI-powered)

### ⚡ Performance

* API latency tracking
* Redis caching support
* Throttling for rate limiting

### 🧠 Architecture

* Service-oriented design
* Repository abstraction
* Clean separation of concerns

---

## 🧠 How Search Works

### v1 — Keyword Search

```http
GET /api/v1/search/?title=bhala
```

* Uses Django ORM
* Fast and predictable

---

### v2 — AI Search (Groq)

```http
GET /api/v2/search/?q=romantic songs
```

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

👉 Example:

```json
{
  "query": "romantic songs",
  "interpreted_filters": {
    "title": "romantic",
    "genre": "romantic"
  }
}
```

---

## 🏗️ Architecture

```text
Client
   ↓
API Layer (DRF Views)
   ↓
Service Layer (Business Logic)
   ↓
Repository Layer (DB Access)
   ↓
Storage (PostgreSQL / S3 / Local)
```

---

## 📂 Project Structure

```bash
songs/
├── views/          # API Layer
├── services/       # Business Logic
├── repositories/   # DB abstraction
├── storage/        # File storage
├── cache/          # Redis layer
└── utils/
```

---

## 🔐 Authentication Flow

```text
Login → JWT Token
      ↓
Request with Token
      ↓
Authentication
      ↓
Access Protected APIs
```

---

## ⚙️ Tech Stack

* **Backend:** Django, DRF
* **AI:** Groq (LLM inference)
* **Database:** PostgreSQL
* **Caching:** Redis (optional)

---

## 📡 API Endpoints

### 🔐 Auth

* `POST /login/`
* `POST /register/`

### 🎵 Songs

* `GET /songs/`
* `GET /api/v1/search/`
* `GET /api/v2/search/`
* `POST /songs/upload/`
* `GET /songs/<id>/play/`

---

## 🧪 What’s Next

* 🔥 Semantic search (FAISS)
* 🎧 AI playlist generator
* 🤖 Autonomous music agent
* ⚡ Async processing (Celery)
* 🌍 CDN-based streaming

---

## ⚠️ Limitations

* No semantic search yet
* Results depend on text matching
* Small dataset

---

## 🧠 What this project demonstrates

* Clean backend architecture in Django
* Real-world API design patterns
* LLM integration in backend systems
* Versioned APIs (v1 → v2 evolution)

---

## 👨‍💻 Author

Built with focus on **backend engineering + AI systems design**
