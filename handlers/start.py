from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🌹 Baga nagaan dhuftan gara AhmedPromotionBot!\n\n"
        "📢 Promotion fi Bulchiinsa Channel irratti isin tajaajilla."
    )
