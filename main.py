from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.menu import main_menu

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🌹 Baga nagaan dhuftan gara AhmedPromotionBot!\n\n"
        "📢 Mee menu keessaa filannoo tokko filadhaa.",
        reply_markup=main_menu
    )
