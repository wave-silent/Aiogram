from aiogram import Bot, Dispatcher, executor, types

from aiogram.utils.callback_data import CallbackData

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')    #prefix - с помощью этого можно удобно обращатьcя к конкретным данным

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Button', callback_data=cb.new('push'))]
])

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await message.answer('Text', reply_markup=ikb)


@dp.callback_query_handler(cb.filter())
async def ikb_cb_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push':
        await callback.answer('Something')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
