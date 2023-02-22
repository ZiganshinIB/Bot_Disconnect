# ⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿
# ⣿⣿⡟⠀⠀⠀⠀⠀⠉⠙⠿⣿⣿⣿⡿⢿⣿⣿⣿⠿⠋⠉⠀⢀⣀⠀⠀⢻⣿⣿
# ⣿⣿⠃⠀⢸⣿⣿⣶⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢶⣾⣿⣿⣇⠀⠘⣿⣿
# ⣿⣿⠀⠀⣼⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⠀⠀⣿⣿
# ⣿⣿⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⣿⣿
# ⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
# ⣿⠃⠀⠀⣀⣤⣶⣶⣶⣾⣷⣶⣦⡀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠘⣿
# ⠇⠀⣠⣾⣿⣿⣿⣿⡏⠉⢹⣿⣿⣷⠀⠀⣾⣿⣿⡏⠉⢹⣿⣿⣿⣿⣷⣄⠀⠘
# ⢀⣼⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⠏⠀⠀⠹⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣷⡀
# ⣼⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠈⠙⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣧
# ⣻⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⢶⣶⣶⡶⠂⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⣿⣿⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿


from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData


from controller import CreateUser
from model.sqlite import *
from template import keyboards, text, StatesTemplate
import config

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


async def on_startup(_):
    await db_start()
    print("Start up")


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    if state is None:
        return
    await state.finish()
    await message.reply("Вы прервали создание анкеты",
                        reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(text=text.start_message,
                         parse_mode="HTML",
                         reply_markup=keyboards.get_create_profile_kb())


@dp.message_handler(commands=['create_profile'])
async def cmd_create(message: types.Message) -> None:
    # if test#
    await CreateUser.start_create_process(message, bot=bot)


@dp.message_handler(state=StatesTemplate.ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    await CreateUser.load_name(message, state, bot)


@dp.message_handler(state=StatesTemplate.ProfileStatesGroup.gender)
async def load_description(message: types.Message, state: FSMContext) -> None:
    await CreateUser.load_description(message, state, bot)


@dp.message_handler(state=StatesTemplate.ProfileStatesGroup.description)
async def load_user(message: types.Message, state: FSMContext) -> None:
    await CreateUser.load_user(message, state, bot)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)