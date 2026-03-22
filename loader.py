import os

# Папка, где лежат распакованные part1.sql, part2.sql и прочее
input_folder = r"C:\Users\gsg47.РПРО\OneDrive\Рабочий стол\уроки пайтон\osint_bot\unpacked_data"
output_file = r"C:\Users\gsg47.РПРО\OneDrive\Рабочий стол\уроки пайтон\osint_bot\all_data_final.txt"

def universal_cleaner():
    print("--- ЗАПУСК УНИВЕРСАЛЬНОЙ ОЧИСТКИ ---")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            
            # Пропускаем папки, берем только файлы
            if not os.path.isfile(file_path):
                continue
                
            print(f"Обработка: {filename}...")
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                for line in infile:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Если это SQL: разбиваем на записи
                    if "VALUES" in line:
                        line = line.split("VALUES")[-1]
                    
                    # Убираем SQL-ные скобки и кавычки, превращаем в чистую строку
                    # Для CSV и TXT это просто почистит края
                    records = line.split("),(")
                    for rec in records:
                        clean_rec = rec.replace("(", "").replace(")", "").replace("'", "").replace(";", "")
                        if clean_rec.strip():
                            outfile.write(clean_rec.strip() + "\n")

    print(f"--- ГОТОВО! ---")
    print(f"Все данные собраны в: {output_file}")

if __name__ == "__main__":
    universal_cleaner()