from config import bot, Dispatcher
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from parser.film import parser


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Здравсвуйте {message.from_user.first_name}")

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
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        reply_markup= markup
    )

async def meme (message: types.Message):
    photo = open ("Media/lll.jpg", 'rb')
    await bot.send_photo(message.chat.id , photo=photo)

async def pin (message:types.Message) :
    await bot.pin_chat_message(message.chat.id, message.message_id)

async def get_film(message: types.Message):
    film = parser()
    for i in film:
        await message.answer(
            f"{i['link']}\n\n"
            f"{i['title']}\n"
            f"{i['status']}\n"
            f"#Y{i['date']}\n"
            f"#{i['genre']}\n"
            f"#{i['country']}"
        )

def register_message_handelers_client(dp:Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_message_handler(meme, commands=["meme"])
    dp.register_message_handler(pin, commands=["pin"], commands_prefix='!')
    dp.register_message_handler(get_film, commands=['film'])
