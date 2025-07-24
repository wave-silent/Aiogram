# Самый первый урок, создан самый простейший бот
from aiogram import Bot, Dispatcher, executor, types


# бот - сервер, который будет взаимодействовать с API Telegram
# API - элемент программы, который взаимодействует с другим программами
TOKEN_API = "8386228254:AAG4-AycDrNYlQj-5kqMyyU2nebq1aINcds"  # Авторизационный токен для подлключения к телеграм API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()    #Обрабатывает какие-то update
async def echo(message: types.Message):
    await message.answer(text=message.text)  # написать сообщение text


if __name__ == '__main__':
    executor.start_polling(dp)  #Пока просто запуск бота



