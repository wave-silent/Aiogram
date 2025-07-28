from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from Project1_keyboards import kb, ikb, kb_photo
import random

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = '''
<b>/start</b> - <em>Старт бота</em>
<b>/help</b> - <em>Перечень команд</em>
<b>/description</b> - <em>Описание бота</em>
'''

sp_photos = ['https://i.pinimg.com/736x/b6/5f/c2/b65fc25b19abdee5b2caa3e6f07f261f.jpg', 'https://i.pinimg.com/originals/56/b1/76/56b1760aafdcfb3116d5769d04cd6b5c.jpg',
             'https://avatars.mds.yandex.net/get-mpic/4322217/img_id909093120241748224.jpeg/orig']

photos = dict(zip(sp_photos, ['Lake', 'Sea', 'Mountain']))      #Удобно, с помощью этой строчки, мы создаем словарь со ссылками наших фотографий
random_photo = random.choice(list(photos.keys()))

flag = False

async def on_startup(_):
    print('Я был запущен!')


async def send_random(message: types.Message):
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id, photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb)

async def l_kb_photo(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню',
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(Text(equals='menu_photo'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Рандомная фотка!',
                         reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать в наш бот!',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Наш бот умеет отправлять рандомные фотографии с описанием',
                           reply_markup=kb)
    await message.delete()


@dp.callback_query_handler()
async def callback_command(callback: types.CallbackQuery):
    global random_photo, flag       # Нежелательно использовать глобальные переменные
    if callback.data == 'like':
        if not flag:
            await callback.answer(text='Тебе понравилось это фото!')
            flag = not flag
        else:
            await callback.answer('Вы уже лайкали!')


    elif callback.data == 'dislike':
        await callback.answer(text='Тебе не зашла эта картинка, о черт!')

    elif callback.data == 'main_menu':
        await l_kb_photo(message=callback.message)
        await callback.answer()

    else:
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                          type='photo',
                                          caption=photos[random_photo]),
                                          reply_markup=ikb)
        await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



# В другом модуле написано
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('menu_photo')
kb.add(b1).insert(b2).add(b3)

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='send_photo')
bp2 = KeyboardButton(text='Главное меню')
kb_photo.add(bp1, bp2)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️', callback_data='like')
ib2 = InlineKeyboardButton(text='💩', callback_data='dislike')
ib3 = InlineKeyboardButton(text='Следующая картинка', callback_data='next')
ib4 = InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
ikb.add(ib1, ib2).add(ib3).add(ib4)
