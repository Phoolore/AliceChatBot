from os import environ
from asyncio import get_event_loop
from logging import basicConfig, INFO

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

bot = Bot(
    environ.get("TOKEN"),
    parse_mode = "HTML"
)
dp = Dispatcher()

async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    basicConfig(lavel = INFO)
    loop = get_event_loop()
    loop.run_utils_complete(main())