from aiogram import Bot, Dispatcher, types, executor
import random

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
ABC = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
counter = 0

@dp.message_handler(commands=['count'])
async def check(message: types.Message):
    global counter
    await message.answer(f'Счетчик: {counter}')
    counter += 1


@dp.message_handler(commands=['description'])
async def help_command(message: types.Message):
    await message.answer(text="Данный бот рандомно возвращает латинскую букву на сообщение пользователя!")
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    if '0' in message.text:
        await message.reply(text="YES")
    else:
        await message.reply(text="NO")


@dp.message_handler()
async def send_random(message: types.Message):
    await message.reply(text=random.choice(ABC))


if __name__ == '__main__':
    executor.start_polling(dp)
