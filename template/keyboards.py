from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


def get_create_profile_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b_create = KeyboardButton(text="/create_profile")
    kb.add(b_create)
    return kb


def get_cancel_profile_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b_cancel = KeyboardButton(text="/cancel_profile")
    kb.add(b_cancel)
    return kb


def get_create_gender_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b_men = KeyboardButton(text="Муж.")
    b_women = KeyboardButton(text="Жен.")
    kb.add(b_men)
    kb.insert(b_women)
    return kb
