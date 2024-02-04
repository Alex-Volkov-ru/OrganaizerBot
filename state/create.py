from aiogram.fsm.state import StatesGroup, State

class CreateState(StatesGroup):
    date = State()
    amount = State()
    categories = State()
    keys = State()
    wallet = State()
    wallet_id = State()
    category_id = State()
    name = State()
    category = State()


