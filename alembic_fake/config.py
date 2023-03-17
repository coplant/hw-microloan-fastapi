from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

DB_FAKE = os.environ.get("DB_FAKE")

DEFAULT_CHUNK_SIZE = 1024 * 1024 * 5
