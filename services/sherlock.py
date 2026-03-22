from maigret.maigret import maigret as MaigretEngine
import os
from transliterate import translit
import logging
from maigret import MaigretDatabase

async def check_username(username:str):
    logger = logging.getLogger('maigret')
    if not logger.handlers:
        logger.addHandler(logging.NullHandler())
    try:
        angl_name = translit(username,'ru',reversed=True)
    except:
        angl_name = username
    clean_name = angl_name.replace("'", "").replace("`", "")
    final_us = clean_name.replace(" ", "")
    print(f"--- ЗАПУСК ПОИСКА ПО НИКУ: {final_us} ---")
    db = MaigretDatabase()
    try:
        db.load_from_file('data.json')
    except Exception as e:
        return [f"Ошибка загрузки базы: {e}"]
    target_sites = ['VK', 'Instagram', 'Facebook', 'Telegram']
    dict_sit = {}
    if isinstance(db.sites,list):
        for site in db.sites:
            if site.name in target_sites:
                dict_sit[site.name] = site
    else:
        for name in target_sites:
            if name in db.sites:
                dict_sit[name] = db.sites[name]
    if not dict_sit:
        return['Ошибка: Указанные сайты не найдены в базе data.json']
    try:
        serch = await MaigretEngine(username=final_us,site_dict=dict_sit,logger=logger,allow_redirects=True,timeout=10)
        links = []
        if isinstance(serch, dict):
                for site_name, data in serch.items():
                    status = data.get('status')
                    if status and (getattr(status, 'is_found', lambda: False)() or status == 'claimed'):
                        url = data.get('url_user')
                        links.append(f"✅ <a href='{url}'>{site_name}</a>")
        elif isinstance(serch, list):
            for res in serch:
                if res.status and res.status.is_found():
                    links.append(f"✅ <a href='{res.url_user}'>{res.site.name}</a>")
        if not links:
            return ['Совпадений не найдено']
        return links

    except Exception as e:
        import traceback
        traceback.print_exc()
        return [f"Ошибка при поиске: {e}"]