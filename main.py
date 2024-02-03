from aiogram import Bot, Dispatcher, F
import asyncio
from dotenv import load_dotenv
import os
import logging
import sys
from aiogram.filters import Command

from utils.commands import set_commands
from handlers.start import get_start
from handlers.help import get_help
from state.register import RegisterState
from state.create import CreateState
from handlers.register import start_register, register_phone, register_name
from handlers.admin.create import create_category_income, select_category, select_date, select_amount, create_category_expensens

load_dotenv()

TOKEN = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

async def start_bot(bot: Bot):
    await bot.send_message(506673528, text='Бот Запущен')

dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))
dp.message.register(get_help, Command(commands='help'))

# Регистрируем хэндлеры регистрации
dp.message.register(start_register, F.text=='Активация бота')
dp.message.register(get_help, F.text=='Помощь')

dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone, RegisterState.regPhone)

#Регистрируем хэндлеры с записей по доходам и расходам
dp.message.register(create_category_income, F.text == 'Доходы/Расходы')
dp.message.register(create_category_expensens, F.text == 'Расходы')
dp.callback_query.register(select_category, CreateState.categories)
dp.callback_query.register(select_date, CreateState.date)

dp.message.register(select_amount, CreateState.amount)


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())


