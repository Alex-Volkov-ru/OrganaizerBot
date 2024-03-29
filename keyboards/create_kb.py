from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
import os
import datetime
from utils.database import Database
def categoriesIncome_kb():
    db = Database(os.getenv('DATABASE_NAME'))
    category = db.db_select_Income('categories')
    kb = InlineKeyboardBuilder()
    for categories in category:
        kb.button(text=f'{categories[1]}', callback_data=f'{categories[0]}')
    kb.adjust(4)
    return kb.as_markup()
def categoriesExpenses_kb():
    db = Database(os.getenv('DATABASE_NAME'))
    category = db.db_select_Expenses('categories')
    kb = InlineKeyboardBuilder()
    for categories in category:
        kb.button(text=f'{categories[1]}', callback_data=f'{categories[0]}')
    kb.adjust(4)
    return kb.as_markup()

def date_kb():
    kb = InlineKeyboardBuilder()
    current_date = datetime.date.today()
    for i in range(31):
        current_date -= datetime.timedelta(days=1)
        kb.button(text=f"{current_date.strftime('%d.%m')}", callback_data=f"{current_date.strftime('%d.%m.%y')}")
    kb.adjust(4)
    return kb.as_markup()





