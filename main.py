import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.admin import router as admin_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    dp.include_router(admin_router)
    print("AhmedPromotionBot hojii jalqabe...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
