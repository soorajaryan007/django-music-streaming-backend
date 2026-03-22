## 🎧 Django Music Streaming Backend

A scalable backend prototype of a **Spotify-like music streaming service** built using **Django, PostgreSQL, and Django ORM**.

This project implements a backend system responsible for **user management, song metadata storage, file uploads, and audio streaming**.

It is designed as a **modular and production-ready foundation** that can scale with technologies like **Redis, AWS S3, CDN, and microservices**.

---

# 🏗 Architecture Overview

This system follows a **layered backend architecture**:

### Core Responsibilities

* User management
* Song metadata storage
* File upload & storage
* Music streaming APIs

---

### System Flow

```
Users
   ↓
Django Server (Gunicorn)
   ↓
Business Logic (Services Layer)
   ↓
Storage Layer (Local / S3)
   ↓
PostgreSQL Database
```

---

# 🚀 Features

* REST API built with Django
* PostgreSQL relational database
* Django ORM for database operations
* MP3 file upload support
* Audio streaming endpoint
* Modular architecture (services, storage separation)
* Clean and scalable backend design

---

# 🧰 Tech Stack

### Backend Framework

**Django**

### Database

**PostgreSQL**

### ORM

**Django ORM**

### Programming Language

**Python**

### API Testing

**Postman / Curl**

### Version Control

**Git**

---

# 📁 Project Structure

```
django-spotify/
│
├── manage.py
├── root/
│   ├── settings.py
│   ├── urls.py
│
├── songs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   │
│   ├── services/
│   │   └── song_service.py
│   │
│   ├── repositories/
│   │   └── song_repository.py
│   │
│   ├── storage/
│   │   ├── local_storage.py
│   │   ├── s3_storage.py
│   │   └── storage_factory.py
│   │
│   ├── utils/
│   │   └── response_handler.py
│   │
│   ├── migrations/
│   └── admin.py
│
└── media/   # Uploaded audio files
```

---

# 🔌 API Endpoints

### Health Check

```
GET /
```

Response:

```json
{
  "message": "Django Spotify Backend Running 🎵"
}
```

---

### Upload Song

```
POST /upload-song
```

Form Data:

* title
* artist
* genre
* file (mp3)

Response:

```json
{
  "id": 1,
  "title": "Song Name",
  "artist": "Artist",
  "genre": "Genre"
}
```

---

### Get All Songs

```
GET /songs
```

Response:

```json
[
  {
    "id": 1,
    "title": "Song Name",
    "artist": "Artist",
    "genre": "Genre",
    "mp3_path": "/media/xyz.mp3"
  }
]
```

---

### Stream Song

```
GET /play/<song_id>
```

Streams the requested MP3 file.

---

# 🗄 Database Schema

### Users Table

| Column     | Type            |
| ---------- | --------------- |
| id         | Integer (PK)    |
| username   | String (unique) |
| email      | String (unique) |
| created_at | DateTime        |

---

### Songs Table

| Column     | Type         |
| ---------- | ------------ |
| id         | Integer (PK) |
| title      | String       |
| artist     | String       |
| genre      | String       |
| mp3_path   | String       |
| created_at | DateTime     |

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```
git clone https://github.com/yourusername/django-spotify.git
cd django-spotify
```

---

## 2. Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate
```

Windows:

```
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Configure Database

Update `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "spotify_clone",
        "USER": "user",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5433",
    }
}
```

---

## 5. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Create Media Folder

```
mkdir media
```

---

## 7. Run Server

```
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# 🎯 Usage

* Upload songs via API (Postman)
* Store metadata in PostgreSQL
* Stream songs directly via endpoint

---

# ☁️ Future Improvements

* Redis caching layer
* AWS S3 storage integration
* CDN for fast streaming
* JWT authentication
* User playlists
* Recommendation engine
* Microservices architecture

---

# 🎯 Learning Goals

This project demonstrates:

* Backend system design
* Django architecture
* File handling & streaming
* Database modeling
* Scalable backend patterns

---

# 👨‍💻 Author

**Sooraj Aryan**

---

# 📄 License

MIT License
