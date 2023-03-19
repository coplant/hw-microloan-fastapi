from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DB_HOST = os.environ.get("FAKE_DB_HOST")
DB_PORT = os.environ.get("FAKE_DB_PORT")
DB_USER = os.environ.get("FAKE_DB_USER")
DB_PASS = os.environ.get("FAKE_DB_PASS")
DB_FAKE = os.environ.get("FAKE_DB_NAME")

DEFAULT_CHUNK_SIZE = 1024 * 1024 * 5
