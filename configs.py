# (c) @Rudraa2213

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "9126459"))
	API_HASH = os.environ.get("API_HASH", "238c912d48a9ec0d0e8b05738f358ffc")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","6178143777:AAEic5dv9NkEamdhNBBtz0QGEGpDKvXaVkc")
	BOT_USERNAME = os.environ.get("BOT_USERNAME",'Content_StoreBot')
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL",'-1001846148083'))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "746480452"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Rudraa:Rudraa2213@cluster0.tj0kh3c.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001754712475")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
I Am Rudraa's **Content Store Bot**! \nYou Can Send Me Any Media file, And I Will give you a Permanent Sharable Link\nAlso Please join my channel And Support Group!


🤖 **My Name:** [Content Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Mogenius](https://mogenius.com/)

😎 **Developer:** @Rudraa332

👥 **Support Group:** [RRR](https://t.me/joint0t)

📢 **Updates Channel:** [Discovery Projects](https://t.me/bot_channelv1)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Rudraa332

Developer is noob😒. And Learning from Official docs. Please donate the Developer for Keeping the Service Alive.

Also remember that developer will Not Forbid for Adult Contents This Bot Is fully free for your Use. So Keep use this.

[Rudraa](https://www.telegram.me/rudraa332) (Contect Me)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **Content Store Bot**.

Send Any Type Of Data And I Will Send You A Permanent Sharable Link. 
I also have support channel ! Please Check __**About Bot**__ Button.
"""
