from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def get_keyboard(buttons):
    kb = []
    from button in buttons:
        kb.append([KeyboardButton(text=button)])
    reply_markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return reply_markup