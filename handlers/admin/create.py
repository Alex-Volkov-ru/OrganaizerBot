from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.create import CreateState
from keyboards.create_kb import categoriesIncome_kb, date_kb, categoriesExpenses_kb
from utils.database import Database
import os

async def create_category_income(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите категорию', reply_markup=categoriesIncome_kb())
    await state.set_state(CreateState.categories)

async def create_category_expensens(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите категорию', reply_markup=categoriesExpenses_kb())
    await state.set_state(CreateState.categories)

async def select_category(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Вы выбрали категорию!\n'
                              f'Дальше выберите дату.', reply_markup=date_kb())
    await state.update_data(categories=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.date)

async def select_date(callback_query: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback_query.from_user.id, f'Дата успешно выбрана и сохранена!\n'
                                                            f'Введите сумму.')
    await state.update_data(date=callback_query.data)
    await state.set_state(CreateState.amount)

async def select_amount(message: Message, state: FSMContext, bot: Bot):
    if (message.text.isdigit()):
        await bot.send_message(message.from_user.id, f'Отлично, я записал транзакцию! \n')
        await state.update_data(amount=message.text)
        create_data = await state.get_data()

        print(create_data)
    else:
        await bot.send_message(message.from_user.id,f'{message.text}, не верный формат! Нужно указать сумму')