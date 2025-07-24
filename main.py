from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'

bot = Bot(TOKEN_API)


dp = Dispatcher(bot)

@dp.message_handler()
async def echo_upper(message: types.Message):   #capitalize - будет возвращать в верхнем регистре
    if message.text.count(' ') >= 1:               # Проверяем на пробелы
        await message.answer(text=message.text)



if __name__ == '__main__':
    executor.start_polling(dp)


