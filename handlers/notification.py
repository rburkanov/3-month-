import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = []
    chat_id.append(message.from_user.id)
    await message.answer("Ok")


async def go_to_study():
    for id in chat_id:
        await bot.send_message(id, "Пора учиться!")

async def scheduler():
    aioschedule.every().monday.at('07:26').do(go_to_study)
    while True:
        await aioschedule.run_pending()
def register_message_handelers_client(dp:Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word:"Напомни"in word.text)
