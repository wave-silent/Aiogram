from aiogram import Bot, executor, types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

import hashlib

from aiogram.types import InlineQueryResultArticle, InputTextMessageContent


TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
cb = CallbackData('ikb', 'action')

user_data = ''

@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    await message.answer('Введите число')



@dp.message_handler()
async def text_handler(message: types.Message) -> None:
    global user_data
    user_data = message.text
    await message.reply('Ваши данные сохранены!')

@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}</b> - {user_data}',
                                            parse_mode="HTML")

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id = result_id,
        title='Echo bot!',
        description='Привет, я не простой Echo bot!'
    )


    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
