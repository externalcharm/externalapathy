import logging
from create_bot import dp
from aiogram import executor
from handlers import menu_handler, request_handler, reviews_handler, start_handler, reviews_handler

logging.basicConfig(level=logging.INFO)


request_handler.register_handlers(dp)
start_handler.register_handlers(dp)
menu_handler.register_handlers(dp)
reviews_handler.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)