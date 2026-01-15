import os
import subprocess
import sys
import re
from pathlib import Path
from web.work_funcs.parse_funcs import *
project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

from lib.UtilsManager import *

TEST_DIR = '/web'
utils = UtilsManager()
current_dir = os.path.dirname(os.path.abspath(__file__))

def find_file(filename, search_dir=None):
    if search_dir is None:
        search_dir = current_dir
    for root, dirs, files in os.walk(search_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None
    
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

    
def main():
    if any(help_arg in sys.argv for help_arg in ['--help']):
        print_help_message()
        sys.exit(0)
    if not '--nokiwi' in sys.argv: 
        make_test_path = find_file("make_test_run.py")
        if not make_test_path:
            print("ОШИБКА: make_test_run.py не найден")
            return
    
        if not run_python_script(make_test_path):
            return
        
    select_scenario()
    choosing_config_file()
    data = utils.load_config()
    utils.kiwi.test_run_start(data['test_run_id'])
    test_path = find_file("prefinal_vers.py", f"{current_dir}{TEST_DIR}")    
    if test_path and run_python_script(test_path):
        utils.kiwi.test_run_stop(data['test_run_id'])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            print("Принудительное завершение работы")
            sys.exit(1)     