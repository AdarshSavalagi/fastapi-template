```txt
/backend-api
├── app/
│   ├── core/               # Settings, Config, Security, Database setup
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   ├── middlewares/        # [NEW] Custom Middlewares
│   │   ├── __init__.py
│   │   ├── logger.py       # Example: Log every request
│   │   └── timing.py       # Example: Calculate request process time
│   │
│   │
│   ├── utils/              # [NEW] Reusable helpers
│   │   ├── __init__.py
│   │   ├── jwt_helper.py   # JWT encoding/decoding logic
│   │   └── common.py       # Date formatting, random string gen, etc.
│   │
│   ├── constants/              # [NEW] Reusable helpers
│   │   ├── __init__.py
│   │   └── messages.py     # Centralized API response messages
│   │
│   ├── modules/            # The heart of your app (Grouped by Feature)
│   │   ├── auth/           # Login, JWT, Roles
│   │   ├── users/          # Student/Admin management
│   │   ├── exams/          # Exam creation, questions, constraints
│   │   ├── evaluation/     # Auto-grading logic
│   │   └── ai_engine/      # [Future] AI proctoring & insights models
│   │
│   ├── services/           # External integrations
│   │   ├── s3.py           # File storage logic
│   │   ├── compiler.py     # Interface for code compilation
│   │   └── email.py
│   │
│   ├── api/                # Route definitions (connects modules to URLs)
│   │   └── v1/
│   │       ├── api.py      # Main router
│   │       └── ...
│   │
│   └── main.py             # Entry point
│
├── tests/                  # Unit and Integration tests
├── alembic/                # DB Migrations (PostgreSQL)
├── requirements.txt
├── .env
├── .gitignore
└── Dockerfile
```