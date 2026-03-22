# from urllib.parse import quote


# def dork_links(target):
#     clean_target = target.strip().replace("@", "")

#     dorks = {
#         "📸 Instagram": f"https://www.instagram.com/{clean_target}/",
#         "💙 VKontakte": f"https://vk.com/{clean_target}",
#         "✈️ Telegram": f"https://t.me/{clean_target}",
#         "📘 Facebook": f"https://www.facebook.com/{clean_target}",
#         "---": "sep",
#         "🔍 Поиск упоминаний (Google)": f"https://www.google.com/search?q={quote(f'@{clean_target} | \"{clean_target}\"')}"
#     }
#     google_query = f'@{clean_target} | "{clean_target}" '
#     dorks["🔍 Поиск упоминаний (Google)"] = f"https://www.google.com/search?q={quote(google_query)}"
#     return dorks