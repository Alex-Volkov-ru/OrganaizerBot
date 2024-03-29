from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Доходы/Расходы')],
    [KeyboardButton(text='Статистика')],
    [KeyboardButton(text='Баланс')],
    [KeyboardButton(text='Помощь')],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери пункт ниже')


category_type_kb = ReplyKeyboardMarkup(
keyboard=[
    [KeyboardButton(text='Доходы')],
    [KeyboardButton(text='Расходы')],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери пункт ниже'
)

balance_kb = ReplyKeyboardMarkup(
keyboard=[
    [KeyboardButton(text='Мой кошелёк')],
    [KeyboardButton(text='Настройка кошелька')],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери пункт ниже'
)

statistika_kb = ReplyKeyboardMarkup(
keyboard=[
    [KeyboardButton(text='Выписка за месяц')],
    [KeyboardButton(text='Выписка за неделю')],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери пункт ниже'
)
