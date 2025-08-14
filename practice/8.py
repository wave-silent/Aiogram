from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib
import uuid


TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_bold_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Empty'

    item_1 = InlineQueryResultArticle(
        input_message_content=InputTextMessageContent(f'<b>{text}</b>',
                                                      parse_mode='HTML'),
        id = str(uuid.uuid4()),            # Уникальный ID для Bold, чтобы не было ошибки при обьединении двух item
        title='Bold',
        description='Empty',
        thumb_url='https://d144mzi0q5mijx.cloudfront.net/img/B/O/Bold.png'                 # Для того чтобы вставить картинку
    )

    item_2 = InlineQueryResultArticle(
        input_message_content=InputTextMessageContent(f'<i>{text}</i>',
                                                      parse_mode='HTML'),
        id=str(uuid.uuid4()),             # Уникальный ID для Italic
        title='Italic',
        description='Empty',
        thumb_url='https://d144mzi0q5mijx.cloudfront.net/img/S/E/Serif-Italic.png'
    )


    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item_1, item_2],
                                  cache_time=1
                                  )



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
