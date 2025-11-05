import os
import re
import sys

def find_config_files():
    """Найти файлы конфигурации по шаблону config_vX-X-XX.json"""
    pattern = re.compile(r'config_v\d-\d-\d{2}\.json')
    return [f for f in os.listdir('.') if pattern.match(f) and os.path.isfile(f)]

def choosing_config_file():
    files = sorted(find_config_files())
    
    if not files:
        print("Файлы конфигурации не найдены")
        return
    
    print("Найдены файлы конфигурации:")
    for i, filename in enumerate(files, 1):
        print(f"{i}. {filename}")
    
    while True:
        try:
            choice = input("\nВыберите файл (1-{} или 0 для выхода): ".format(len(files)))
            if choice == '0':
                return
            
            index = int(choice) - 1
            if 0 <= index < len(files):
                selected_file = files[index]
                print(f"Выбран файл: {selected_file}")
                # Здесь можно добавить дальнейшую обработку выбранного файла
                break
            else:
                print("Неверный номер")
        except (ValueError, KeyboardInterrupt):
            print("Введите корректный номер или 0 для выхода")


if __name__ == "__main__":
    choosing_config_file()