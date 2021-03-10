from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("DISCORD_TOKEN")
OWNER_ID = getenv("OWNER_ID")
TARGET_ID = getenv("TARGET_ID")