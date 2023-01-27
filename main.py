from handlers import callback ,admin, client, extra
from config import dp
import logging
from aiogram.utils import executor

client.register_message_handelers_client(dp)
callback.register_handler_callback(dp)
# admin.register_message_handelers_client(dp),

extra.register_handler_extra(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

