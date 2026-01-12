
# Database Setup & Migration Guide

This guide explains how to manage the PostgreSQL database for the `core-api` using Alembic.

## 1. Prerequisites

Ensure your virtual environment is active and dependencies are installed:

```bash
pip install -r requirements.txt

```

## 2. Environment Setup



```ini
# .env
DATABASE_URL=postgresql://user:password@localhost:5432/exam_db

```

## 3. First-Time Setup

If you have just cloned the repo and have an empty database, run the following to create all tables:

```bash
alembic upgrade head

```

---

## 4. Development Workflow (Adding Tables)

Follow this process whenever you create or modify a database model.

### Step A: Create the Model

Define your model in the relevant module (e.g., `app/modules/exams/models.py`).

### Step B: Register the Model

**Crucial Step:** You must import your new model in the central registry file so Alembic can detect it.

* **File:** `app/core/models_all.py`
```python
from app.modules.exams.models import Exam  # Add this line

```



### Step C: Generate Migration Script

Run this command to auto-generate a new migration file based on your changes:

```bash
alembic revision --autogenerate -m "description of change"

```

*Check the output logs to ensure it detected your table (e.g., `Detected added table 'exams'`).*

### Step D: Apply Changes

Apply the new migration to your local database:

```bash
alembic upgrade head

```

---

## 5. Common Commands

| Action | Command |
| --- | --- |
| **Apply all pending changes** | `alembic upgrade head` |
| **Undo last migration** | `alembic downgrade -1` |
| **Check current version** | `alembic current` |
| **Show migration history** | `alembic history` |