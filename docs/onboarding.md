# 🧭 Onboarding Guide — AI Music Streaming Backend

---

# 👋 Welcome

Welcome to the AI Music Streaming Backend 🎧

This system combines:

* 🎵 Music streaming APIs
* 🔍 Keyword + AI-powered search
* 🏗️ Scalable backend architecture

This guide will help you:

* Understand the system quickly
* Run it locally
* Navigate the codebase
* Make safe changes

---

# ⚡ 1. Quick Start (Run in 5 Minutes)

---

## 🔧 Prerequisites

* Python 3.10+
* pip / virtualenv
* Redis (optional but recommended)

---

## 🚀 Setup

```bash id="setup01"
git clone <repo-url>
cd <project-folder>

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env id="env01"
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Server

```bash id="run01"
python manage.py migrate
python manage.py runserver
```

---

## ✅ Verify

Open:

```id="verify01"
http://localhost:8000/
```

Expected response:

```json id="verify02"
{
  "message": "Spotify Clone Running 🎵"
}
```

---

# 🧠 2. How to Think About This System

---

## 🧩 Mental Model

```id="mental01"
View → Service → Repository → Database
```

### In plain terms:

* **Views** → receive requests
* **Services** → make decisions
* **Repositories** → fetch/store data

---

## 🧠 AI Search Flow

```id="mental02"
User Query → LLM → Filters → ORM → Results
```

---

# 📂 3. Codebase Navigation

---

## 🔑 Key Folders

```id="nav01"
songs/
   views.py        → API endpoints
   services/       → business logic
   repository/     → DB queries
   utils/          → helpers (streaming, etc.)

users/
   authentication & user logic

docs/
   api.md
   architecture.md
   onboarding.md
```

---

## 🧭 Where to Start Reading

If you're new:

1. `songs/views.py` → entry point
2. `services/` → understand logic
3. `repository/` → see DB interaction

---

# 🔍 4. Key Features Walkthrough

---

## 🎵 Song Flow

```id="flow01"
Request → View → Service → Repository → DB
```

---

## 🔍 Search Flow

### v1 (Keyword)

```id="flow02"
Query → ORM → Results
```

### v2 (AI)

```id="flow03"
Query → parse_query() → Filters → ORM → Results
```

---

## ▶️ Streaming Flow

```id="flow04"
API → Service → StreamingService → Audio Stream
```

---

# 🧪 5. Testing the APIs

---

## 🎵 Get Songs

```bash id="test01"
curl http://localhost:8000/songs/
```

---

## 🔍 Keyword Search

```bash id="test02"
curl "http://localhost:8000/api/v1/search/?q=love"
```

---

## 🧠 AI Search

```bash id="test03"
curl "http://localhost:8000/api/v2/search/?q=romantic songs"
```

---

## ▶️ Play Song

```bash id="test04"
curl http://localhost:8000/play/1/
```

---

# 🔐 6. Authentication

---

Used for:

* Uploading songs

### Flow

```id="auth01"
User → Token → Request → DRF Permission → Access
```

---

# 🛠️ 7. How to Make Changes Safely

---

## ✅ Adding a New Feature

1. Add logic in `services/`
2. Add DB logic in `repository/`
3. Expose via `views.py`
4. Update API docs

---

## 🔍 Modifying Search

* Update `parse_query()`
* Ensure filters match DB fields
* Test fallback behavior

---

## 🎵 Adding New Song Fields

* Update model
* Update repository filters
* Update API response

---

# ⚠️ 8. Common Pitfalls

---

### ❌ Putting logic in views

Keep views thin

---

### ❌ Breaking filter structure

AI search depends on consistent JSON format

---

### ❌ Forgetting fallback logic

Always ensure system works without LLM

---

### ❌ Hardcoding secrets

Use `.env` for API keys

---

# ⚡ 9. Performance Awareness

---

* LLM calls are expensive → avoid unnecessary calls
* Use keyword search for simple queries
* Redis can be used for caching

---

# 🚀 10. First Task for New Engineers

---

Try this:

### ✅ Task

* Add a new filter: `language`

### Steps

1. Update `parse_query()` prompt
2. Add field in repository filter
3. Update API response
4. Test via `/api/v2/search/`

---

# 🧠 11. Growth Path

---

Once comfortable:

* Add vector search (FAISS)
* Implement recommendation engine
* Optimize streaming with chunking
* Add async processing (Celery)

---

# 🏁 Summary

You now know:

* How the system is structured
* How data flows
* Where to make changes
* How to extend safely

---

Welcome aboard 🚀
Build carefully, scale confidently.

---
