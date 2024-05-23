
import time
# from bot import bot
import asyncio

import info
from aiogram import Bot, Dispatcher, types, executor
# from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.dispatcher import FSMContext
from SQLAlchemy01 import *
from other import sorting_in_data
bot = Bot(token=info.token1)

sqlbot = SqlAlchemy('bot_base.db')

chatt = None
messagee = None
async def delete_message(chatt, messagee):
    await bot.delete_message(chat_id=chatt, message_id=messagee)
    print('sfsfsdfsfs')
def pr():
    print("ook")

def get_keyboard():
    # Генерация клавиатуры.
    buttons = [
        types.InlineKeyboardButton(text="удалить эти данные", callback_data="num_f"),

    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard

async def messages_processing(message: types.Message):
    print(message.text)
    result = sorting_in_data(message.text.lower())

    # внести данные
    # sqlbot.add_data_in_month(result)

    # sqlbot.select_(Month_04_24)

    message_bot = await message.answer(f"Вот что я понял:\n {result}", reply_markup=get_keyboard())
    # time.sleep(3)
    global chatt
    chatt = message_bot.chat.id

    global messagee
    messagee = message_bot.message_id
    print(chatt, '---', messagee)
    await asyncio.sleep(5)
    # await delete_message(message_bot.chat.id, message_bot.message_id)
    # await message.answer(f"Вот что я понял:\n {result}")

    await bot.edit_message_text(chat_id=message_bot.chat.id, message_id=message_bot.message_id, text=f"Последние данные:\n {result}")

    # await message.delete(message_bot_id)
    # await message.answer(f"Вот что я понял:\n {result}")
    # await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

# @dp.callback_query_handler(text="random_value")
async def data_delete(callback_query: types.CallbackQuery):

    print(chatt)
    await bot.delete_message(chat_id=chatt, message_id=messagee)
    await callback_query.message.delete_reply_markup()
    await callback_query.message.answer("Данные удалены")

    print("ook")

async def cmd_start(message: types.Message):
    await message.reply("Выберите команду")



async def reference_message(message: types.Message):
    await message.answer("Вот мои команды! \n"
                         "/1 или 'бот запиши' для записи количества прочитанных страниц\n"
                         "'отмена' чтобы выйти из записи")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(messages_processing)
    dp.register_message_handler(cmd_start, lambda message: message.text.lower() == "бот")

    dp.register_message_handler(reference_message, commands=["0"])
    dp.register_message_handler(reference_message, lambda message: message.text.lower() == "справка")

    dp.register_callback_query_handler(data_delete, lambda q: q.data == 'num_f')
# from bot import *
# bot = Bot(token=info.token1)
# dp = Dispatcher(bot, storage=MemoryStorage())
#
# @dp.callback_query_handler(Text(startswith="num_"))
# async def send_random_value(call: types.CallbackQuery):
#     await call.message.answer("Просто отправляем текст в ответ")
#     print("ook")
#     pr()