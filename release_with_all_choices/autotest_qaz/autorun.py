import os
import subprocess
import sys
import re
from pathlib import Path

project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

from lib.UtilsManager import *

TEST_DIR = '/web'
utils = UtilsManager()
current_dir = os.path.dirname(os.path.abspath(__file__))

def find_config_files():
    pattern = re.compile(r'config_v\d-\d-\d{2}\.json')
    return [f for f in os.listdir('.') if pattern.match(f) and os.path.isfile(f)]

def find_file(filename, search_dir=None):
    if search_dir is None:
        search_dir = current_dir
    for root, dirs, files in os.walk(search_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

def parse_arguments():
    return [ arg for arg in sys.argv[1:] 
        if arg in ['--pytest', '--help', '--no-kiwi'] or arg.startswith('--groups=')]    

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
    
def run_python_script(script_path):
    
    if not os.path.exists(script_path):
        print(f"ОШИБКА: Файл {script_path} не найден")
        return False
    
    cmd = [sys.executable, script_path] + parse_arguments() + browser_parse_arg() + headless_parse_arg()
    
    try:
        
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Ошибка: {script_path}")
        return False


def choosing_config_file():
    files = sorted(find_config_files())
    
    if not files:
        print("Файлы конфигурации не найдены")
        return None
    
    print("Найдены файлы конфигурации:")
    for i, filename in enumerate(files, 1):
        print(f"{i}. {filename}")
    
    while True:
        try:
            choice = input(f"\nВыберите файл (1-{len(files)} или 0 для выхода): ")
            if choice == '0':
                sys.exit(0)
    
            index = int(choice) - 1
            if 0 <= index < len(files):
                selected_file = files[index]
                #print(f"Выбран файл: {selected_file}")
                
                # Сохраняем выбор в JSON1
                with open('set_conf.json', 'r+', encoding='utf-8') as f:
                    json.dump({
                        "selected_file": selected_file,
                    }, f, ensure_ascii=False, indent=2)
                
                #print("Выбор сохранен в set_conf.json")
                return selected_file
            else:
                print("Неверный номер")
        except (ValueError, KeyboardInterrupt):
            print("Введите корректный номер")
    

def print_help_message():
    """Выводит справочную информацию"""
    help_text = """
Использование:
  python3 ./autorun.py [ОПЦИИ]

Опции:
  -h, --help          Показать эту справку и выйти
  --pytest            Запуск тестов с помощью pytest
  --groups            Запуск только указанных групп тестов
                      
Примеры:
  python autorun.py                               # Полный запуск
  python autorun.py --groups=1,3,5-8              # Выборочный запуск
  python autorun.py --pytest                      # Через pytest
  python autorun.py --groups=1,3,5-8 --pytest     # Запуск с использованием нескольких опций
    """
    print(help_text)
    
def main():
    if any(help_arg in sys.argv for help_arg in ['--help']):
        print_help_message()
        sys.exit(0)
    
    if not '--no-kiwi' in sys.argv: 
        make_test_path = find_file("make_test_run.py")
        if not make_test_path:
            print("ОШИБКА: make_test_run.py не найден")
            return
        
        if not run_python_script(make_test_path):
            return
    
    choosing_config_file()
    data = utils.load_config()
    utils.kiwi.test_run_start(data['test_run_id'])
    test_path = find_file("pre-final_vers.py", f"{current_dir}{TEST_DIR}")    
    if test_path and run_python_script(test_path):
        utils.kiwi.test_run_stop(data['test_run_id'])

if __name__ == "__main__":
    

    try:
        main()
    except KeyboardInterrupt:
            print("Принудительное завершение работы")
            sys.exit(1)     