from icecream import ic

ic.configureOutput(includeContext=True)
ic.configureOutput(prefix='DEBUG => ')

import time
# from bot import bot
import asyncio

import info
from aiogram import Bot, Dispatcher, types, executor
# from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.dispatcher import FSMContext

from SQLAlchemy01 import *
from other import sorting_in_data, translate_dir

bot = Bot(token=info.token1)
dp = Dispatcher(bot)

sqlbot = SqlAlchemy('bot_base.db')

insert_id_data = None
message_bot = None
result = None
message_text_input = None

list_credit = ['хозтовары', 'молоко', 'техника', 'зарплата', ]
list_debt = ['мясо', 'молоко', 'техника', "хозтовары"]

month_number = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
month_dir = {'январь': '01', 'февраль': '02', 'март': '03', 'апрель': '04', 'май': '05', 'июнь': '06', 'июль': '07', 'август': '08', 'сентябрь': '09', 'октябрь': '10', 'ноябрь': '11', 'декабрь': '12'}
# async def delete_message(chat_id, message_id):
#     await bot.delete_message(chat_id=chat_id, message_id=message_id)
#
# def pr():
#     print("oocbcbk")

def get_keyboard_del():
    # Генерация клавиатуры
    buttons = [
        # types.InlineKeyboardButton(text="удалить эти данные", callback_data="num_f"),
        types.InlineKeyboardButton(text="подтвердить", callback_data="num_f"),

    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


# внести данные
async def messages_processing(message: types.Message):
    ic(message.text)
    global result
    result = sorting_in_data(message.text.lower())
    tanslate_result = translate_dir(result)

    # # внести данные
    # global insert_id_data
    # insert_id_data = sqlbot.add_last_month(result)
    # ic(insert_id_data)

    # await message.answer(f"Даные внесены:")
    # for k, v in result.items():
    #     await message.answer(f"{k}: {v}")
    # message_bot = await message.answer(f"id:{insert_id_data}",
    #                                    reply_markup=get_keyboard_del())
    # await asyncio.sleep(5)
    # await bot.edit_message_text(chat_id=message_bot.chat.id, message_id=message_bot.message_id,
    #                             text=f"id: _{insert_id_data}")

    # str_start = "Внести данные:\n"
    # for k, v in result.items():
    #     str_start += f"{k}: {v}\n"

    def iterate_text():
        str_start = ""
        for k, v in tanslate_result.items():
            str_start += f"{k}: {v}\n"
        return str_start

    # message_bot = await message.answer(str_start,
    #                                    reply_markup=get_keyboard_del())
    global message_text_input
    message_text_input = iterate_text()
    global message_bot
    message_bot = await message.answer(f"Внести данные:\n{message_text_input}",
                                       reply_markup=get_keyboard_del())

    await asyncio.sleep(10)

    # ic(message_bot.message_id)
    # ic(type(message_bot.message_id))
    # await callback_query.message.delete_reply_markup()
    # ic(str_start)
    # await bot.edit_message_text(chat_id=message_bot.chat.id, message_id=message_bot.message_id,
    #                             text=str_message + "...")

    await bot.delete_message(chat_id=message_bot.chat.id, message_id=message_bot.message_id)


async def data_update_in_id(message: types.Message):
    result = sorting_in_data(message.text.lower())
    # ic(result)
    id_ = result.pop('id', None)
    # ic(id_)
    # ic(result)
    if id_ is None:
        await message.answer(f"Ошибка! Вы не указали айди!")

    elif 'debt' in result:
        result['credit'] = None
    else:
        result['debt'] = None
    sqlbot.update_last_of_month(id_, result)
    await message.answer(f"Данные id: {id_} изменены")


async def data_delete(callback_query: types.CallbackQuery):
    await callback_query.message.delete_reply_markup()
    # ic(insert_id_data)
    # sqlbot.delete_last_month(insert_id_data)
    # await bot.delete_message(chat_id=message_bot.chat.id, message_id=message_bot.message_id)

    # await callback_query.message.answer(f"Данные id: {insert_id_data} удалены")

    # внести данные
    global insert_id_data
    insert_id_data = sqlbot.add_last_month(result)
    ic(insert_id_data)
    # await callback_query.message.answer(message_bot.text)
    await callback_query.message.answer(f"Данные id: {insert_id_data} подтверждены\n{message_text_input}")
    # ic(message_bot.message_id)
    # ic(type(message_bot.message_id))


async def data_delete_in_id(message: types.Message):
    id_ = message.text[20:]  # - "удалить данные айди "data_update_in_id
    # await message.answer(f"Введите id")
    # ic(message.text)
    sqlbot.delete_last_month(id_)
    await message.answer(f"Данные id: {id_} удалены")


async def data_total_this_month(message: types.Message):
    str_ = ""
    sum_manual_debt = 0
    for i in list_debt:
        sum_ = sqlbot.select_last_sum_section_of_debt(i)
        if sum_ is not None:
            str_ += f"{i.capitalize()}: {str(sum_)} \n"
            sum_manual_debt += int(sum_)
    str_debt = f"ДЕБИТ = {sum_manual_debt}\n" + str_

    str_ = ""
    sum_manual_credit = 0
    for i in list_credit:
        sum_ = sqlbot.select_last_sum_section_of_credit(i)
        if sum_ != None:
            str_ += f"{i.capitalize()}: {str(sum_)} \n"
            sum_manual_credit += int(sum_)
    str_credit = f"КРЕДИТ = {sum_manual_credit}\n" + str_
    total = f"ИТОГО = {sum_manual_debt - sum_manual_credit}"
    await message.answer(f"{str_debt}\n{str_credit}\n{total}")

# select_annual_report_24
# sqlbot.select_annual_result_24('04')
async def data_total_other_month(message: types.Message):
    list_message = message.text.split()
    for i in month_number:
        list_select_annual_result_24 = sqlbot.select_annual_result_24(i)
        if i in list_message:
            str_debt = f"ДЕБИТ = {list_select_annual_result_24[2]}\n"
            for d in list_debt:
                for it in sqlbot.select_annual_report_24_debt(i, d):
                    if it is not None:
                        ic(it)
                        str_debt += f"{d.capitalize()}: {it}\n"
            str_credit = f"КРЕДИТ = {list_select_annual_result_24[3]}\n"
            for c in list_credit:
                for it in sqlbot.select_annual_report_24_credit(i, c):
                    if it is not None:
                        ic(it)
                        str_credit += f"{c.capitalize()}: {it}\n"
            str_total = f"ИТОГО = {list_select_annual_result_24[4]}"
            await message.answer(f"{str_debt}\n{str_credit}\n{str_total}")

    for i in month_dir:
        if i in list_message:
            pass
async def cmd_start(message: types.Message):
    await message.reply("Выберите команду")


async def reference_message(message: types.Message):
    await message.answer("Вот мои команды! \n"
                         "/1 или 'бот запиши' для записи количества прочитанных страниц\n"
                         "'отмена' чтобы выйти из записи")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, lambda message: message.text.lower() == "бот")
    dp.register_message_handler(data_delete_in_id, lambda message: "удалить данные айди" in message.text.lower())
    dp.register_message_handler(data_update_in_id, lambda message: "изменить данные айди" in message.text.lower())
    dp.register_message_handler(data_total_this_month, lambda message: message.text.lower() == "отчет этого месяца")
    dp.register_message_handler(data_total_other_month, lambda message: "отчет за" in message.text.lower())

    dp.register_message_handler(messages_processing)

    dp.register_message_handler(reference_message, commands=["0"])
    dp.register_message_handler(reference_message, lambda message: message.text.lower() == "справка")

    dp.register_callback_query_handler(data_delete, lambda q: q.data == 'num_f')


'''
команды 

    - внести по умолчанию без команды
    
    
    - изменть данные
        - укажите айди и изминения
    
    - удалить данные 
        - введите айди
        
    
    - показать отчет
        - за этот месяц
        - за другой 
            - укажите месяц
            
    - сделать отчет в эксель
        - за этот месяц
        - за другой 
            - укажите месяц
            
    - загрузить резервную копию
    '''
