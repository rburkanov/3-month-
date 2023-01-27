from aiogram import types
from config import bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



async def quiz_2(call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Next", callback_data="button_1")
    markup.add(button_1)
    question = "Кто из перечисленных является богаче?"
    answers = [
        "Марк Цукерберг",
        "Джефф Безос",
        "Илон Маск"

    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        reply_markup =markup

    )
async def quiz_3(call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("next", callback_data="button_2")
    markup.add(button_2)
    question = "Кто является сейчас президентом Кыргызстана?"
    answers = [
        "Садыр Жапаров",
        "Сооронбай Жээнбеков",
        "Мирбек Атабеков"

    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        reply_markup=markup
    )
async def quiz_4(call:types.CallbackQuery):
    question = "Столица Кыргызстана?"
    answers = [
        "Ош",
        "Талас",
        "Бишкек"

    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2
    )

def register_handler_callback(dp:Dispatcher):
    # dp.register_callback_query_handler(quiz_2, text="button")
    # dp.register_callback_query_handler(quiz_3, text="button_1")
    # dp.register_callback_query_handler(quiz_4, text="button_2")
    dp.register_callback_query_handler(quiz_2, lambda call:call.data=='button')
    dp.register_callback_query_handler(quiz_3, lambda call:call.data=="button_1")
    dp.register_callback_query_handler(quiz_4, lambda call:call.data=="button_2")