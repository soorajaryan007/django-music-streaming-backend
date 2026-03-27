# 🏗️ Architecture — AI Music Streaming Backend

---

# 🧭 Overview

This system is designed as a **scalable, service-oriented backend** for a music streaming platform with AI-powered search.

It separates responsibilities into distinct layers to ensure:

* Maintainability
* Scalability
* Clear ownership of logic
* Easy extension into microservices

---

# 🧠 System Mental Model

Think of the system as three collaborating brains:

```id="brain01"
API Layer → Handles requests & responses  
Service Layer → Executes business logic  
Repository Layer → Interacts with database
```

Each layer has a single responsibility and does not leak concerns into others.

---

# 🗺️ High-Level Architecture

```id="arch02"
Client (Web / Mobile)
        ↓
API Layer (Django REST Framework)
        ↓
Service Layer (Business Logic)
        ↓
Repository Layer (Database Access)
        ↓
Storage Layer (PostgreSQL / S3 / Local)
```

---

# 🧠 AI Search Flow (v2)

```id="arch03"
User Query
   ↓
LLM (Groq - llama3-70b)
   ↓
Structured Filters (JSON)
   ↓
Service Layer
   ↓
Repository Layer (ORM Queries)
   ↓
Results
```

---

# 📂 Project Structure

```id="arch04"
root/
├── songs/
│   ├── views.py
│   ├── services/
│   ├── repository/
│   ├── utils/
│
├── users/
│   ├── views.py
│   ├── authentication/
│
├── docs/
│   ├── api.md
│   ├── architecture.md
│
├── manage.py
```

---

# 🔌 Layer Breakdown

---

## 1. API Layer (DRF Views)

### Responsibilities

* Handle HTTP requests
* Validate input
* Return responses
* Call service layer

### Example Flow

```id="arch05"
Request → View → Service → Response
```

### Characteristics

* Thin (no business logic)
* Stateless
* Permission controlled

---

## 2. Service Layer (Core Logic)

### Responsibilities

* Business logic
* Orchestrating workflows
* Calling repositories
* Integrating external services (LLM, storage)

### Example

```id="arch06"
natural_search_song()
   → parse_query()
   → get_song_by_natural_query()
```

### Why this layer?

* Prevents “fat views”
* Enables reuse
* Makes migration to microservices easier

---

## 3. Repository Layer (Data Access)

### Responsibilities

* Database interaction
* Query abstraction
* ORM handling

### Example

```id="arch07"
filter(filters)
get_all_songs()
get_song_by_title()
```

### Benefits

* Decouples DB logic from business logic
* Makes DB replacement easier

---

## 4. Storage Layer

### Current

* Local file storage

### Future-ready

* AWS S3 integration

### Responsibilities

* Store audio files
* Provide access URLs

---

# 🔍 Search Architecture

---

## 🟢 v1 — Keyword Search

```id="arch08"
Query → Service → ORM Filter → Results
```

* Fast
* Deterministic
* No AI dependency

---

## 🧠 v2 — AI Search

```id="arch09"
Query → LLM → JSON Filters → ORM → Results
```

### Key Component: `parse_query()`

* Converts natural language → structured filters
* Uses Groq LLM (llama3-70b)
* Ensures JSON output

---

## ⚡ Optimization Strategy

* Short queries (≤ 2 words) skip LLM
* Reduces latency + cost

---

## 🛡️ Fault Tolerance

If LLM fails:

```id="arch10"
Fallback → treat query as title search
```

System never breaks due to AI failure.

---

# 🎵 Streaming Architecture

```id="arch11"
Client → API → Service → StreamingService → File URL → Stream
```

### Features

* Efficient streaming response
* Latency tracking via decorator

---

# 🔐 Authentication Flow

```id="arch12"
Client → Token → DRF Permission → View → Service
```

* Upload API is protected
* Uses DRF authentication system

---

# ⚡ Performance & Scaling

---

## Current Optimizations

* ⏱️ Latency tracking (`@measure_latency`)
* ⚡ Redis caching support
* 🚦 Rate limiting (throttling)

---

## Future Scaling Strategy

### Horizontal Scaling

* Stateless API servers
* Load balancer

### Microservices Migration

Split into:

* Song Service
* Search Service
* User Service

---

## AI Scaling

* Replace Groq with:

  * Local LLM (Ollama)
  * OpenAI / Anthropic
* Add caching for LLM responses

---

# 🧩 Design Decisions

---

## Why Service Layer?

* Keeps views clean
* Centralizes business logic
* Enables testing

---

## Why Repository Pattern?

* Decouples ORM
* Improves maintainability

---

## Why LLM for Search?

* Handles fuzzy queries
* Improves UX
* Enables semantic understanding

---

## Why Hybrid Search?

* v1 → fast, reliable
* v2 → intelligent, flexible

Best of both worlds.

---

# 🧠 Trade-offs

| Decision      | Benefit            | Cost              |
| ------------- | ------------------ | ----------------- |
| LLM Search    | Better UX          | Latency + cost    |
| Service Layer | Clean architecture | More boilerplate  |
| Repository    | Flexibility        | Extra abstraction |

---

# 🚀 Future Architecture Evolution

---

## 🔮 Planned Features

* Vector search (FAISS / Pinecone)
* Hybrid ranking (keyword + semantic)
* Recommendation engine
* Event-driven architecture (Kafka)

---

## 🧠 Target Architecture

```id="arch13"
Client
   ↓
API Gateway
   ↓
Microservices
   ├── Song Service
   ├── Search Service (LLM + Vector DB)
   ├── User Service
   ↓
Data Layer
   ├── PostgreSQL
   ├── Redis
   ├── S3
```

---

# 🏁 Summary

This system is built with:

* Clear separation of concerns
* AI-enhanced capabilities
* Scalable backend design

It is structured to evolve from a **monolith → distributed system** without major rewrites.

---
