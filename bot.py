# app.py module
# -*- coding: utf-8 -*-
import logging
from aiogram import Bot, Dispatcher, types
from db import Database
from button import menu_keyboard, menu_detail
from inline_button import keyboard
from aiogram.types import InputFile
from aiogram.utils import executor
from gtts import gTTS
import os

API_TOKEN = "7324996837:AAExsUbbF-QYehebH-uiai-73CbNKgAw4Dw"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    ful_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_2 (username, full_name, user_id) VALUES ('{username}', '{ful_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Assalomu aleykum sizni ko'rganimdan xursandman  @{username}", reply_markup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz @{username}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 1")
async def show_menu_1(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("1 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "Menyu 2")
async def show_menu_2(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "Menyu 3")
async def show_menu_3(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("3 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "Menyu 4")
async def show_menu_4(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("4 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "Menyu 5")
async def show_menu_5(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("5 - bo'lim. Mahsulotlardan birini tanglang: " , reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Menyu 6")
async def show_menu_6(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("6 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Menyu 7")
async def show_menu_7(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("7 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Menyu 8")
async def show_menu_8(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("8 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Matinni ovozlashtirish")
async def br(message: types.Message):
    await ovoz(message)



@dp.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_keyboard)





@dp.message_handler(lambda message: message.text == "Mahsulot 1" or "Mahsulot 3" or "Mahsulot 4")
async def show_menu_12(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    if message == "Matinni ovozlashtirish":
        await ovoz(message)

    else:
        await message.answer(" Mahsulotni nechtaligini tanglang:", reply_markup=keyboard)
        await ovoz(message)




@dp.message_handler(content_types=types.ContentType.TEXT)
async def ovoz(x: types.Message):
    try:
        # Matnli xabar yuborish
        await x.reply("Siz yuborgan matn: " + x.text)

        # Matnni ovozli xabarga aylantirish
        tts = gTTS(text=x.text, lang='ru')  # Tilni moslang
        tts.save("voice.ogg")

        # Ovozli xabarni yuborish
        voice = InputFile("voice.ogg")
        await bot.send_voice(chat_id=x.chat.id, voice=voice)

        # Yaratilgan faylni o'chirish
        os.remove("voice.ogg")

    except Exception as e:
        await x.reply("Xatolik yuz berdi: " + str(e))



"""  
    if message == "Matinni ovozlashtirish":
        await ovoz(message)
    else:
        await message.answer(" Mahsulotni nechtaligini tanglang:", reply_markup=keyboard)


"""


###########################
###########################
###########################
###########################
"""
    Assalomu alaykum ustoz men matnlarni ovozlashtrw degan buttonga yozgan matini ovozlawtiruvchi funk qowdim lekin
    if != bolsa iwlayapti qolgan hollarda esa inline_button chiqyapti 
    shuning uchun tepaga 3hil varianti korsatib qoydim
    """
###########################
###########################
###########################
###########################

@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    if message.from_user.id in [6734637648]:
        await message.reply("Salom admin")
        photo_path = "https://static.vecteezy.com/system/resources/thumbnails/025/220/125/small/picture-a-captivating-scene-of-a-tranquil-lake-at-sunset-ai-generative-photo.jpg"
        await bot.send_photo(message.chat.id, photo=photo_path)
    else:
        await message.reply("Bunday buyruq turi mavjud emas")






@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
