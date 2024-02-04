from database.migrations.orders import Order
from database.migrations.price import Price
from database.migrations.user import User


async def add_user(user):
    return await User.create(**user)


async def add_model(model, data):
    return await model.create(**data)


async def get_model(model, model_id):
    return await model.query.where(model.id == model_id).gino.first()


async def get_models(model):
    return await model.query.gino.all()


async def update_model(model, model_id, new_data):
    some_model = await get_model(model, model_id)

    if some_model:
        await some_model.update(**new_data).apply()
        return True
    else:
        return False


async def get_user(telegram_id):
    return await User.query.where(User.telegram_id == telegram_id).gino.first()


async def find_user(user_id):
    return await User.query.where(User.id == user_id).gino.first()


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


async def get_prices():
    return await Price.query.order_by(Price.sum).gino.all()


async def get_order(order_id):
    return await Order.load(user=User).query.where(Order.id == order_id).gino.first()

