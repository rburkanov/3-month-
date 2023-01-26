import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Здравсвуйте {message.from_user.first_name}")
@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton ("next", callback_data= "button")
    markup.add(button)
    question = "Какой язык программирования лучше?"
    answers = [
        "Python",
        "Java",
        "JavaScript"

    ]

    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        reply_markup= markup
    )
@dp.callback_query_handler(lambda call:call.data=="button")
async def quiz_2(call:types.CallbackQuery):
    # markup = InlineKeyboardMarkup()
    # button_1 = InlineKeyboardButton("next", callback_data="button_1")
    # markup.add(button_1)
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
        correct_option_id=2

    )
@dp.message_handler(commands="meme")
async def meme (message: types.Message):
    photo = open ("Media/lll.jpg", 'rb')
    await bot.send_photo(message.chat.id , photo=photo)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id,int (message.text)**2)
    else:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

