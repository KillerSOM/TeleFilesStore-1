# (c) @AbirHasan2005

import os


class Config:
	API_ID = int(os.environ.get("API_ID", "22466557"))
	API_HASH = os.environ.get("020e8aa708282ed9b5210d84ba374736")
	BOT_TOKEN = os.environ.get("7136288796:AAH6CWn7TIVxR8F7TUxVlrkxRIiQI606NXk")
	BOT_USERNAME = os.environ.get("Sanji_Test_Robot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001957744474"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5297903100"))
	DATABASE_URL = os.environ.get("mongodb+srv://killersom72:<password>@sanjifilestore.x6rhkdi.mongodb.net/?retryWrites=true&w=majority&appName=SanjiFileStore")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001957744474")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", -1001957744474)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	
