'''
InlineQuery - класс, результатом вызова которого является его экземпляр - конкретный запрос, сформированный
при отправке пользователем текста, через обращение к Inline боту

Состоит:
id - идентификатор запроса
from - обьект пользователя
query - сам текст

Доп. значения:
location - локация
chat_type - тип чата
'''

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from aiogram.types import InlineQueryResultArticle, InputTextMessageContent               #Inline Mode

import hashlib

TOKEN_API='8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')

def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Button_1', callback_data=cb.new('push_1')),  # callback_data = {'action', 'push_1'}
         InlineKeyboardButton('Button_2', callback_data=cb.new('push_2'))]  # callback_data = {'action', 'push_2'}
    ])

    return ikb


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await message.answer('Добро пожаловать!', reply_markup=get_ikb())

@dp.callback_query_handler(cb.filter(action='push_1'))     # single responsibility principle
async def push_first_command(callback: types.CallbackQuery) -> None:
        await callback.answer('Hello')

@dp.callback_query_handler(cb.filter(action='push_2'))
async def push_second_command(callback: types.CallbackQuery) -> None:
    await callback.answer('World')

@dp.inline_handler()   # process InlineQuery() is formed by Telegram IPI
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'    # получили текст от пользователя
    input_content = InputTextMessageContent(text)   # Формируем контент ответного сообщения
    result_id = hashlib.md5(text.encode()).hexdigest()    #сделали уникальный идентификатор Id результата

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Echo!!!'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)
  

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
