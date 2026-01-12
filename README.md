# ExamCTL Backend API


## 🚀 Prerequisites

1.  **Python 3.10+** installed.
2.  **PostgreSQL** installed and running.
3.  **Virtualenv** (recommended).

---

## 🛠️ Installation & Setup

### 1. Clone & Environment
Navigate to the backend directory and set up your Python environment.

```bash
cd backend-api

# Create virtual environment
python -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows)
# venv\Scripts\activate
```

### 2. Install Dependencies

```base
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create `.env` file and setup values present in `.env.example`.


## 🗄️ Database Setup (Migrations)

This project uses **Alembic** for database migrations.

### 1. Initialize Database

Ensure your Postgres server is running and the database `exam_db` exists.

```sql
CREATE DATABASE exam_db;

```

### 2. Apply Migrations

Run the following command to create tables (Users, etc.) in your database:

```bash
alembic upgrade head

```

---

## 🏃 Running the Application

Start the development server with live reloading:

```bash
uvicorn app.main:app --reload

```

* **API Root:** `http://127.0.0.1:8000`
* **Health Check:** `http://127.0.0.1:8000/health`

---

## 📖 Documentation

Once the server is running, access the interactive API docs:

* **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
* *Note: Use the "Authorize" button to test JWT protected endpoints.*


* **ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

---

## 👨‍💻 Development Workflow

### How to add a new Table/Model

1. **Create Model:** Define your class in `app/modules/<feature>/models.py`.
2. **Register Model:** Import it in `app/core/models_all.py` so Alembic can see it.
```python
# app/core/models_all.py
from app.modules.exams.models import Exam 

```


3. **Generate Script:**
```bash
alembic revision --autogenerate -m "added exam table"

```


4. **Apply Change:**
```bash
alembic upgrade head

```



### How to add a new Endpoint

1. Create routes in `app/modules/<feature>/routes.py`.
2. Register the router in `app/api/v1/api.py`.

```python
# app/api/v1/api.py
from app.modules.exams import routes as exam_routes
api_router.include_router(exam_routes.router, prefix="/exams", tags=["Exams"])

```
