import os
import asyncio
import itertools

from datetime import datetime
from dotenv import load_dotenv

from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TimedOut

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "6518216142"
MESSAGES = [
    "BICEP CURL 💪",
    "PUSHUPS 🫸",
    "LEGS 🦵"
]

START_HOUR = 10
END_HOUR = 23
SKIPPED_DAYS = [4, 5]

MESSAGE_TIMER = 60 * 60    # 1 Hour

async def periodic_sender(bot: Bot):
    await bot.send_message(chat_id=CHAT_ID, text="Bot Updated!")
    messages_cycler = itertools.cycle(MESSAGES)

    while True:
        try:
            now = datetime.now()
            weekday = now.weekday()
            if weekday not in SKIPPED_DAYS and START_HOUR <= now.hour <= END_HOUR:
                await bot.send_message(chat_id=CHAT_ID, text=next(messages_cycler))
            await asyncio.sleep(MESSAGE_TIMER)
        except Exception as e:
            print(e)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).read_timeout(30).write_timeout(30).connect_timeout(30).build()
    print("Bot up and running :)")

    asyncio.run(periodic_sender(app.bot))

if __name__ == "__main__":
    main()

