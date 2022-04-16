from aiogram import Dispatcher, types
from keyboard import kb_main

async def help(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=kb_main)
    await message.answer('''
/now - Выводит нынешнюю дату с временем
/full_date - Бот просит вас ввести дату в цифровом формате(день, месяц, год) и выводит день недели, месяц и год''')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(help, commands=['start', 'help'])