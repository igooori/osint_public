from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from urllib.parse import quote_plus

def get_osint(final_number: str) -> InlineKeyboardMarkup:
    n = "".join(filter(str.isdigit, str(final_number)))
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Глаз Бога", url=f"https://t.me/GlazBoga_TG_bot?start=i_{n}")
        ],
        [
            InlineKeyboardButton(text="💙 Написать в ВК", url=f"https://vk.me/id{n}"),
            InlineKeyboardButton(text="🟠 ОК", url=f"https://ok.ru/search?st.query={n}")
        ],
        [
            InlineKeyboardButton(text="💬 WhatsApp", url=f"https://wa.me/{n}"),
            InlineKeyboardButton(text="✈️ Telegram", url=f"https://t.me/share/url?url=%2B{n}")
        ],
        [
            InlineKeyboardButton(text="🔎 Искать везде (Google)", url=f"https://www.google.com/search?q={n}")
        ]
    ])
    return kb