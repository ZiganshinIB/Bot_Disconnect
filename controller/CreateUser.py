
## message.chat.id
## message.from_user.id, message.from_user.first_name, message.from_user.full_name,

from aiogram import types
from aiogram.dispatcher import FSMContext

from template import keyboards, text, StatesTemplate
from model import DataFacade
from controller.Observer import *


async def start_create_process(message: types.Message, bot) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=text.create_name_profile,
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await StatesTemplate.ProfileStatesGroup.name.set()


async def load_description(message: types.Message, state: FSMContext, bot) -> None:
    async with state.proxy() as data:
        data["gender"] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text="Расскажи о себе",
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await StatesTemplate.ProfileStatesGroup.next()


async def load_user(message: types.Message, state: FSMContext, bot) -> None:
    async with state.proxy() as data:
        data["description"] = message.text
        data[""]
        await notify(['SUPER_ADMIN'], data, bot)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Мы сообрали информацию",
                           parse_mode="HTML")
    await DataFacade.add_user(message.from_user.id, **data)
    await state.finish()
