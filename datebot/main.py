import logging
from create_bot import dp
from aiogram import executor
from handlers import date_handler, start_handler

logging.basicConfig(level=logging.INFO)


date_handler.register_handlers(dp)
start_handler.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)