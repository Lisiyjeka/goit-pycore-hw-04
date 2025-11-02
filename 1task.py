# Функція для обчислення загальної та середньої заробітної плати з файлу
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if not lines:
            return (0, 0)
        
        total = 0
        count = 0
        
        for line in lines:
            line = line.strip()
            if line:
                try:
                    # Розділяємо рядок по комі та беремо другу частину (зарплата)
                    salary = int(line.split(',')[1])
                    total += salary
                    count += 1
                except (ValueError, IndexError):
                    # Пропускаємо рядки з неправильним форматом
                    continue
        
        if count == 0:
            return (0, 0)
        
        average = total // count  # Ціле число для середньої зарплати
        return (total, average)
    
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return (0, 0)

# виклик функції для тестування
if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")