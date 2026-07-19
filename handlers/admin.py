from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMINS

router = Router()


@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id not in ADMINS:
        await message.answer("❌ Ati admin miti.")
        return

    await message.answer(
        "👨‍💼 AhmedPromotionBot Admin Panel\n\n"
        "📢 /broadcast - Ergaa erguu\n"
        "📚 /channels - Channel bulchuu\n"
        "📊 /stats - Lakkoofsa ilaalu"
    )
