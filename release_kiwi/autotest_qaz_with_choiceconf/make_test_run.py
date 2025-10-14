import json
import sys
import os
from  lib.UtilsManager import *
from typing import Dict, Any

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.abspath(parent_dir))
path= project_root.parent / 'set_conf.json'
with open( path, 'r', encoding='utf-8') as f:
             data = json.load(f)
             setting = data['selected_file']
name="AutoTest with case"

# Записываем значение переменной в файл
def save_variable_to_file(value):
    filename = os.path.join(current_dir, f"{setting}")
    try:
        # Читаем текущий конфиг
        with open(filename, 'r', encoding='utf-8') as file:
            config: Dict[str, Any] = json.load(file)
        
        config['test_run_id'] = value
        
        # Записываем обратно с сохранением форматирования
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=4, ensure_ascii=False)
            
        print(f"Успешно обновлен test_run_id = {value} в {filename}")
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Конфиг файл не найден: {filename}")
    except json.JSONDecodeError:
        raise ValueError(f"Ошибка чтения JSON в файле: {filename}")
    except Exception as e:
        raise IOError(f"Ошибка при обновлении конфига: {str(e)}")

test_cfg=UtilsManager()
config_full = test_cfg.load_config()
#создание TestRun c TestCase с последней ревизией
add_len,run_id=test_cfg.kiwi.create_full_test_run('autotestpy',config_full['test_plan_id'],config_full['product_id'],name)
save_variable_to_file(run_id)

