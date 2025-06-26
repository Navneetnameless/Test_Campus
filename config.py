from dotenv import load_dotenv
import os

load_dotenv()

env_vars = {
    "API_HASH": os.getenv("API_HASH", ""),
    "API_ID": os.getenv("API_ID", ""),
    "BOT_TOKEN": os.getenv("BOT_TOKEN", ""),
    "MONGO_URI": os.getenv("MONGO_URI", "mongodb+srv://Yuuichi:Yuuichi@cluster0.z3hyhbb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"),  # ✅ Add this
    "CACHE_CHANNEL": os.getenv("CACHE_CHANNEL", "Dump2075"),
    "CHANNEL": os.getenv("CHANNEL", "Manga_Campus"),
    "FNAME": os.getenv("FNAME", "[MC] [{chap_num}] {chap_name} @Manga_Campus")
}

dbname = os.getenv("MONGO_DB_NAME", "manga")  # ✅ Optional: can pass db name separately
