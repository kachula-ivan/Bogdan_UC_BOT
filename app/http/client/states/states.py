from aiogram.fsm.state import StatesGroup, State


class Auth(StatesGroup):
    login = State()
    password = State()
    check = State()


class SetPubgId(StatesGroup):
    enter = State()
    validate = State()
