from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv("DISCORD_TOKEN")
OWNER_ID = getenv("OWNER_ID")
ADMIN_ID = getenv("ADMIN_ID").split()