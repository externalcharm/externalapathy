from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import database as db
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
    await message.answer("Напишите дату..")

async def send_date(message: types.Message, state: FSMContext):
    async with state.proxy() as parsed_message:
        parsed_message = message.text.split()
        date = datetime.datetime(int(parsed_message[2]), int(parsed_message[1]), int(parsed_message[0])).strftime("%a.%B %Y")
        answer = db.select(date[0:3])
        await message.answer(f"{answer}" + f" {date[4:]}")
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(datenow, commands=['now'])
    dp.register_message_handler(date, commands=['full_date'])
    dp.register_message_handler(send_date, state=FSMDate.time)