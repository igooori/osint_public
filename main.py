import asyncio
from aiogram import Bot,Dispatcher
from settings import TOKEN
import socket
from aiogram.client.session.aiohttp import AiohttpSession
import aiohttp
from aiohttp import TCPConnector
from aiogram.types import BotCommand
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.bot import DefaultBotProperties
from models.base import Base,engine
from handlers.check_user import router as check_router
from admin.panel import router as stats_router
from handlers.clear_phone import router as phone_router
# from handlers.google_handlers import router as google_router
from handlers.canel import router as canel_router

dp = Dispatcher()
# async def set_my_commands(bot:Bot):
#     commands = [
#         BotCommand(command='start',description='👋 Начать работ')
#     ]
#     await bot.set_my_commands(commands)
async def main():
    # session = AiohttpSession()
    bot = Bot(
    token=TOKEN,
    # session=session,
    # default=DefaultBotProperties(parse_mode='HTML')
    )

    print('бот запускаеться')
    dp.include_router(canel_router)
    dp.include_router(phone_router)
    # dp.include_router(google_router)
    dp.include_router(stats_router)
    dp.include_router(check_router)
    # await set_my_commands(bot)
    # await dp.start_polling(bot)

    await dp.start_polling(bot, request_timeout=120)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("⭕ Бот остановлен вручную")