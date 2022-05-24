from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_request = KeyboardButton('make_request')
button_menu = KeyboardButton('menu')
button_cancel = KeyboardButton('cancel')
button_location = KeyboardButton('send_location', request_location=True)
button_review = KeyboardButton('отзывы')
button_feedback = KeyboardButton('оставить отзыв')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_request).add(button_menu).add(button_review).add(button_feedback)

kb_location = ReplyKeyboardMarkup(resize_keyboard=True)
kb_location.add(button_cancel).add(button_location)

# block of menu
#-----------------------------------------------------------------------------------------------------
button_pizza = KeyboardButton('pizza')
button_burgers = KeyboardButton('burgers')
button_sushi = KeyboardButton('sushi')
button_snacks = KeyboardButton('snacks')
button_drink = KeyboardButton('drink')

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.add(button_pizza).add(button_burgers).add(button_sushi).add(button_snacks).add(button_drink)
#-----------------------------------------------------------------------------------------------------

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)
