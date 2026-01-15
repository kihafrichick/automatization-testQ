from .import_file import *


def find_config_files():
    pattern = re.compile(r'config_v\d-\d-\d{2}\.json')
    return [f for f in os.listdir('.') if pattern.match(f) and os.path.isfile(f)]

def parse_arguments():
    return [ arg for arg in sys.argv[1:] 
        if arg in ['--pytest', '--help', '--nokiwi'] or arg.startswith('--groups=')]    

def browser_parse_arg():
    if any(arg in sys.argv[1:] for arg in ['--firefox','fx']):
        os.environ['BROWSER_OPTION'] = 'firefox'
        return ['--firefox']
    else:
        os.environ['BROWSER_OPTION'] = 'chrome'
        return []

def headless_parse_arg():
    if any(arg in sys.argv[1:] for arg in ['--headless','-hl']):
        os.environ['BROWSER_VIEW_OPTION'] = 'headless'
        return ['--headless']
    else:
        os.environ['BROWSER_VIEW_OPTION'] = 'show'
        return []
    

def select_file_for_device(unit_name):
    files = sorted(find_config_files())
    
    if not files:
         print("Файлы конфигурации не найдены")
         return None
    
    print("Найдены файлы конфигурации:")
    for i, filename in enumerate(files, 1):
         print(f"{i}. {filename}")
    
    """Выбор файла для указанного устройства"""
    while True:
        try:
            choice = input(f"\nВыберите файл для {unit_name} (1-{len(files)} или 0 для выхода): ")
            if choice == '0':
                sys.exit(0)
            
            index = int(choice) - 1
            if 0 <= index < len(files):
                selected_file = files[index]
                print(f"Выбран файл для {unit_name}: {selected_file}")
                return selected_file
            else:
                print("Неверный номер")
        except (ValueError, KeyboardInterrupt):
            print("Введите корректный номер")

def select_scenario():
    """Выбор сценария с автоматической настройкой режимов"""
    print("""Выберите сценарий работы:
    
1. Unit--Blade    (Устройство 1: dev_val, Устройство 2: dev_val_blade)
2. Unit--Unit     (Оба устройства: dev_val)
3. Blade--Unit    (Устройство 1: dev_val_blade, Устройство 2: dev_val)
4. Blade--Blade   (Оба устройства: dev_val_blade)""")
    
    while True:
        choice = input("\nВведите цифру (1-4): ").lower().strip()
        
        if choice in ['1']:
            # Устройство 1: dev_val, Устройство 2: dev_val_blade
            os.environ['DEVICE_1_MODE'] = 'dev_val'
            os.environ['DEVICE_2_MODE'] = 'dev_val_blade'
            return 'device1_normal', 'device2_blade'
            
        elif choice in ['2']:
            # Оба устройства: dev_val
            os.environ['DEVICE_1_MODE'] = 'dev_val'
            os.environ['DEVICE_2_MODE'] = 'dev_val'
            return 'device1_normal', 'device2_normal'
            
        elif choice in ['3']:
            # Устройство 1: dev_val_blade, Устройство 2: dev_val
            os.environ['DEVICE_1_MODE'] = 'dev_val_blade'
            os.environ['DEVICE_2_MODE'] = 'dev_val'
            return 'device1_blade', 'device2_normal'
            
        elif choice in ['4']:  # Б--Б
            # Оба устройства: dev_val_blade
            os.environ['DEVICE_1_MODE'] = 'dev_val_blade'
            os.environ['DEVICE_2_MODE'] = 'dev_val_blade'
            return 'device1_blade', 'device2_blade'
            
        else:
            print("Некорректный выбор. Введите 1, 2, 3 или 4")

def choosing_config_file():
    first_file = select_file_for_device("первого устройства")
    second_file = select_file_for_device("второго устройства")

    with open('set_conf.json', 'r+', encoding='utf-8') as f:
        json.dump({
            "sborka_sinhron": {"conf_file": first_file},
            "sborka_sinhron_blade": {"conf_file_blade": second_file}
        }, f, ensure_ascii=False, indent=2)

def parse_group_selection(groups_str: str) -> Set[int]:
    """Парсит строку с номерами групп в множество чисел"""
    selected_groups = set()
    if not groups_str:
        return selected_groups
    
    for part in groups_str.split(','):
        part = part.strip()
        if '-' in part:
            start, end = map(int, part.split('-'))
            selected_groups.update(range(start, end + 1))
        else:
            selected_groups.add(int(part))
    
    return selected_groups

def print_help_message():
    """Выводит справочную информацию"""
    help_text = """
Использование:
  python3 ./autorun.py [ОПЦИИ]

Опции
  -h, --help            Показать это сообщение и выйти
  --groups , -g 	      Номера групп для запуска (например: groups=1,3,5-8)                       
  --pytest              Запустить через pytest
  --nokiwi             Запустить без создания test run в Kiwi TCMS
  --headless            Опция для запуска без отображения действия скрипта
  --firefox/fx          Выбор браузера Firefox (по умолчанию скрипт запустится в Google-chrome)
                    
Примеры:
  python autorun.py                               # Полный запуск
  python autorun.py --groups=1,3,5-8              # Выборочный запуск
  python autorun.py --pytest                      # Через pytest
  python autorun.py --groups=1,3,5-8 --pytest     # Запуск с использованием нескольких опций
    """
    print(help_text)