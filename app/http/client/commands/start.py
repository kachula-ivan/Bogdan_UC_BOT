import datetime
import random
import string

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

import config
from bot import bot
from database.commands import db
from database.migrations import user as User

from keyboartds.default import auth, main
from keyboartds.inline import new_user

router = Router()
flags = {"throttling_key": "default"}


@router.message(Command('start'), flags=flags)
async def start(message: Message):
    # try:
    user = await db.get_user(message.from_user.id)
    if user is None:
        letters = string.ascii_uppercase

        user = await db.add_user({
            'telegram_id': message.from_user.id,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'username': message.from_user.username,
            'login': random.randint(10000, 99999),
            'password': ''.join(random.choice(letters) for i in range(6)),
            'status': User.STATUS_UNREGISTER,
            'role': User.ROLE_USER,
            'created_at': datetime.datetime.now(),
        })

        await bot.send_message(config.CHAT_TELEGRAM_ID, (f'🪪 Новый пользователь: \n'
                                                         f'first_name: <b>{message.from_user.first_name}</b>\n'
                                                         f'last_name: <b>{message.from_user.last_name}</b>\n'
                                                         f'username: @{message.from_user.username}'),
                               reply_markup=new_user(user.telegram_id))

        await message.answer('👇', reply_markup=auth())

    elif user.status != User.STATUS_ACTIVE:
        await message.answer('Войдите в аккаунт', reply_markup=auth())

    else:
        await message.answer('🔝 Главное меню', reply_markup=main())

# except: await message.answer(('❗ Бот розроблений для кожного особисто, не можна його добавляти в групи.
# Поспілкуйтесь з ним самі: @trx_games_bot\nЯкщо у вас виникли інші проблеми, звертайтесь до нашого менеджера:
# @Christooo1'))
