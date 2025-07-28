from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='👌', callback_data='like')
ib2 = InlineKeyboardButton(text='👎', callback_data='dislike')
ib3 = InlineKeyboardButton(text='Убрать клавиатуру и фотографию', callback_data='delete')
ikb.add(ib1, ib2).add(ib3)

flag = False

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, photo='https://i.pinimg.com/736x/9d/ef/81/9def81be5c019917efdeb3ff72f16ee3.jpg',
                         caption='Тебе нравится эта фотография?',
                         reply_markup=ikb)
    await message.delete()




@dp.callback_query_handler()
async def callback_command(callback: types.CallbackQuery):
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer('Нравится!')
            flag = not flag
        else:
            await callback.answer('Ты уже так голосовал!')
    # await callback.answer(show_alert=True, text='like')           show_alert - позволяет делать красивое окошко, где написано это слово, при нажатии кнопки 
    elif callback.data == 'dislike':
        await callback.answer('Не нравится!')

    elif callback.data == 'delete':
        await callback.message.delete()    # Так мы можем легко удалить клавиатуру и само фото



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
