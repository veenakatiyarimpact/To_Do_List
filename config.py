import os

# Best practice: Use environment variables, fallback to defaults for local dev
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password_here")
DB_NAME = os.getenv("DB_NAME", "todo_db")
