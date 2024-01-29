from aiogram.fsm.state import StatesGroup, State

class CreateState(StatesGroup):
    place = State()
    date = State()
    amount = State()
    categories = State()
