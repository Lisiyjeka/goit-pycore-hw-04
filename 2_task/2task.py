import json

def get_cats_info(path):
    """
    Читає файл з інформацією про котів та повертає список словників.
    
    Args:
        path (str): Шлях до файлу з даними про котів
        
    Returns:
        list: Список словників з інформацією про кожного кота
    """
    try:
        cats_list = []
        
        with open(path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:  # Пропускаємо порожні рядки
                    continue
                
                # Розділяємо рядок по комам
                parts = line.split(',')
                
                # Перевіряємо чи є всі три частини
                if len(parts) != 3:
                    print(f"Попередження: Рядок {line_num} має неправильний формат: '{line}'")
                    continue
                
                id, name, age = parts
                
                # Створюємо словник для поточного кота
                cat_info = {
                    "id": id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                }
                
                cats_list.append(cat_info)
        
        return cats_list
    
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Неочікувана помилка: {e}")
        return []

# використання функції , та приведення до читабельного формату за допомогою вбудованого модуля json
cats_info = get_cats_info("2_task/cats_file.txt")

print(json.dumps(cats_info, indent=1, ensure_ascii=False))