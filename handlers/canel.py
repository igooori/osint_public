from aiogram import Router,F
from aiogram.types import CallbackQuery
from keyboards.canel_keyboard import get_canel
from keyboards.help_keyboard import get_info
router = Router()

@router.callback_query(F.data == 'canel')
async def canel_global(callback:CallbackQuery):
    txt = (f"""Привет, {callback.from_user.first_name}! 🔍

Введите Username, чтобы начать мгновенный поиск по базам GitHub, VK и TikTok.

Я просканирую открытые источники и найду активные профили.""")
    try:
        await callback.message.edit_text(
            text=txt,
            reply_markup=get_info()
        )
    except:
        await callback.message.answer(
            text=txt,
            reply_markup=get_info()
        )
    await callback.answer()