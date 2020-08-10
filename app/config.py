import os
import dotenv


dotenv.load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_DEBUG = True

WEBHOOK_HOST = ""
WEBHOOK_PORT = ""
WEBHOOK_PATH = ""
WEBHOOK_URL = ""
