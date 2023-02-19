
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from model.sqlite import *
from template import keyboards,text
import config

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    name = State()
    gender = State()
    description = State()


async def on_startup(_):
    await db_start()
    print("Start up")


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(text=text.start_message,
                         parse_mode="HTML",
                         reply_markup=keyboards.get_create_profile_kb())


@dp.message_handler(commands=['create_profile'])
async def cmd_create(message: types.Message) -> None:
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


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)