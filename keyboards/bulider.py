from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_callback_btns(*, btns: dict[str, str], sizes: tuple[int] = (2,), url_btns: dict[str, str] = None):
    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

    if url_btns:
        for text, url in url_btns.items():
            keyboard.add(InlineKeyboardButton(text=text, url=url))

    return keyboard.adjust(*sizes,).as_markup()

def get_reply_btns(*, btns: list[str], sizes: tuple[int] = (2,)):
    keyboard = ReplyKeyboardBuilder()

    for text in btns:
        keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(resize_keyboard=True)