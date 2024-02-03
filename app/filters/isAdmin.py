from aiogram.filters import Filter
from aiogram.types import Message

import config


class IsAdmin(Filter):
    key = 'is_admin'

    async def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) in config.ADMINS
