# Songs Module

Handles song upload, metadata, and streaming.

## Responsibilities
- Store song metadata
- Handle file storage abstraction
- Provide streaming endpoints

## Key Files
- models.py → DB schema
- views.py → API endpoints
- services.py → business logic
- repository.py → DB abstraction

## Flow Example
Upload Song:
View → Service → Repository → Storage