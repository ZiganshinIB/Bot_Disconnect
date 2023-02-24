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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ContentType
from aiogram.utils.callback_data import CallbackData
import applog

from controller import CreateUser, WorkUser, MessageChat
from model.sqlite import *
from model.sqlite import _db_start_
from template import keyboards, text, StatesTemplate
import config

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
log = applog.get_logger('Test')
print(type(log))


async def on_startup(_):
    await _db_start_()
    log.info("Start")


@dp.message_handler(lambda message: message.chat.id == -1001321018780, content_types=[ContentType.NEW_CHAT_MEMBERS])
async def new_member_chat(message: types.Message) -> None:
    await MessageChat.new_member(message, bot)


@dp.message_handler(lambda message: -1001321018780 == message.chat.id,)
async def message_chat_disconnect(message: types.Message) -> None:
    await MessageChat.access_write(message, bot)


# *****************************************************--_USER_--***************************************************** #
@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['cancel'], state='*')
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    if state is None:
        return
    await state.finish()
    await message.reply("Вы прервали",
                        reply_markup=ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(text=text.start_message,
                         parse_mode="HTML",
                         reply_markup=keyboards.get_create_profile_kb())

# ------------------------------- UserProfile ------------------------------- #


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['create_profile'])
async def cmd_create(message: types.Message) -> None:
    # if test#
    await CreateUser.user_start_create(message, bot=bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, state=StatesTemplate.ProfileStatesGroup.city)
async def load_city(message: types.Message, state: FSMContext) -> None:
    await CreateUser.user_load_city(message, state, bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, state=StatesTemplate.ProfileStatesGroup.company)
async def load_company(message: types.Message, state: FSMContext) -> None:
    await CreateUser.user_load_company(message, state, bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, state=StatesTemplate.ProfileStatesGroup.deportment)
async def load_deportment(message: types.Message, state: FSMContext) -> None:
    await CreateUser.user_load_deportment(message, state, bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, state=StatesTemplate.ProfileStatesGroup.position)
async def load_position(message: types.Message, state: FSMContext) -> None:
    await CreateUser.user_load_position(message, state, bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, state=StatesTemplate.ProfileStatesGroup.description)
async def load_description(message: types.Message, state: FSMContext) -> None:
    await CreateUser.user_load_description(message, state, bot)
    log.info(f'ползователь зарегалься {message.from_user.id}')


# ----------------------------- UserProfile END ----------------------------- #


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['add_username_in_access'])
async def cmd_add_access(message: types.Message):
    await WorkUser.add_username_in_access(message=message, bot=bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['add_username_in_role'])
async def cmd_add_role(message: types.Message):
    await WorkUser.add_user_in_role(message=message, bot=bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['info_user'])
async def cmd_info_user(message: types.Message):
    await WorkUser.info_user(message, bot)
    pass
# *****************************************************--_USER_--***************************************************** #

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)