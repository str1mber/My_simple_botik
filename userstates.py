from aiogram.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    BASE = State()
    CREATING_PARI = State()
    PARI_CREATED = State()
    SETTING_PARI_TAKER = State()