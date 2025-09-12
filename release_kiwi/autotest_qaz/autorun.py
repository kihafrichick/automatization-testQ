import os
import subprocess
import json
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from  lib.UtilsManager import *
TEST_DIR='/web'
# Ваши данные
utils= UtilsManager()
data = utils.load_config()
# 1. Сначала запускаем make_test_run.py и ждем завершения
# Получаем путь к текущему скрипту для корректного поиска файлов
current_dir = os.path.dirname(os.path.abspath(__file__))

def find_file(filename, search_dir=None):
    """Поиск файла в указанной директории и поддиректориях"""
    if search_dir is None:
        search_dir = current_dir
        
    for root, dirs, files in os.walk(search_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

def run_python_script(script_path):
    """Запуск python-скрипта с обработкой ошибок"""
    if not os.path.exists(script_path):
        print(f"ОШИБКА: Файл {script_path} не найден")
        return False
    
    try:
        print(f"Запуск: {script_path}")
        result = subprocess.run([sys.executable, script_path], check=True)
        print(f"Успешно завершен: {script_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Скрипт завершился с ошибкой (код {e.returncode}): {script_path}")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка при выполнении {script_path}: {str(e)}")
        return False

# Основной код выполнения
def main():


    # 1. Запуск make_test_run.py

    make_test_path = find_file("make_test_run.py")
    if not make_test_path:
        print("ОШИБКА: Файл make_test_run.py не найден")
        print("Поиск осуществлялся в:", current_dir)
        return
    
    if not run_python_script(make_test_path):
        print("Прерывание выполнения из-за ошибки в make_test_run.py")
        return 
    data = utils.load_config()
    utils.kiwi.test_run_start(data['test_run_id'])
    
    # 2. Поиск и запуск тестовых файлов
    for run_id in data["order_run_id"]:
        test_file = f"test_{run_id}.py"
        test_path = find_file(f"{test_file}",f"{current_dir}{TEST_DIR}")
        
        if not test_path:
            print(f"ПРЕДУПРЕЖДЕНИЕ: Файл {test_file} не найден, пропускаем")
            continue
            
        if not run_python_script(test_path):
            print(f"ПРЕДУПРЕЖДЕНИЕ: Проблема при выполнении {test_file}, продолжаем")
    utils.kiwi.test_run_stop(data['test_run_id'])
if __name__ == "__main__":
    main()