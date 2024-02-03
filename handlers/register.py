from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re
import os
from utils.database import Database


async def start_register(message: Message, state: FSMContext, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if(users):
        await bot.send_message(message.from_user.id, f'{users[1]}, Бот уже активирован!')
    else:
        await bot.send_message(message.from_user.id,f'Давайте начнем регистрацию \nДля начала скажите, как к Вам обращаться? \n')
        await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id,f'😉Приятно познакомится {message.text}😉 \n'
                         f'Теперь укажите номер телефона, чтобы быть на связи \n'
                         f'📱Формат телефона +7ХХХХХХХХХХ 📱 \n\n'
                         f'⚠️Внимание!!! Я чувствителен к формату⚠️')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhone)

async def register_phone(message: Message, state: FSMContext, bot: Bot):
    if(re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        msg = f'Приятно познакомится {reg_name} \n\nТелефон {reg_phone}'
        await bot.send_message(message.from_user.id, msg)
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, message.from_user.id)
        await state.clear()
    else:
        await bot.send_message(message.from_user.id,f'{message.text}, номер указан в неверном формате!')