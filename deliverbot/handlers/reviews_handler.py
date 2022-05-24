from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from database import database as db
from keyboard import kb_menu, kb_main, kb_cancel

class FSMReview(StatesGroup):
    review = State()

async def review(message: types.Message):
    await FSMReview.review.set()
    await message.answer("Введите отзыв о ресторане(Своё имя, комментарий и оценка)")
    await message.answer("Пример: Василий, мне понравилось 10/10", reply_markup=kb_cancel)

async def insert_review(message: types.Message, state: FSMContext):
    parsed_message = message.text.split(',')
    async with state.proxy() as data:
        data['review'] = db.insert_review(parsed_message[0], parsed_message[1])
    await message.answer(f"Отзыв: {parsed_message[0]} {parsed_message[1]} занесен в книгу отзывов")
    await state.finish()

async def send_reviews(message: types.Message):
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
    dp.register_message_handler(review, Text(equals="оставить отзыв", ignore_case=False))
    dp.register_message_handler(cancel, Text(equals="cancel", ignore_case=False), state='*')
    dp.register_message_handler(insert_review, state=FSMReview.review)
    dp.register_message_handler(send_reviews, Text(equals="отзывы", ignore_case=False))