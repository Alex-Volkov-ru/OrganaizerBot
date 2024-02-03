from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard
from utils.database import Database
import os
from keyboards.profile_kb import profile_kb

HELP_COMMAND = """
<b>Старт</b>  -  <em>запуск меню Телеграмм Бота</em>
<b>Доходы / Расходы</b>  -  <em>запись доходов или расходов по различным категориям</em>
<b>Статистика</b>  -  <em>информация об финансов: день, неделя, месяц, год.</em>
<b>Баланс</b>  -  <em>информация об твоём Балансе на данный момент</em>
<b>Написать нам</b>  -  <em>Telegram = @ximikat01</em>

<em>Приятного использования!</em>"""
async def get_help(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, HELP_COMMAND)