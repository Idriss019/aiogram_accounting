import asyncio
import logging
# from datetime import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import info

from handlers import register_handlers

from middle_ware import AntifludMiddleware, ThrottlingMiddleware_m
from aiogram import Bot, Dispatcher

from aiogram.dispatcher.filters import Text
bot = Bot(token=info.token1)



async def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    logger.error("Starting bot")

    bot = Bot(token=info.token1)
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_handlers(dp)

    dp.middleware.setup(AntifludMiddleware())
    await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling(allowed_updates=['message', 'callback_query'])


if __name__ == "__main__":
    asyncio.run(main())
