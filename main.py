import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from db import Database
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = "7324996837:AAGIu_iInuSS4SMavoxC-DpPF0arMoQUqrQ"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f" Assalomu Alaykum hush kelibsiz @{username}")

                                                                                                                                                                               
menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Menyu 1"), KeyboardButton("Menyu 2"), KeyboardButton("Menyu 3"), KeyboardButton("Menyu 4")],
        ],
    resize_keyboard=True)



# async def get_all_product():
menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail.add(KeyboardButton("Menyu 1"), KeyboardButton("Menyu 2"))
menu_detail.add(KeyboardButton("Mahsulot 1"), KeyboardButton("Mahsulot 2"), KeyboardButton("Mahsulot 3"))
menu_detail.add(KeyboardButton("Back"))


mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
