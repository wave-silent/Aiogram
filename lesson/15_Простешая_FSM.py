'''
FSM - Конечная машина состояний
'''

from aiogram import executor, Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

TOKEN_API = '8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'
storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,
                storage=storage)       # Некоторое хранилище

def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Начать работу!'))

    return kb

def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))


class ClientState(StatesGroup):     # Состояния
    photo = State()
    desc = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await message.answer('Добро пожаловать!',
                         reply_markup=get_kb())


@dp.message_handler(commands=['cancel'], state='*')                    # state='*' - Это все состояния
async def start_command(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.reply('Отменил!',
                        reply_markup=get_kb())
    await state.finish()    # Завершаем состояние, если человек нажимает cancel




@dp.message_handler(lambda message: not message.photo, state = ClientState.photo)    # Если не фото, обработчик
async def check_photo(message: types.Message):
    return await message.reply('Это не фотография!')


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state = ClientState.photo)    # Если это фото, обработчик
async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id    # Сохраняем идентификатор фотографий, который отправил пользователь, в data['photo']
        # Идентификатор фотографий, это уникальный идентификатор каждой фотографии, сформированный telegram api
        await ClientState.next()
        await message.reply('А теперь отправь нам описание!')


@dp.message_handler(state = ClientState.desc)    # Описание фото
async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text

    await message.reply('Ваша фотография сохранена!')

    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id, photo=data['photo'],
                             caption=data['desc'])

    await state.finish()


@dp.message_handler(Text(equals='Начать работу!'), state=None)
async def start_work(message: types.Message) -> None:
    await ClientState.photo.set()
    await message.answer('Сначала отправь нам фотографию!',
                         reply_markup=get_cancel())



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
