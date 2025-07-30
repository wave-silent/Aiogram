import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await asyncio.sleep(10)
    await message.answer('adadadf')


@dp.errors_handler(exception=BotBlocked)
async def error_botblocked(update: types.Update, exception: BotBlocked):
    print('Нельзя отправить сообщение, потому что нас заблокировали!')
    return True

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
