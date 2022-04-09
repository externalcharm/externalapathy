from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import database as db
import datetime

async def datenow(message: types.Message):
    date = datetime.datetime.now()
    await message.answer(date.ctime())

class FSMDate(StatesGroup):
    time = State()

async def date(message: types.Message):
    await FSMDate.first()
    await message.answer("Напишите дату..")

async def send_date(message: types.Message, state: FSMContext):
    async with state.proxy() as parsed_message:
        parsed_message = message.text.split()
        date = datetime.datetime(int(parsed_message[2]), int(parsed_message[1]), int(parsed_message[0]))
        string = date.strftime("%a.%B %Y")
        answer = db.select(string[0:3])
        await message.answer(f"{answer} "[3:][:-5] + f" {string[4:]}")
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(datenow, commands=['now'])
    dp.register_message_handler(date, commands=['full_date'])
    dp.register_message_handler(send_date, state=FSMDate.time)