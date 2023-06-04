
## message.chat.id
## message.from_user.id, message.from_user.first_name, message.from_user.full_name,

from aiogram import types
from aiogram.dispatcher import FSMContext

import applog
from template import keyboards, text, StatesTemplate
from model import DataFacade
from controller.Observer import *
log = applog.get_logger('CreateUser')

async def user_start_create(message, bot):
    await bot.send_message(chat_id=message.from_user.id,
                           text=text.create_city_profile,
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await StatesTemplate.ProfileStatesGroup.city.set()


async def user_load_city(message: types.Message, state, bot):
    async with state.proxy() as data:
        data["city"] = message.text
        if message.from_user.first_name:
            await StatesTemplate.ProfileStatesGroup.next()
            data["name"] = message.from_user.first_name
        else:
            log.info("Нет имени у пользоавтеля ")
            await bot.send_message(chat_id=message.from_user.id,
                                   text=text.create_name_profile,
                                   parse_mode="HTML",
                                   reply_markup=keyboards.get_cancel_profile_kb())
            await StatesTemplate.ProfileStatesGroup.next()
        if message.from_user.last_name:
            await StatesTemplate.ProfileStatesGroup.next()
            data["last_name"] = message.from_user.last_name
        else:
            data["last_name"] = None
            await StatesTemplate.ProfileStatesGroup.next()
        if message.from_user.username:
            await StatesTemplate.ProfileStatesGroup.next()
            data["username"] = message.from_user.username
        else:
            data["username"] = None
            await StatesTemplate.ProfileStatesGroup.next()
    await bot.send_message(chat_id=message.from_user.id,
                           text=text.create_company_profile,
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await StatesTemplate.ProfileStatesGroup.next()



async def user_load_company(message, state, bot):
    async with state.proxy() as data:
        data["company"] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text=text.create_deportment_profile,
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await StatesTemplate.ProfileStatesGroup.next()


async def user_load_deportment(message, state, bot):
    async with state.proxy() as data:
        data["deportment"] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text=text.create_position_profile,
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await StatesTemplate.ProfileStatesGroup.next()


async def user_load_position(message, state, bot):
    async with state.proxy() as data:
        data["position"] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text=text.create_description_profile,
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await StatesTemplate.ProfileStatesGroup.next()


async def user_load_description(message, state, bot):
    async with state.proxy() as data:
        data["description"] = message.text
        await notify_new_user(message.from_user.id, data, bot)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Спасибо жди ответа ",
                           parse_mode="HTML",
                           reply_markup=keyboards.get_cancel_profile_kb())
    await state.finish()

