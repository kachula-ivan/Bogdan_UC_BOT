from os import getenv

from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

storage = MemoryStorage()
TOKEN = str(getenv("BOT_TOKEN"))

PG_DATABASE = str(getenv("PG_DATABASE"))
PG_USER = str(getenv("PG_USER"))
PG_PASSWORD = str(getenv("PG_PASSWORD"))
PG_HOST = str(getenv("PG_HOST"))

ADMIN_TELEGRAM_ID = int(getenv("ADMIN_TELEGRAM_ID"))
CHAT_TELEGRAM_ID = int(getenv("CHAT_TELEGRAM_ID"))

THROTTLE_TIME = int(getenv("THROTTLE_TIME"))
