from database.migrations.user import User


async def add_user(user):
    return await User.create(**user)


async def select_user(telegram_id):
    return await User.query.where(User.telegram_id == telegram_id).gino.first()
