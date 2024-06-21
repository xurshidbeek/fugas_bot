from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor
from gtts import gTTS
import os

menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Menyu 1"), KeyboardButton("Menyu 2"), KeyboardButton("Menyu 3"), KeyboardButton("Menyu 4")],
    [KeyboardButton("Menyu 5"),KeyboardButton("Menyu 6"),KeyboardButton("Menyu 7"),KeyboardButton("Menyu 8")],
    [KeyboardButton("Matinni ovozlashtirish") ],
        ],
    resize_keyboard=True)



# async def get_all_product():
menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail.add(KeyboardButton("Mahsulot 1"), KeyboardButton("Mahsulot 2"))
menu_detail.add(KeyboardButton("Mahsulot 3"), KeyboardButton("Mahsulot 4"), KeyboardButton("Mahsulot 5"),
                KeyboardButton("Mahsulot 6"),KeyboardButton("Mahsulot 7"),KeyboardButton("Mahsulot 8"))
menu_detail.add(KeyboardButton("Back"))


mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))
# .--.
#..-
#--
#.--.