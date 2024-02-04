from aiogram.filters import Filter
from aiogram.types import Message

from database.commands import db
from database.migrations.user import STATUS_ACTIVE


class IsActive(Filter):
    key = 'is_active'

    async def __call__(self, message: Message) -> bool:
        try:
            user = await db.get_user(message.from_user.id)

            return True if user.status == STATUS_ACTIVE else False
        except:
            return False