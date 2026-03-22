from aiogram.types import ReplyKeyboardMarkup
from .bulider import get_reply_btns

def get_main() -> ReplyKeyboardMarkup:
    return get_reply_btns(
        btns={
            "🌐 поиск",
            "• Личный кабинет •",
            "📄 Подробнее"
        },
        sizes=(2,)
    )