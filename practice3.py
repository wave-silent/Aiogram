from aiogram import Bot, Dispatcher, executor, types

TOKEN_API='8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я запустился!')

@dp.message_handler(commands=['give'])
async def start_command(message: types.Message):
    await message.answer('Смотри какой смешной кот ❤️')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEPA_logxuMC-l5mFlAjHG2AAH0aNrE03YAAmcCAALNwEgYZ-ixnulCuOw2BA')
    await message.delete()

@dp.message_handler()
async def count(message: types.Message):
    await message.reply(str(message.text.count('✅')))

@dp.message_handler()
async def send_emoji(message: types.Message):
    if message.text == '❤️':
        await message.reply('🖤')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text='<b>/give</b> - <em>Пишет сообщение и отправляет стикер кота</em>', parse_mode="HTML")

@dp.message_handler(content_types=['sticker'])      #Отправляет ID на стикер
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
