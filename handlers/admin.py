import random

from aiogram import types
from config import bot, ADMIN, Dispatcher
from database.bot_db import sql_command_all, sql_command_delete




async def delete_data(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Ты не мой босс!")
    else:
        users = await sql_command_all()
        random_user = random.choice(users)
        await bot.send_message(
            message.from_user.id,
            random_user[-1],
            caption=f"{random_user[0]} {random_user[1]} {random_user[2]} "
                    f"{random_user[3]}\n\n{random_user[4]}"
            )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)

def register_handlers_admin(dp:Dispatcher):
    dp.register_message_handler(delete_data,commands=["delete"])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))