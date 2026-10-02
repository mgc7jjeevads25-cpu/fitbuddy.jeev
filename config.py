import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"
EXAMPLE_ENV_FILE = BASE_DIR / ".env.example"

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
elif EXAMPLE_ENV_FILE.exists():
    load_dotenv(EXAMPLE_ENV_FILE)

DEFAULT_DB_PATH = (BASE_DIR / "fitbuddy.db").resolve().as_posix()
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DB_PATH}")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "").strip()

# Keep these configurable because Gemini model names available to an API key can change.
# New Gemini API keys commonly require the newer 3.x flash models.
WORKOUT_MODEL = os.getenv("GEMINI_WORKOUT_MODEL", "gemini-3.8-flash")
TIP_MODEL = os.getenv("GEMINI_TIP_MODEL", "gemini-3.8-flash")

ADMIN_KEY = os.getenv("ADMIN_KEY", "").strip()
