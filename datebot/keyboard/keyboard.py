from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_now = KeyboardButton('/now')
button_date = KeyboardButton('/full_date')
button_cancel = KeyboardButton('/cancel')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_now).insert(button_date)

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)