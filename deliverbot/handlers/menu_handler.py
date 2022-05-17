from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import database as db
from keyboard import kb_menu, kb_main

class FSMMenu(StatesGroup):
    menu = State()

async def menu(message: types.Message):
    await FSMMenu.menu.set()
    await message.answer("Выберите категорию меню", reply_markup=kb_menu)

async def send_menu(message: types.Message, state: FSMContext):
    async with state.proxy() as text:
        text['menu'] = message.text
        menu = db.select_menu(message.text[1:])
        answer = ''
        for id, product, price in menu:
            answer = answer + str(id) + '; ' + product + '; Цена: ' + str(price) + '\n'
    await message.answer(answer, reply_markup=kb_main)
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(menu, commands=['menu'])
    dp.register_message_handler(send_menu, state=FSMMenu.menu)