import os
import sys
import uuid
import tempfile
import time
import logging
import json
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)

TEST_ID_KIWI = 126 
os.chdir('./autotest_qaz')
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
print("ufd ufd",os.getcwd())

from lib.UtilsManager import *

test_cfg = UtilsManager()
cfg_file = 'config.json'
config = test_cfg.load_config()

# --- Настройка драйвера ---
script_name = os.path.splitext(os.path.basename(__file__))[0]
user_data_dir = os.path.join(tempfile.gettempdir(), f'chrome_{script_name}_{uuid.uuid4()}')

options = webdriver.ChromeOptions()
service = Service(executable_path='/usr/bin/chromedriver', log_path='/tmp/chromedriver.log')
options.binary_location = '/usr/bin/google-chrome'
driver = webdriver.Chrome(service=service, options=options)

config_path = test_cfg.find_config_file(cfg_file)

with open(config_path, 'r', encoding='utf-8') as f:
         config = json.load(f)
            
def take_screenshot(test_name = "1"):
    """Сохраняет скриншот текущей страницы и возвращает путь к файлу."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    screenshot_dir = os.path.join(script_dir, 'screenshots')
    os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{screenshot_dir}/{test_name}_screenshot_{timestamp}.png"
    driver.save_screenshot(output_filename)
    print(f"Screenshot saved to {output_filename}")
    global filename
    filename = output_filename
    return filename

    
def web_ident():
    try:
        driver.get("http://192.168.17.223") 
        driver.set_window_size(1854, 1011)
        time.sleep(2)
        driver.find_element(By.ID, "login").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.ID, "password").click()
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys("cradmin")
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(7) > .ui-dialog-buttonpane .ui-button").click()
        time.sleep(2)
        print("Quasar-2: Авторизация: OK")
        return True 
    except Exception as e:
        print("Quasar-2: Авторизация: ERROR")
        return False 

def function_15():
    try:
        driver.find_element(By.LINK_TEXT, "Пользователи").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".bg_page").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".user-element:nth-child(1) .on-click-view-session-permissions").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(23) > .ui-dialog-buttonpane .ui-button").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".user-element:nth-child(2) .on-click-set-permissions").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) .ui-button:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".user-element:nth-child(3) .on-click-set-passexp").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(23) > .ui-dialog-buttonpane .ui-button").click()
        time.sleep(1)
        take_screenshot()
        print("Вкладка 'Пользователь': ОК")
        return True 
    except Exception as e:
        print("Вкладка 'Пользователь': ERROR")
        return False

def main():
    global filename
    try:
        result_1 = web_ident()
        result_2 = function_15()
                
 
        if result_1 and result_2:
            test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
            test_cfg.add_screenshot_to_kiwi(config['test_run_id'], TEST_ID_KIWI,filename)
            test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
        else:
            msg = "web_ident or function_15 failed"
            test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', msg)
            test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, msg)
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
        test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
