from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):                    # Отображается в консоли
    print("Бот был успешно запущен!")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em>Привет, добро пожаловать в наш бот!</em>', parse_mode="HTML")  #Можем использовать HTML к тексту

@dp.message_handler(commands=['give'])    #Отправляет стикер
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEPA_Vogxjgv9zD8x2VXjz2d6hVibkSUwAC5BoAAn_nkEgZOHYB1oFHcjYE')
    await message.delete()

@dp.message_handler()         #Отправялет емоджи 
async def give_emoji(message: types.Message):
    await message.reply(message.text + ' ❤️')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
