env_vars = {
  # Get From my.telegram.org
  "API_HASH": "057fd0be9d7c38526b143c582bceb24b",
  # Get From my.telegram.org
  "API_ID": "20445873",
  #Get For @BotFather
  "BOT_TOKEN": "7857406628:AAGT41Xak2UxFaIFDCAGYEq4uh-lt6NkFRY",
  # Get For tembo.io
  
  "DATABASE_URL_PRIMARY": "mongodb+srv://Yuuichi:Yuuichi@cluster0.z3hyhbb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "[MC] [{chap_num}] {chap_name} @Manga_Campus"
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL')
