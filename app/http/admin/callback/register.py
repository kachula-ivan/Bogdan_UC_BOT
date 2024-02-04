from aiogram import F, Router
from aiogram.types import CallbackQuery

from database.commands import db
from database.migrations import user as User
from keyboartds.inline import decline_register_accept, new_user

router = Router()


@router.callback_query(F.data.startswith('register:'))
async def register(call: CallbackQuery):
    try:
        telegram_id = call.data[len('register:'):]
        user = await db.get_user(int(telegram_id))

        await db.update_user(int(telegram_id), {'status': User.STATUS_REGISTER})

        try:
            await call.bot.send_message(int(telegram_id), f'✅ Поздравляем! Ваши данные для входа:\n'
                                                          f'Логин: <code>{user.login}</code>\n'
                                                          f'Пароль: <code>{user.password}</code>')
        except:
            pass

        await call.message.answer(f'Данные отправлены пользователю: @{call.from_user.username}\n')
        await call.message.delete()
    except:
        await call.message.answer('Неизвестная ошибка. Напиши Вани')


@router.callback_query(F.data.startswith('unregister:'))
async def unregister(call: CallbackQuery):
    try:
        telegram_id = call.data[len('unregister:'):]

        await call.message.edit_text('Точно?')
        await call.message.edit_reply_markup(str(call.message.message_id), decline_register_accept(telegram_id))
    except:
        await call.message.answer('Неизвестная ошибка. Напиши Вани')


@router.callback_query(F.data.startswith('decline_register:'))
async def decline_register(call: CallbackQuery):
    try:
        telegram_id = call.data[len('decline_register:'):]

        await db.update_user(int(telegram_id), {'status': User.STATUS_DECLINED})

        try:
            await call.bot.send_message(int(telegram_id), f'❌ Вам отказано в регистрации')
        except:
            pass

        await call.message.answer('Отказано')
        await call.message.delete()
    except:
        await call.message.answer('Неизвестная ошибка. Напиши Вани')


@router.callback_query(F.data.startswith('accept_register:'))
async def accept_register(call: CallbackQuery):
    try:
        telegram_id = call.data[len('accept_register:'):]
        user = await db.get_user(int(telegram_id))

        await call.message.edit_text(f'🪪 Новый шанс пользователя: \n'
                                     f'first_name: <b>{user.first_name}</b>\n'
                                     f'last_name: <b>{user.last_name}</b>\n'
                                     f'username: @{user.username}')
        await call.message.edit_reply_markup(str(call.message.message_id), new_user(user.telegram_id))
    except:
        await call.message.answer('Неизвестная ошибка. Напиши Вани')
