from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def empty() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
            ]
        ],
    )


def new_user(telegram_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅", callback_data=f"register:{telegram_id}"),
                InlineKeyboardButton(text="❌", callback_data=f"unregister:{telegram_id}"),
            ]
        ],
    )


def mailing_send() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅", callback_data=f"mailing_send:accept"),
                InlineKeyboardButton(text="❌", callback_data=f"mailing_send:cancel"),
            ]
        ],
    )


def decline_register_accept(telegram_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Отказать", callback_data=f"decline_register:{telegram_id}"),
                InlineKeyboardButton(text="Вернуться назад", callback_data=f"accept_register:{telegram_id}"),
            ]
        ],
    )


def profile() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Установить PUBG ID", callback_data=f"set_pubg_id"),
            ]
        ],
    )
