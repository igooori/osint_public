import asyncio
from aiogram import Bot,Router,F
from aiogram.types import Message
from aiogram.filters import Command
# from keyboards.main_keyboard import get_main
from keyboards.canel_keyboard import get_canel
from keyboards.main_kb import get_main
from aiogram.types import CallbackQuery

router = Router()

@router.message(Command('start'))
async def start(message:Message):
    name = message.from_user.first_name or "пользователь"
    response = f"""Привет, {name}! 🛡️

<b>Начни легальный OSINT-поиск прямо сейчас.</b>

📍 <b>Доступные методы поиска:</b>
• По номеру телефона (РФ/СНГ)
• По ФИО

<i>Все данные взяты из открытых и архивных источников в ознакомительных целях.</i>"""
    
    try:
        await message.answer(response,reply_markup=get_main())
    except:
        await message.edit_text(response,reply_markup=get_main)
@router.message(F.text == "📄 Подробнее")
async def info(message:Message):
    response = f"""
<b>⚡️ Система мониторинга OSINT </b>

<b>📍 Доступные методы анализа:</b>

📞 <code>79966340060</code> — поиск по номеру телефона (реестры, контакты).
👤 <code>Иванов Иван</code> — поиск по ФИО (упоминания в архивах и событиях).
🚘 <code>А111АА777</code> — проверка транспортных средств по госномеру/VIN.
🆔 <code>@username</code> — поиск по уникальному идентификатору (GitHub/VK).

<b>ℹ️ Как пользоваться:</b>
Просто отправьте боту текст в нужном формате (как в примерах выше). Бот сам определит тип данных и запустит поиск.

<b>💡 Управление:</b>
• 💳 <b>Подписка:</b> для доступа к полным отчетам.
• 🛠 <b>Помощь:</b> связь с техподдержкой и инструкции.

<i>Все данные получены из открытых и архивных источников. Поиск анонимен.</i>
"""
    await message.edit_text(response,parse_mode='HTML',reply_markup=get_canel())
@router.message(F.text == '🌐 поиск')
async def poisk(message:Message):
    await message.answer()