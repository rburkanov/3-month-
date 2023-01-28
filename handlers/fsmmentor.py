from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMIN
from config import bot, Dispatcher
from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    ID = State()
    name = State()
    age = State()
    nap = State()
    group = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMIN:
        await FSMAdmin.id.set()
        await message.answer(f"Здравствуй{message.from_user.full_name}")
    elif message.from_user.id not in ADMIN:
        await message.answer("Ты не куратор!")

async def load_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = int(message.text)

            await FSMAdmin.next()
            await message.answer("Как звать то?")
    except:
        await bot.send_message(message.from_user.id, "id состоит только из цифр")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.from_user.id, 'Какое направление?',)

async def load_nap(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nap'] = message.text
    await FSMAdmin.next()
    await message.answer("Возраст")

async def load_age(message: types.Message, state: FSMContext):
    try:
        if 50> int(message.text) > 12:
            async with state.proxy() as data:
                data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Из какой группы?")

    except:
        await message.answer('Ввожи только числа')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["goup"] = message.text
        await bot.send_message(message.from_user.id, f"id - {data['id']},\n"
                                                     f"имя - {data['name']},\n направление - {data ['nap']},\nвозраст - {data['age']},\n"
                                                     f"группа - {data['group']}")
    await FSMAdmin.next()
    await message.answer("Все правильно")

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower()== 'да':
        await sql_command_insert(state)
        await state.finish()
        await bot.send_message(message.from_user.id, 'Регистрация завершена')

def register_handlers_fsmmentor(dp:Dispatcher):
    dp.register_message_handler(fsm_start, commands=['ankets'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_nap, state=FSMAdmin.nap)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
