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


def main():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="💰 Прайс лист 📜"),
            ],
            [
                KeyboardButton(text="👤 Аккаунт"),
                KeyboardButton(text="📊 Статистика"),
            ],
        ],
        resize_keyboard=True,
    )
