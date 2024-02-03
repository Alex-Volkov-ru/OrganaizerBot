from aiogram.filters import BaseFilter
from aiogram.types import Message
import os
from utils.database import Database

class CheckUser(BaseFilter):
    async def __call__(self, message: Message):
        try:
            user_id = os.getenv('USER_ID')
            db = Database(os.getenv('DATABASE_NAME'))
            users = db.select_user_id(message.from_user.id)
            return users[3] in user_id
        except:
            return False