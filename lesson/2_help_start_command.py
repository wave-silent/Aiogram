# Простейшая обработка команд
from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом 
"""

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='Добро пожаловать в наш телеграмм бот!')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
