from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileStatesGroup(StatesGroup):
    city = State()
    company = State()
    deportment = State()
    position = State()
    description = State()
