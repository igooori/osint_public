from aiogram.types import InlineKeyboardMarkup
from .bulider import get_callback_btns

def get_info() -> InlineKeyboardMarkup:
    return get_callback_btns(
        btns={
            "📄 Подробнее": "info"
        },
        sizes=(1,),
    )