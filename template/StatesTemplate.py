from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileStatesGroup(StatesGroup):
    city = State()
    name = State()
    last_name = State()
    username = State()
    company = State()
    deportment = State()
    position = State()
    description = State()
