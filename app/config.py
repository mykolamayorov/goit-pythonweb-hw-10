import os
from dotenv import load_dotenv

load_dotenv()

# --- Database ---
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mysecretpassword")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "postgres")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# --- JWT ---
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "CHANGE_ME")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_ACCESS_TOKEN_EXPIRES_MINUTES = os.getenv("JWT_ACCESS_TOKEN_EXPIRES_MINUTES", "30")

# --- Email (Mailtrap / SMTP) ---
SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = os.getenv("SMTP_PORT", "587")
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
MAIL_FROM = os.getenv("MAIL_FROM", "noreply@example.com")
APP_BASE_URL = os.getenv("APP_BASE_URL", "http://localhost:8000")

# --- CORS ---
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "")

# --- Rate limit for /me ---
ME_RATE_LIMIT = os.getenv("ME_RATE_LIMIT", "5/minute")

# --- Cloudinary ---
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME", "")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY", "")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET", "")
