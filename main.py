<<<<<<< HEAD
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
=======
>>>>>>> parent of d73ff5b (REFRACT)

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
<<<<<<< HEAD
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ContentType
=======
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
>>>>>>> parent of d73ff5b (REFRACT)
from aiogram.utils.callback_data import CallbackData
import applog

<<<<<<< HEAD
from controller import CreateUser, WorkUser, MessageChat
from model.sqlite import *
from model.sqlite import _db_start_
from template import keyboards, text, StatesTemplate
=======
from model.sqlite import *
from template import keyboards,text
>>>>>>> parent of d73ff5b (REFRACT)
import config


storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
log = applog.get_logger('Test')
print(type(log))


<<<<<<< HEAD
async def on_startup(dp):
    await bot.set_webhook(config.WEBHOOK_URL)
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
=======
class ProfileStatesGroup(StatesGroup):
    name = State()
    gender = State()
    description = State()


async def on_startup(_):
    await db_start()
    print("Start up")


@dp.message_handler(commands=['start'])
>>>>>>> parent of d73ff5b (REFRACT)
async def cmd_start(message: types.Message) -> None:
    await message.answer(text=text.start_message,
                         parse_mode="HTML",
                         reply_markup=keyboards.get_create_profile_kb())

# ------------------------------- UserProfile ------------------------------- #


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['create_profile'])
async def cmd_create(message: types.Message) -> None:
<<<<<<< HEAD
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
=======
    await bot.send_message(chat_id=message.from_user.id,
                           text=text.create_name_profile,
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await create_profile(message.from_user.id)
    await ProfileStatesGroup.name.set()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    print("...")
    async with state.proxy() as data:
        data["name"] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text="Укажите пол",
                           parse_mode="HTML",
                           reply_markup=keyboards.get_create_gender_kb())
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.gender)
async def load_name(message: types.Message, state: FSMContext) -> None:
    print("...")
    async with state.proxy() as data:
        data["gender"] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text="Расскажи о себе",
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.description)
async def load_name(message: types.Message, state: FSMContext) -> None:
    print(message.from_user)
    user_info = ''
    async with state.proxy() as data:
        data["description"] = message.text
        user_info = f"Мы сообрали информацию {data['name']} ({message.from_user.full_name} - {message.from_user.username} - {message.from_user.id})\n. Описание:{message.text} "
    await bot.send_message(chat_id=message.from_user.id,
                           text="Мы сообрали информацию",
                           parse_mode="HTML")
    await edit_profile(state=state, user_id=message.from_user.id)
    await bot.send_message(chat_id=config.SUPER_ADMIN_ID,
                           text=user_info,
                           parse_mode="HTML")
    await state.finish()
>>>>>>> parent of d73ff5b (REFRACT)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['add_username_in_access'])
async def cmd_add_access(message: types.Message):
    await WorkUser.add_username_in_access(message=message, bot=bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['add_userid_in_access'])
async def cmd_add_access(message: types.Message):
    await WorkUser.add_userid_in_access(message=message, bot=bot)



@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['add_username_in_role'])
async def cmd_add_role(message: types.Message):
    await WorkUser.add_user_in_role(message=message, bot=bot)


@dp.message_handler(lambda message: message.chat.id == message.from_user.id, commands=['info_user'])
async def cmd_info_user(message: types.Message):
    await WorkUser.info_user(message, bot)
    pass
# *****************************************************--_USER_--***************************************************** #

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup
    )
