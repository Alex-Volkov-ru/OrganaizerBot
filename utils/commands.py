from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start', # Команда
            description='Запускаем бота'   # Описание команды
        ),
        BotCommand(
            command='help',
            description='Помощь в работе с ботом'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())