from aiogram import Bot, Dispatcher, executor, types
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

async def on_startup(_):
    print('Я запустился!')

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>Показывает доступные команды</em>
<b>/description</b> - <em>Описание того, что может делать бот</em>
<b>/send_orange</b> - <em>Отправляет фото апельсина</em>
<b>/location</b> - <em>Отправляет рандомное местоположение</em>
"""

kb = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/location')
b3 = KeyboardButton('/send_orange')
b4 = KeyboardButton('/description')
b5 = KeyboardButton('❤️')

kb.add(b1).insert(b2).add(b3).insert(b4).add(b5)

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать!',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['location'])
async def location_command(message: types.Message):
    await bot.send_location(chat_id=message.chat.id, longitude=random.randint(1, 100), latitude=random.randint(1, 100))
    await message.delete()


@dp.message_handler(commands=['send_orange'])
async def send_orange_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo='https://avatars.mds.yandex.net/get-mpic/5031100/img_id1059595353447848448.jpeg/orig')
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Данный бот умеет ...', parse_mode="HTML")
    await message.delete()


@dp.message_handler()
async def love_command(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEPA_Vogxjgv9zD8x2VXjz2d6hVibkSUwAC5BoAAn_nkEgZOHYB1oFHcjYE')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
