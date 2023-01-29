from handlers import callback ,admin, client, fsmmentor, notification,extra
from config import dp,bot,ADMIN
import logging
import asyncio

from database.bot_db import sqlcreate
from aiogram.utils import executor

async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    await bot.send_message(chat_id=ADMIN[0],
                           text="Bot started!")
    sqlcreate()

client.register_message_handelers_client(dp)
callback.register_handler_callback(dp)
fsmmentor.register_handlers_fsmmentor(dp)
admin.register_handlers_admin(dp)
notification.register_message_handelers_client(dp)
extra.register_handler_extra(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

