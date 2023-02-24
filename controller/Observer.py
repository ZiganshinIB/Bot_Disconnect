import aiogram

from model import DataFacade
from aiogram import types
from aiogram.dispatcher import FSMContext

from template import keyboards, text, StatesTemplate
from model import DataFacade


async def notify_new_user(user_id: str, data: dict, bot) -> None:
    await DataFacade.add_user(user_id, **data)
    inf = f"<b>Регистрируется</b> {user_id}. Пользователь: {data['name']}\n Город: {data['city']} \n Компание: {data['company']}\n Отдел: {data['deportment']} \n Должность: {data['position']} \n Описание: {data['description']}"
    for user in await DataFacade.get_user_id_role("USER_Viewer"):
        await bot.send_message(chat_id=user["id"],
                               text=inf,
                               parse_mode="HTML")


async def notify_error_command(command: str, message: types.Message, error_message: str, bot):
    inf = f"Произошла ошибка в команде {command}\n" \
          f"от пользователя {message.from_user.id} - {message.from_user.username}\n" \
          f"пользователь ввел сообщение: {message.text}\n" \
          f"Ошибка:{error_message}"
    for user in await DataFacade.get_user_id_role("ERROR_Viewer"):
        await bot.send_message(chat_id=user['id'],
                               text=inf,
                               parse_mode="HTML")


async def notify_access_error(access_name: str, message: types.Message, bot: aiogram.Bot):
    inf = f"Пользователь {message.from_user.username}\n" \
          f"пытается воспользоватся группой доступа: \n" \
          f"{access_name}"
    for user in (await DataFacade.get_user_id_role("ACCESS_handler")):
        await bot.send_message(chat_id=user['id'],
                               text=inf,)


async def notify_new_user_access(user: dict, access: dict, message: types.Message, bot: aiogram.Bot):
    inf = f"Вам добавили группу доступа <b>{access['access_name']}</b> \n" \
          f"Описание: {access['description']}"
    await bot.send_message(chat_id=user['id'],
                           text=inf,
                           parse_mode="HTML")