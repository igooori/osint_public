from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from settings import ADMIN_ID
from models.base import SearchLog,async_session_maker
from sqlalchemy import select,func

router = Router()

@router.message(Command('stats'))
async def admin_stats(message:Message):
    user = message.from_user.id
    if ADMIN_ID == user:
        name = message.from_user.username
        response = f"Привет, {name}"
        async with async_session_maker() as session:
            query = select(func.count()).select_from(SearchLog)
            result = await session.execute(query)
            total = result.scalar()
            await message.answer(f"📊 {response}. Всего запросов: {total}")
    else:
        await message.answer('вы не админ')

