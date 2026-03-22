from aiogram.types import InlineKeyboardMarkup
from .bulider import get_callback_btns

def get_canel() -> InlineKeyboardMarkup:
    return get_callback_btns(
        btns={
            "⬅️ Назад": "canel"
        },
        sizes=(1,),
    )