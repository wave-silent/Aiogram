from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

def get_inline_kb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Increase', callback_data='btn_increase'), InlineKeyboardButton('Decrease', callback_data='btn_decrease')],
    ])

    return ikb

number = 0

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'The current num is {number}', reply_markup=get_inline_kb())

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))    #Обрабатываются команды только get_inline_kb клавиатуры
async def inline_kb_cb(callback: types.CallbackQuery):
    global number
    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(text=f'The current num is {number}',
                                         reply_markup=get_inline_kb())

    elif callback.data == 'btn_decrease':
        number -= 1
        await callback.message.edit_text(text=f'The current num is {number}',
                                         reply_markup=get_inline_kb())

    else:
        1/0


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
