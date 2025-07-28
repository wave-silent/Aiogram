from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
HELP_COMMAND="""
<b>/start</b> - <em>Начало нашей работы!</em>
<b>/help</b> - <em>Выводит перечень команд!</em>
<b>/картинка</b> - <em>Отправляет картинку по адресу!</em>
<b>/location</b> - <em>Отправляет локацию</em>
"""

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # await message.answer(message.text)
    # await bot.send_message(chat_id=message.chat.id, text='Hello!')    #Тождественен message.answer
    # await bot.send_message(chat_id=message.from_user.id, text="Hello!")  #Отправляет сообщения только лично
    await bot.send_message(chat_id = message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://mastera.academy/wp-content/uploads/2025/05/PIN-1074x460-NEWS-2-1.jpg')
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_location(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=55, longitude=74)
    await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # skip_updates - нужен для того, чтобы когда пользователь запускал бота, он не реагировал на сообщения
    # других людей, когда бот находился в офлайне
