from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard
from utils.database import Database
import os
from aiogram.fsm.context import FSMContext
from state.create import CreateState
from keyboards.profile_kb import profile_kb, category_type_kb, statistika_kb, balance_kb


async def get_start(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if (users):
        await bot.send_message(message.from_user.id, f'Здравствуйте, {users[1]}!', reply_markup=profile_kb)
    else:
        await bot.send_message(message.from_user.id, f'😊Здравствуйте {message.from_user.first_name} {message.from_user.last_name}, рад Вас видеть!\n'
                                                    f'💼Бот поможет вести статистику по Вашим доходам и расходам, а так же делать выписку по Вашему кошельку!💼\n'
                                                    f'Если возникнут вопросы, Вы можете пойти нахуй.😊\n\n\n', reply_markup=register_keyboard)

async def category_type(message: Message, state: FSMContext, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    await bot.send_message(message.from_user.id, f'выберите категорию ниже', reply_markup=category_type_kb)
    await state.set_state(CreateState.categories)

async def balance_type(message: Message, state: FSMContext, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    await bot.send_message(message.from_user.id, f'выберите категорию ниже', reply_markup=balance_kb)
    await state.set_state(CreateState.categories)

async def statistic_type(message: Message, state: FSMContext, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    await bot.send_message(message.from_user.id, f'выберите категорию ниже', reply_markup=statistika_kb)
    await state.set_state(CreateState.categories)


