from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

from database.commands import db
from database.migrations import user as User

from keyboartds.default import auth

router = Router()
flags = {"throttling_key": "default"}


@router.message(Command('start'), flags=flags)
async def cmd_start(message: Message):
    if message.chat.type == 'private':
        # try:
        user = await db.select_user(message.from_user.id)
        if not user or user.status != User.STATUS_ACTIVE:
            # await db.add_user({
            #     'telegram_id': message.from_user.id,
            #     'username': message.from_user.username,
            #     'status': user.STATUS_UNREGISTER,
            # })
            #
            await message.answer(('👇'), reply_markup=auth())
        else:
            await message.answer(('ти зареган'))
    # except: await message.answer(('❗ Бот розроблений для кожного особисто, не можна його добавляти в групи.
    # Поспілкуйтесь з ним самі: @trx_games_bot\nЯкщо у вас виникли інші проблеми, звертайтесь до нашого менеджера:
    # @Christooo1'))
    else:
        await message.answer((
                                 '❗ Бот розроблений для кожного особисто, не можна його добавляти в групи. '
                                 'Поспілкуйтесь з ним самі: @trx_games_bot\nЯкщо у вас виникли інші проблеми, '
                                 'звертайтесь до нашого менеджера: @Christooo1'))
