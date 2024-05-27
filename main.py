from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import StateFilter
from aiogram import F
from config import TOKEN
from userstates import UserStates
from keyboard_helper import keyboards

import paris_service as ps

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Это СТАВКИ НА СПОРТ!!! 1X-BET", reply_markup=kb)
    await state.set_state(UserStates.BASE)

@dp.message(F.text == "Мои пари", StateFilter(UserStates.BASE))
async def my_paris(message: types.Message):
    text = "Список пари:"
    paris = ps.get_paris(message.from_user.id)
    for pari in paris:
        text += "\n" + '- ' + pari
    await message.answer(text)

@dp.message(F.text == "Создать пари", StateFilter(UserStates.BASE))
async def add_paris(message: types.Message):
    text = ps.add_pari(message.from_user.id, message.text)
    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())