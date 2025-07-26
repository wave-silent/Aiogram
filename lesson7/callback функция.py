'''
В Python существует концепция обработки событий посредством специальных callback функций(ф. обратного вызова)

callback функция - это обыкновенная функция, которая будет приведена интерпретатором Питон в исполнение в ответ на
возникновение конкретного, определенного нами события.

Существует callback функция обратного вызова, реагирующая на некоторое событие

CallbackQuery - класс, который возвращает обьект запроса обратного вызова в ответ на некоторое событие. Имеет множество атрибутов

callback_query_handler - декоратор-хендлер, использующий для реализации обработки обьекта запроса. Обрабатывает не одно, а множество обьектов callback query.
Для избирательной обработки используется специальный фильтр.
'''


from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я был запущен!')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/vote')
kb.add(b1).insert(b2)

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать в наш бот!',
                           reply_markup=kb)


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='❤️', callback_data='like')
    ib2 = InlineKeyboardButton(text='👎', callback_data='dislike')
    ikb.add(ib1, ib2)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://main-cdn.sbermegamarket.ru/big2/hlr-system/-2/02/08/20/71/86/9/100026736802b1.jpg',
                         caption='Нравится ли тебе данная фотография?',            # caption - для описания текста
                         reply_markup=ikb)  


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer('Тебе понравилась данная фотография!')
    await callback.answer('Тебе не понравилась данная фотография!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
