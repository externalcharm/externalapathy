from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import database as db
from keyboard import kb_main, kb_cancel
import datetime

async def datenow(message: types.Message):
    date = datetime.datetime.now()
    date = date.strftime("%a.%B %Y %H:%M:%S")
    answer = db.select(date[0:3])
    await message.answer(f"{answer}" + f" {date[4:]}")

class FSMDate(StatesGroup):
    time = State()

async def date(message: types.Message):
    await FSMDate.time.set()
    await message.answer("Напишите дату..", reply_markup=kb_cancel)

async def send_date(message: types.Message, state: FSMContext):
    async with state.proxy() as parsed_message:
        parsed_message = message.text.split()
        date = datetime.datetime(int(parsed_message[2]), int(parsed_message[1]), int(parsed_message[0])).strftime("%a.%B %Y")
        answer = db.select(date[0:3])
        await message.answer(f"{answer}" + f" {date[4:]}", reply_markup=kb_main)
    await state.finish()

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Действие отменено.", reply_markup=kb_main)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(datenow, commands=['now'])
    dp.register_message_handler(date, commands=['full_date'])
    dp.register_message_handler(cancel, commands=['cancel'] , state='*')
    dp.register_message_handler(send_date, state=FSMDate.time)