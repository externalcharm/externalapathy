from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from database import database as db
from keyboard import kb_main, kb_cancel

class FSMReview(StatesGroup):
    feedback = State()

async def feedback_get(message: types.Message):
    await FSMReview.feedback.set()
    await message.answer("Введите отзыв о ресторане(Своё имя, комментарий и оценка)")
    await message.answer("Пример: Василий, мне понравилось 10/10", reply_markup=kb_cancel)

async def insert_feedback(message: types.Message, state: FSMContext):
    parsed_message = message.text.split(',')
    async with state.proxy() as data:
        data['feedback'] = db.insert_feedback(parsed_message[0], parsed_message[1])
    await message.answer(f"Отзыв: {parsed_message[0]} {parsed_message[1]} занесен в книгу отзывов", reply_markup=kb_main)
    await state.finish()

async def send_feedbacks(message: types.Message):
    answer = ''
    reviews = db.select_reviews()
    for review in reviews:
        answer = answer + 'Кто оставил: ' + review[0] + ' Отзыв: ' + review[1] + '\n'
    await message.answer(answer)

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Действие отменено.", reply_markup=kb_main)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(feedback_get, Text(equals="give_feedback", ignore_case=False))
    dp.register_message_handler(cancel, Text(equals="cancel", ignore_case=False), state='*')
    dp.register_message_handler(insert_feedback, state=FSMReview.feedback)
    dp.register_message_handler(send_feedbacks, Text(equals="feedbacks", ignore_case=False))