from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileStatesGroup(StatesGroup):
    name = State()
    gender = State()
    description = State()