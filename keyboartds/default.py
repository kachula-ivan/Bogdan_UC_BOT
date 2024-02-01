from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def auth():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="💻 Логин 🔐"),
            ],
            [
                KeyboardButton(text="📝📋 Регистрация 🖋️🔒"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
