import aiosqlite
import asyncio
import time
import re
import os
from aiogram import Router, F
from aiogram.types import Message
import json
import subprocess
from aiogram.filters import Command

router = Router() 


CH_PATH = "/usr/bin/clickhouse"
CH_DATA = "/run/media/syntax/fe41420a-2b2c-46da-95d2-916bf3b50f52/clickhouse_data_new"
async def search(user_query, status_callback=None):
    start_time = time.time() #
    search_term = user_query.strip()
    clean_phone = "".join(filter(str.isdigit, search_term))
    
    if clean_phone and len(clean_phone) >= 10:
        phone_target = clean_phone[-10:]
        sql = (
            f"SELECT raw_data FROM osint "
            f"WHERE phone IN ('{phone_target}', '7{phone_target}', '8{phone_target}') "
            f"LIMIT 30 FORMAT JSONEachRow"
        )
    else:
        if status_callback:
            await status_callback("🔍 Глубокое сканирование всей записи...")
        
        search_phrase = search_term.strip()
        if not search_term: 
            return None, 0
        
        sql = (
            f"SELECT raw_data FROM default.osint " 
            f"WHERE raw_data ILIKE '%{search_phrase}%' "
            f"LIMIT 30 FORMAT JSONEachRow "
            f"SETTINGS max_execution_time=300, max_threads=1, priority=1"
        )

    try:
        my_env = os.environ.copy()
        my_env["LANG"] = "ru_RU.UTF-8"

        process = await asyncio.create_subprocess_exec(
            "clickhouse-client", 
            "--query", sql,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=my_env
        )
        
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=105)

        if stderr:
            error_msg = stderr.decode('utf-8', errors='ignore')
            if "INDEX_NOT_USED" not in error_msg:
                print(f"🔴 Ошибка ClickHouse: {error_msg}")

        results = []
        output = stdout.decode('utf-8', errors='ignore').strip()
        
        if output:
            for line in output.split('\n'):
                if not line.strip(): continue
                try:
                    item = json.loads(line)
                    raw = item.get('raw_data', '')
                    if isinstance(raw, str) and (raw.startswith('{') or raw.startswith('[')):
                        results.append(json.loads(raw))
                    elif isinstance(raw, dict):
                        results.append(raw)
                    else:
                        results.append({"Данные": raw})
                except Exception as je:
                    print(f"Ошибка парсинга строки: {je}")
                    continue
                
        return results, round(time.time() - start_time, 2)

    except Exception as e:
        print(f"🔴 Search Error: {e}")
        return None, 0
LABELS = {
    'fio': '👤 ФИО',
    'name': '👤 Имя',
    'phone': '📞 Телефон',
    'email': '📧 Email',
    'address': '🏠 Адрес',
    'addr': '🏠 Адрес',
    'birthday': '📅 Дата рождения',
    'pass': '🎫 Паспорт',
    'password': '🔑 Пароль',
    'login': '🆔 Логин',
    'source': '📂 Источник'
}

def format_record(data):
    text = "🔹 <b>Найдена запись:</b>\n"
    lines = []
    
    for key, value in data.items():
        if not value or str(value).lower() in ['none', '', 'nan']:
            continue
            
        label = LABELS.get(key.lower(), key.capitalize())
        
        lines.append(f"<b>{label}</b>: <code>{value}</code>")
    
    if not lines:
        return "Пустая запись"
        
    return text + "\n".join(lines)
@router.message(F.text, ~F.text.startswith("/"))
async def phone(message: Message):    
    status_msg = await message.answer('⏳ Начинаю поиск...')
    
    try:
        resultsm, duration = await search(message.text)
    except Exception as e:
        print(f"Ошибка в функции search: {e}")
        return

    try:
        if resultsm == "LIMIT_EXCEEDED":
            await status_msg.edit_text("⚠️ Слишком много данных. Уточните запрос.")
        elif resultsm:
            await status_msg.edit_text(f"✅ Найдено: {len(resultsm)} за {duration}с")
            for row in resultsm[:10]:
                await message.answer(format_record(row))
        else:
            await status_msg.edit_text(f"❌ Ничего не найдено ({duration}с)")
    except Exception as e:
        print(f"Не удалось отправить ответ в телеграм (сеть): {e}")


