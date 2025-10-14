import os
import sys
import json
from pathlib import Path
project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))
from KIWItcms.kiwitcmsclient import *
path= project_root.parent / 'set_conf.json'
with open( path, 'r', encoding='utf-8') as f:
             data = json.load(f)
             setting = data['selected_file']

class UtilsManager:
    def __init__(self, base_dir=None):
        """
        Инициализация менеджера утилит
        
        Args:
            base_dir (str/Path, optional): Базовый каталог проекта. Если None, определяется автоматически.
        """
        # Определяем базовый каталог 
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent
        
        # Добавляем каталог проекта в PYTHONPATH
        if str(self.base_dir) not in sys.path:
            sys.path.append(str(self.base_dir))
        
        # Инициализация клиента KiwiTCMS (опционально)
        self.kiwi = self._init_kiwi_client()
        self.mappings=self.kiwi.get_status_mappings()
        # Конфигурация по умолчанию
        self.default_config = {
            "test_run_id": None,
            "order_run_id": None
        }

    def _init_kiwi_client(self):
        """Инициализирует клиент KiwiTCMS, если модуль доступен"""
        try:

            self.current_file = os.path.abspath(__file__)
            self.current_dir = os.path.dirname(self.current_file)

        
        # Добавляем родительскую директорию в PYTHONPATH
            sys.path.append(os.path.abspath(self.current_dir))
            from KIWItcms.kiwitcmsclient import KiwiTCMSClient
            return KiwiTCMSClient()
        except ImportError:
            print("Warning: KiwiTCMSClient not available")
            return None

    def find_config_file(self, cfg_file=f"{setting}"):
        """
        Ищет конфигурационный файл на уровень выше текущей директории
        
        Args:
            cfg_file (str): имя конфигурационного файла (по умолчанию "config.json")
            
        Returns:
            str: полный путь к конфигурационному файлу
            
        Raises:
            FileNotFoundError: если файл не найден
        """
        config_path = self.base_dir / cfg_file
        
        if not config_path.exists():
            raise FileNotFoundError(
                f"Конфигурационный файл не найден по пути: {config_path}\n"
                f"Создайте файл {cfg_file} в директории: {self.parent_dir}"
            )
        return config_path

    def load_config(self, cfg_file=f"{setting}"):
        """
        Загружает конфигурацию из JSON-файла
        
        Args:
            cfg_file (str): имя конфигурационного файла (по умолчанию "config.json")
            
        Returns:
            dict: загруженная конфигурация или значения по умолчанию в случае ошибки
        """
        try:
            config_path = self.find_config_file(cfg_file)
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Проверка обязательных полей
            required_fields = ["test_run_id"]
            missing_fields = [f for f in required_fields if f not in config]
            
            if missing_fields:
                print(f"Внимание: В конфиге отсутствуют поля: {missing_fields}. Используются значения по умолчанию")
                for field in missing_fields:
                    config[field] = self.default_config[field]
            
            # Добавляем отсутствующие необязательные поля
            for field in ["test_run_id", "order_run_id"]:
                if field not in config:
                    config[field] = self.default_config[field]
            
            return config
        
        except json.JSONDecodeError as e:
            print(f"Ошибка в формате JSON: {e}. Используются значения по умолчанию")
            return self.default_config.copy()
        except Exception as e:
            print(f"Ошибка загрузки конфига: {e}. Используются значения по умолчанию")
            return self.default_config.copy()
    
    def update_kiwi(self,test_run,test_case: int,status,comment=None):
        cases=self.kiwi.get_executions_for_run(test_run)
        
        str1=self.mappings['name_to_id'][status] 
        for case in cases:
            if (case['case']==test_case): 
                self.kiwi.update_execution(case['id'],str1,comment)
                return 0
        return 1
    def add_comment_kiwi(self,test_run,test_case,comment=None):
        cases=self.kiwi.get_executions_for_run(test_run)
        for case in cases:
            if (case['case']==test_case):
                self.kiwi.add_comment_execution(case['id'],comment)
                return 0
        return 1
    
    def add_screenshot_to_kiwi(self, test_run: int, test_case: int, filename):
        cases=self.kiwi.get_executions_for_run(test_run)
        for case in cases:
            if (case['case']==test_case): 
                self.kiwi.add_attachment_to_execution(test_run, filename)
                return 0
        return 1
    
    def print_head_test(self, name_test):
        print("=" * 50)
        print(name_test)
        print("=" * 50)
        return


