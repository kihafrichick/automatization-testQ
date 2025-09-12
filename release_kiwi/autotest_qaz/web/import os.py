import os
import sys
import uuid
import tempfile
import time
import logging
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TEST_ID_KIWI = 126 
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))


from lib.UtilsManager import *

test_cfg = UtilsManager()
config = test_cfg.load_config()


def test_upload():
    test_run_id = config['test_run_id']
    """Тестовая функция для проверки загрузки"""
    test_file = "test_screenshot.png"
    
    # Создаем тестовый файл
    with open(test_file, 'w') as f:
        f.write("test content")
    
    # Пробуем загрузить
    success = test_cfg.add_screenshot_to_kiwi(
        test_run_id,           # ваш test_run_id
        file_path=test_file,         
        description="Test upload"
    )
    
    print(f"Тест загрузки: {success}")
    os.remove(test_file)