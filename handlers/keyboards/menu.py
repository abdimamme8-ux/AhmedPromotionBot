from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📢 Promotion")],
        [KeyboardButton(text="📚 Channelota Barnootaa")],
        [KeyboardButton(text="👥 Gareewwan")],
        [KeyboardButton(text="ℹ️ Waa'ee Bot")],
        [KeyboardButton(text="📞 Nu Qunnami")]
    ],
    resize_keyboard=True
)
