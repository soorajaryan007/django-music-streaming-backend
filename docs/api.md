# 🎧 API Documentation — AI Music Streaming Backend

## 🌐 Base URL

```
http://localhost:8000/
```

---

# 🧭 Overview

This backend provides:

* 🎵 Song management & streaming
* 🔍 Keyword-based search (v1)
* 🧠 AI-powered natural language search (v2)
* 🔐 Authenticated upload system

---

# ❤️ Health Check

### GET `/`

Check if server is running

#### Response

```json
{
  "message": "Spotify Clone Running 🎵"
}
```

---

# 🎵 Songs API

---

## 1. Get All Songs

### GET `/songs/`

Fetch all available songs

#### Permissions

* Public

#### Response

```json
[
  {
    "id": 1,
    "title": "Song Name",
    "artist": "Artist",
    "url": "..."
  }
]
```

---

## 2. Play Song (Streaming)

### GET `/play/<song_id>/`

Streams the song

#### Permissions

* Public

#### Example

```
/play/1/
```

#### Behavior

* Returns audio stream
* Uses optimized streaming service
* Latency is tracked internally

#### Errors

```json
{
  "error": "Not found"
}
```

---

## 3. Upload Song

### POST `/upload-song/`

Upload a new song

#### Permissions

* Authenticated users only

#### Headers

```
Authorization: Bearer <token>
```

#### Request (multipart/form-data)

* file
* title
* artist
* metadata (optional)

#### Response

```json
{
  "message": "Song uploaded successfully",
  "song_id": 10
}
```

---

# 🔍 Search APIs

---

## 🟢 v1 — Keyword Search

### GET `/api/v1/search/`

Fast and deterministic search using Django ORM

#### Query Params

* `q` (required): song title keyword

#### Example

```
/api/v1/search/?q=bhala
```

#### Response

```json
{
  "version": "v1",
  "results": [
    {
      "id": 1,
      "title": "Bhala Song"
    }
  ]
}
```

#### Errors

```json
{
  "error": "title query parameter required"
}
```

---

## 🧠 v2 — AI Natural Language Search

### GET `/api/v2/search/`

Understands human queries using LLM and converts them into structured filters

---

## 🧬 Flow

```
User Query
   ↓
LLM (Groq - llama3-70b)
   ↓
Structured Filters
   ↓
Django ORM
   ↓
Results
```

---

## Query Params

* `q` (required): natural language query

---

## Example

```
/api/v2/search/?q=romantic sad songs from 2010
```

---

## Response

```json
{
  "version": "v2",
  "query": "romantic sad songs from 2010",
  "interpreted_filters": {
    "title": "romantic",
    "artist": null,
    "genre": "romantic",
    "mood": "sad",
    "year": 2010
  },
  "results_count": 5,
  "results": [...]
}
```

---

## ⚡ Optimization Logic

* If query has ≤ 2 words → skips LLM → treated as title search
* Improves performance and reduces cost

---

## 🛡️ Fallback Strategy

If LLM fails:

* Entire query is treated as `title`
* System still returns results instead of failing

---

## 🧠 Supported Filters

| Field  | Description    |
| ------ | -------------- |
| title  | Song title     |
| artist | Artist name    |
| genre  | Music genre    |
| mood   | Emotional tone |
| year   | Release year   |

---

# 🔐 Authentication

Used for:

* Uploading songs

Supports:

* Token / JWT (depending on implementation)

---

# ⚡ Performance Features

* ⏱️ API latency tracking (`@measure_latency`)
* ⚡ Redis caching (optional)
* 🚦 Rate limiting (throttling support)

---

# 🧩 Design Philosophy

This API is built with:

* Service Layer → Business logic
* Repository Layer → DB abstraction
* LLM Layer → Intelligent query parsing

---

# 🧠 Developer Tips

* Use v1 for speed-critical systems
* Use v2 for better UX (user-facing search)
* Extend filters by modifying `parse_query()`

---

# 🚀 Future Enhancements

* Vector search (semantic embeddings)
* Personalized recommendations
* Hybrid search (keyword + vector + LLM)
* Streaming optimization with chunking/CDN

---

# 🧭 Quick Test Commands

```bash
# Get songs
curl http://localhost:8000/songs/

# Keyword search
curl "http://localhost:8000/api/v1/search/?q=love"

# AI search
curl "http://localhost:8000/api/v2/search/?q=romantic songs"

# Play song
curl http://localhost:8000/play/1/
```

---

# 🏁 Summary

This API is designed to mimic real-world music platforms:

* ⚡ Fast keyword retrieval
* 🧠 Intelligent natural language understanding
* 🏗️ Scalable backend architecture

---
