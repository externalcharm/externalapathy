from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_now = KeyboardButton('/now')
button_date = KeyboardButton('/full_date')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_now).insert(button_date)