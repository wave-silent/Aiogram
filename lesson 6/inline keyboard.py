'''
Удобная клавиатура, котороя прикрепляется к сообщение снизу, она очень удобна своих функционалам! 
'''

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я запустился!')

inline_kb = InlineKeyboardMarkup(row_width=2)   # row_width - сколько кнопок в строке
ib1 = InlineKeyboardButton(text='Button 1', url="https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=11&ab_channel=ПрактическоепрограммированиеPython")
ib2 = InlineKeyboardButton(text='Button 2', url="https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=11&ab_channel=ПрактическоепрограммированиеPython")
inline_kb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Приветствую тебя!',
                           reply_markup=inline_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
