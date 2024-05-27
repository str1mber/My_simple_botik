from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import StateFilter
from config import TOKEN
from userstates import UserStates
from keyboard_helper import keyboards

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Я эхо-лот, ха-ха-ха", reply_markup=kb)
    await state.set_state(UserStates.BASE)

@dp.message(Command("test"), StateFilter(UserStates.BASE))
async def start(message: types.Message):
    await message.answer("О нет! Что ты наделал?! Теперь мы все умреееем!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())