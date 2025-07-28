'''

В aiogram существует три основных класс ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
Каждый класс осуществляет какой-то функционал

ReplyKeyboardMarkup - создаем обьект клавиатуры, осуществляет более лаконичную клавиатуру

KeyboardButton - добавляет кнопки

ReplyKeyboardRemove - удаляет клавиатуру из интерфейса telegram

'''



from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)      #Делает иконку клавиатуры более лаконичной, удобной
#                        one_time_keyboard=True   # Исчезающая клавиатура, выглядит красиво
b1 = KeyboardButton('/help')
# b2 = KeyboardButton('/start')   #Лучше не делать такую кнопку, потому что может флудд, и надо это обрабатывать
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')
#kb.add(b1).add(b2).add(b3) #Вставляет кнопки просто построчно
kb.add(b1).insert(b2).add(b3)   # insert - делает новый столбец


HELP_COMMAND = '''
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка нашего фото</em>
'''


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")
                           #reply_markup=ReplyKeyboardRemove())    #Удаляет полностью клавиатуру, если мы прописываем /help
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Добро пожаловать в наш бот!', parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Наш бот умеет отправлять фотографии', parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id = message.from_user.id, photo='https://cdn1.ozone.ru/s3/multimedia-1-2/c600/7494698342.jpg')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
