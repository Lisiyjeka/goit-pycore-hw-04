
"""
Скрипт для візуалізації структури директорії
Використання: python3 directory_tree.py /Users/user/Documents/study-all-materials/goit-pycore-hw-04
"""

import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для кольорового виводу
init(autoreset=True)

def print_directory_structure(directory_path, prefix="", is_last=True):
    """
    Рекурсивно виводить структуру директорії з кольоровим форматуванням
    
    Args:
        directory_path (Path): Шлях до директорії
        prefix (str): Префікс для відступів
        is_last (bool): Чи є поточний елемент останнім у списку
    """
    try:
        # Отримуємо всі елементи директорії та сортуємо їх
        items = sorted(directory_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        # Визначаємо символ для поточного рівня
        connector = "└── " if is_last else "├── "
        
        # Виводимо поточну директорію
        print(prefix + connector + Fore.BLUE + f"📁 {directory_path.name}" + Style.RESET_ALL)
        
        # Оновлюємо префікс для наступних рівнів
        new_prefix = prefix + ("    " if is_last else "│   ")
        
        for index, item in enumerate(items):
            # Визначаємо чи є поточний елемент останнім
            item_is_last = index == len(items) - 1
            
            if item.is_dir():
                # Рекурсивно обробляємо піддиректорії
                print_directory_structure(item, new_prefix, item_is_last)
            else:
                # Виводимо файл з відповідним кольором
                file_connector = "└── " if item_is_last else "├── "
                file_emoji = "📄"
                print(new_prefix + file_connector + Fore.GREEN + f"{file_emoji} {item.name}")
                
    except PermissionError:
        # Обробка помилок доступу
        error_connector = "└── " if is_last else "├── "
        print(prefix + error_connector + Fore.RED + f"⛔ [Доступ заборонено]")

def main():
    """Основна функція скрипта"""
    # Перевіряємо кількість аргументів
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: Необхідно вказати шлях до директорії")
        print(Fore.YELLOW + "Використання: python directory_tree.py /шлях/до/директорії")
        sys.exit(1)
    
    # Отримуємо шлях з аргументів командного рядка
    directory_path = Path(sys.argv[1])
    
    # Перевіряємо чи існує шлях
    if not directory_path.exists():
        print(Fore.RED + f"Помилка: Шлях '{directory_path}' не існує")
        sys.exit(1)
    
    # Перевіряємо чи це директорія
    if not directory_path.is_dir():
        print(Fore.RED + f"Помилка: '{directory_path}' не є директорією")
        sys.exit(1)
    
    # Виводимо заголовок
    print(Fore.CYAN + f"🌳 Структура директорії: {directory_path.absolute()}")
    print(Fore.CYAN + "=" * 50)
    
    # Виводимо структуру директорії
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()