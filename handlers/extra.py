from aiogram import types,Dispatcher
from config import bot
from config import ADMIN
import random


async def echo(message: types.Message):
    if message.text.startswith("game") and message.from_user.id in ADMIN:
        emojis = ['🎯', '🎳', '🎰', '🎲', '⚽️', '🏀']
        dice = random.choise(emojis)
        await bot.send_dice(message.chat.id, emoji=dice)
    elif message.text.isdigit():
        await bot.send_message(message.from_user.id,int (message.text)**2)
    else:
        await bot.send_message(message.from_user.id, message.text)

def register_handler_extra(dp:Dispatcher):
    dp.register_message_handler(echo)
