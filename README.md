# 🎵 Django Spotify Clone — Scalable Backend Architecture

A production-oriented backend system for a music streaming platform built using **Django + Django REST Framework (DRF)**.

This project is designed with **clean architecture principles**, separating concerns into **API layer, service layer, repository layer, and storage layer**.

---

# 🚀 Features

* 🔐 JWT-based Authentication
* 🎵 Song Upload & Streaming
* 📦 Storage abstraction (Local + S3 ready)
* ⚡ Redis caching support
* ⏱️ API latency tracking
* 🧠 Service-oriented architecture
* 🔒 Secure APIs with permissions & throttling

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
```

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
│   ├── authentication.py  # JWT authentication
│   ├── utils/jwt.py       # Token generation & decoding
│   └── views.py
│
├── songs/                 # Song domain
│   ├── models.py
│   ├── views.py
│   ├── services/          # Business logic
│   ├── repositories/      # DB abstraction
│   ├── storage/           # Storage layer (Local/S3)
│   ├── cache/             # Redis caching
│   ├── api_latency/       # Performance tracking
│   └── utils/             # Helpers
│
├── media/                 # Uploaded songs (local storage)
├── requirements.txt
└── manage.py
```

---

# 🧠 Layered Architecture

## 1️⃣ API Layer (Views)

* Handles HTTP requests
* Applies authentication, permissions, throttling
* Delegates logic to services

Example:

```python
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_song(request):
    return service.upload_song(...)
```

---

## 2️⃣ Service Layer (Core Logic)

* Contains business rules
* Orchestrates repository + storage

Example:

```python
song_service.upload_song()
```

---

## 3️⃣ Repository Layer

* Handles database operations
* Keeps ORM isolated from business logic

---

## 4️⃣ Storage Layer

* Abstracts file storage
* Supports:

  * Local storage
  * AWS S3 (pluggable)

---

## 5️⃣ Authentication Layer

* Custom JWT authentication (`users.authentication.JWTAuthentication`)
* Integrated with DRF
* Stateless and scalable

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
Permission check (IsAuthenticated)
```

---

# ⚙️ Key Design Decisions

## ✅ DRF-first architecture

* Removed Django middleware-based auth
* Centralized authentication in DRF

## ✅ Service-Oriented Design

* Views are thin
* Business logic isolated

## ✅ Storage Abstraction

* Easily switch between local and S3

## ✅ Environment-based settings

* `base.py`, `local.py`, `production.py`

---

# 🔥 Performance & Scaling

* Throttling enabled:

  * `UserRateThrottle`
* Redis caching support (extensible)
* API latency tracking middleware

---

# 🛠️ Setup Instructions

## 1️⃣ Clone repo

```bash
git clone <repo-url>
cd django-spotify
```

---

## 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure environment

Create `.env`:

```env
DB_NAME=spotify_clone
DB_USER=user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5433

SECRET_KEY=your_secret_key
```

---

## 5️⃣ Run migrations

```bash
python manage.py migrate --settings=root.settings.local
```

---

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
* `GET /songs/search/`
* `POST /songs/upload/` (Auth required)
* `GET /songs/<id>/play/`

---

# 🧪 Future Improvements

* Refresh tokens
* Role-based permissions (Artist/Admin/User)
* Distributed caching (Redis cluster)
* Async processing (Celery)
* CDN integration for media delivery

1. ✅ Natural language music search
2. ✅ AI playlist generator
3. ✅ Music agent (create + save playlist automatically)

---

# 🧠 Key Learning Highlights

This project demonstrates:

* Clean architecture in Django
* DRF internals (auth, permissions, throttling)
* Separation of concerns
* Scalable backend design patterns

---

# 👨‍💻 Author

Built with focus on **system design + backend engineering fundamentals**.
