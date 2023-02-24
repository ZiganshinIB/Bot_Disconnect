import aiogram

import applog
from model import DataFacade
from aiogram import types
from controller import Observer

log = applog.get_logger('Test')


async def access_write(message: types.Message, bot: aiogram.Bot):
    flag = await DataFacade.is_access(message.from_user.id, "WRITER_disconnect_chat")
    if not flag:
        await Observer.notify_access_error(access_name='WRITER_disconnect_chat', message=message, bot=bot)
        await bot.delete_message(message.chat.id, message.message_id)


async def new_member(message: types.Message, bot):
    if await DataFacade.is_access(message.from_user.id, "READER_disconnect_chat"):
        text = f'<b>Добро пожаловать {message.from_user.username}  в Чат</b> Чат не для работы, а для Души '
        await bot.send_message(chat_id=message.from_user.id,
                               text=text,
                               parse_mode="HTML")
    await Observer.notify_access_error(access_name='READER_disconnect_chat', message=message, bot=bot)
    await bot.ban_chat_member(message.chat.id, message.from_user.id)
