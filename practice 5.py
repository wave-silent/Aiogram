from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я был запущен!')

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1', url='https://ru.stackoverflow.com/questions/1560452/Не-импортируется-executor-из-библиотеки-aiogram-в-python')
ib2 = InlineKeyboardButton(text='Button 2', url='https://ru.stackoverflow.com/questions/1560452/Не-импортируется-executor-из-библиотеки-aiogram-в-python')
ikb.add(ib1, ib2)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/links')
kb.add(b1)

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать в главное меню!',
                           reply_markup=kb)


@dp.message_handler(commands=['links'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Выберите опцию!',
                           reply_markup=ikb)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
