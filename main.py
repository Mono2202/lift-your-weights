import os
import asyncio

from datetime import datetime
from dotenv import load_dotenv

from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "6518216142"
MESSAGE="Webhook worked!"

START_HOUR = 10
END_HOUR = 23
SKIPPED_DAYS = [4, 5]

async def periodic_sender(bot: Bot):
    while True:
        now = datetime.now()
        weekday = now.weekday()
        #if weekday not in SKIPPED_DAYS and START_HOUR <= now.hour < END_HOUR:
        await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)
        await asyncio.sleep(60 * 30)  # Wait 30 minutes

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    print("Bot up and running :)")

    asyncio.run(periodic_sender(app.bot))

if __name__ == "__main__":
    main()

