from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.http.client.states.states import Auth
from database.commands import db
from database.migrations import user as User
from keyboartds.default import auth

router = Router()
flags = {"throttling_key": "default"}


@router.message(F.text.startswith('💻 Логин 🔐'), flags=flags)
async def login(message: Message, state: FSMContext):
    await state.set_state(Auth.login)
    await message.answer('Логин:')


@router.message(Auth.login, flags=flags)
async def password(message: Message, state: FSMContext):
    await state.update_data(LOGIN=message.text)
    await state.set_state(Auth.password)
    await message.answer('Пароль:')


@router.message(Auth.password, flags=flags)
async def password(message: Message, state: FSMContext):
    await state.update_data(PASSWORD=message.text)
    await state.set_state(Auth.check)

    user = await db.get_user(message.from_user.id)
    data = await state.get_data()

    if data['LOGIN'].isdigit() and user.login == int(data['LOGIN']) and user.password == data['PASSWORD']:
        await db.update_user(user.telegram_id, {'status': User.STATUS_ACTIVE})
        await message.answer('✅ Вы вошли в аккаунт\nДля выхода, нажмите на /logout')
    else:
        await message.answer('Неверный логин или пароль!', reply_markup=auth())


@router.message(Command('logout'), flags=flags)
async def logout(message: Message):
    user = await db.get_user(message.from_user.id)
    await db.update_user(user.telegram_id, {'status': User.STATUS_LOGOUT})
    await message.answer('Вы вышли из аккаунта!', reply_markup=auth())
