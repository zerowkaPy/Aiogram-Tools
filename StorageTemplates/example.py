from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext

import asyncio
from dotenv import load_dotenv
from os import getenv

from postgre_storage import PostgreStorage

load_dotenv("params.env")       #Get the .env file, which should be located in your project folder
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE_URL = getenv("DATABASE_URL")


bot = Bot(BOT_TOKEN)


dp = Dispatcher(storage=PostgreStorage())  #We pass PostgreStorage() to dispatcher
user_router = Router()

dp.include_router(user_router)

@dp.shutdown()             #This handle is required and is needed to close the connection to the database
async def on_shutdown():
    await PostgreStorage.close()


@user_router.message(CommandStart())
async def start_user_handler(message:Message, state:FSMContext):
    await message.answer("Hi!")



async def main():
    await PostgreStorage.set_pool(DATABASE_URL)  #This method is also necessary because it establishes a connection to the database
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
