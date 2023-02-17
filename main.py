import asyncio
from aiogram import Bot, Dispatcher, types, executor
import config

bot = Bot(token=config.BOT_TOKEN)
disp = Dispatcher(bot=bot)
async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} ?!",
        parse_mode=types.ParseMode.HTML,
    )

@disp.message_handlers()
async def echo(message: types.Message):
    await message.answer(text=message.text)

if __name__ == "__main__":
    executor.start_polling()