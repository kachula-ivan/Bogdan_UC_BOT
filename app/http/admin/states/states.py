from aiogram.fsm.state import StatesGroup, State


class Mailing(StatesGroup):
    type = State()
    accept = State()
    send = State()


class AddPrice(StatesGroup):
    uc = State()
    sum = State()
