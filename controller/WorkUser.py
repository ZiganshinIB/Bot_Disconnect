import aiogram

import applog
from model import DataFacade
from aiogram import types
from controller import Observer

log = applog.get_logger('Test')


async def info_user(message: types.Message, bot):
    if await DataFacade.is_access(message.from_user.id, 'ADMIN_user'):
        texts = message.text.split(' ')
        if len(texts) != 2:
            error_message = f"Ввели {len(texts) - 1} аргумент, а ожидалось 1"
            await Observer.notify_error_command(command=texts[0],
                                                message=message,
                                                error_message=error_message,
                                                bot=bot)
            log.error(f"User:{message.from_user.id} :: err:{error_message} ")
            await message.reply(f"Ошибка: {error_message}")
            return
        try:
            user = await DataFacade.get_user_id(texts[1])
            message_text = f"Пользователь: {user['name']}\n " \
                           f"Город: {user['city']}\n " \
                           f"Компание: {user['company']}\n " \
                           f"Отдел: {user['deportment']} \n " \
                           f"Должность: {user['position']} \n " \
                           f"Описание: {user['description']}"
            await bot.send_message(chat_id=message.from_user.id,
                                   text=message_text)
        except ValueError as e:
            error_message = f"запросили user_id: {texts[1]}, его нет в БД"
            await Observer.notify_error_command(command=texts[0],
                                                message=message,
                                                error_message=error_message,
                                                bot=bot)
            log.warning(f"Com:{texts[0]} :: User:{message.from_user.id} :: err:{error_message} ")
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text="нет Доступа",
                               parse_mode="HTML")
    return


async def add_username_in_access(message: types.Message, bot: aiogram.Bot):
    if await DataFacade.is_access(message.from_user.id, "ADMIN_Access"):
        texts = message.text.split(' ')
        if len(texts) != 3:
            error_message = f"Ввели {len(texts) - 1} аргумент, а ожидалось 2 (username, access_name)"
            await Observer.notify_error_command(command=texts[0],
                                                message=message,
                                                error_message=error_message,
                                                bot=bot)
            log.error(f"User:{message.from_user.id} :: err:{error_message} ")
            await message.reply(f"Ошибка: {error_message}")
            return
        try:
            users: list = await DataFacade.get_users(username=[texts[1]])
        except ValueError as e:
            error_message = f"запросили username: {texts[1]}, его нет в БД"
            await Observer.notify_error_command(command=texts[0],
                                                message=message,
                                                error_message=error_message,
                                                bot=bot)
            log.warning(f"Com:{texts[0]} :: User:{message.from_user.id} :: err:{error_message} ")
            return
        if len(users) > 1:
                await message.reply("таких 2 пользователя прошу вас воспользоваться другим анналогом команды")
                return
        user = users[0]
        try:
            access = await DataFacade.get_access(access_name=texts[2])
        except ValueError as e:
                await Observer.notify_error_command(command=texts[1],
                                                    message=message,
                                                    error_message=str(e),
                                                    bot=bot)
                log.info(e)
                return
        await DataFacade.add_user_access(user_id=user['id'], access_name=access['access_name'])
        await Observer.notify_new_user_access(user=user, access=access, message=message, bot=bot)
        await bot.send_message(chat_id=message.from_user.id,
                                   text="ОК")

    else:
        await Observer.notify_access_error(access_name="ADMIN_Grup",
                                           message=message,
                                           bot=bot)
        await message.reply(text="У вас нет доступа")


def add_userid_in_access(message: types.Message, bot: aiogram.Bot):
    if await DataFacade.is_access(message.from_user.id, "ADMIN_Access"):
        texts = message.text.split(' ')
        if len(texts) != 3:
            error_message = f"Ввели {len(texts) - 1} аргумент, а ожидалось 2 (user_id, access_name)"
            await Observer.notify_error_command(command=texts[0],
                                                message=message,
                                                error_message=error_message,
                                                bot=bot)
            log.error(f"User:{message.from_user.id} :: err:{error_message} ")
            await message.reply(f"Ошибка: {error_message}")
            return
        try:
            users: list = await DataFacade.get_users(user_id=[texts[1]])
            user = users[0]
        except ValueError as e:
            error_message = f"запросили user_id: {texts[1]}, его нет в БД"
            await Observer.notify_error_command(command=texts[0],
                                                message=message,
                                                error_message=error_message,
                                                bot=bot)
            log.warning(f"Com:{texts[0]} :: User:{message.from_user.id} :: err:{error_message} ")

        try:
           access = await DataFacade.get_access(access_name=texts[2])
        except ValueError as e:
            await Observer.notify_error_command(command=texts[1],
                                                message=message,
                                                error_message=str(e),
                                                bot=bot)
            log.info(e)
            return
        await DataFacade.add_user_access(user_id=user['id'], access_name=access['access_name'])
        await Observer.notify_new_user_access(user=user, access=access, message=message, bot=bot)
        await bot.send_message(chat_id=message.from_user.id,
                                text="ОК")

    else:
        await Observer.notify_access_error(access_name="ADMIN_Grup",
                                           message=message,
                                           bot=bot)
        await message.reply(text="У вас нет доступа")