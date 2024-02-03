from database.migrations.user import User


async def add_user(user):
    return await User.create(**user)


async def get_user(telegram_id):
    return await User.query.where(User.telegram_id == telegram_id).gino.first()


async def get_users(field=False, value=False):
    if field and value:
        return await User.query.where(field == value).gino.all()

    return await User.query.gino.all()


async def update_user(telegram_id, new_data):
    user = await get_user(telegram_id)

    if user:
        await user.update(**new_data).apply()
        return True
    else:
        return False