import os
import sys
import logging
import asyncio
import uuid
from pathlib import Path
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


#logging.basicConfig(level=logging.DEBUG)
                     #filename='output.log',          # Имя файла для логов
                             # Уровень логирования
                     #format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
                     #datefmt='%Y-%m-%d %H:%M:%S'     # Формат даты и времени
options = webdriver.ChromeOptions()
service = Service(executable_path='/usr/bin/chromedriver', log_path='/tmp/chromedriver.log') # Путь к chromedriver
options.binary_location =  '/usr/bin/google-chrome'  # Путь к браузеру Chrome
driver = webdriver.Chrome(service=service, options=options)

# os.chdir('./autotest_qaz/web')
project_root = Path(__file__).resolve().parent.parent
print("ufd ufd",os.getcwd())
config_path = project_root / 'config_v4-1-21.json'
with open(config_path, 'r', encoding='utf-8') as f:
         config = json.load(f)
sys.path.append(str(project_root))


path_number_1 = config['path_number_1']
path_number_2 = config['path_number_2']
from lib.UtilsManager import *
test_cfg = UtilsManager()

    #ПЕРЕХОД НА WEB-ИНТЕРФЕЙС
    
async def initialization_blade():
    TEST_ID_KIWI = 1381
    try:
            driver.get(config['quazar_IP_blade'])
            driver.set_window_size(1854, 1011)
            await asyncio.sleep(2)
            driver.find_element(By.ID, "login").send_keys("Admin")
            await asyncio.sleep(2)
            driver.find_element(By.ID, "password").click()
            await asyncio.sleep(2)
            driver.find_element(By.ID, "password").send_keys("cradmin")
            driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(7) > .ui-dialog-buttonpane .ui-button").click()
            await asyncio.sleep(2)
            test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
            test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
            print("Quasar-2:Переход на страницу и авторизация:OK")
            return True   
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
        test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
        print('Quasar-2:Переход на страницу и авторизация:ERROR')
        return False
        
        #СКАНИРОВАНИЕ ИНФОРМАЦИИ ИЗ ТАБЛИЦЫ ГЛАВНОЙ СТРАНИЦЫ
        
async def tab_scan_blade():
    TEST_ID_KIWI = 1382
    try:
        wait = WebDriverWait(driver, 20)
        table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.selected-cu-params.standard.even_odd')))
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')  
            print([cell.text.strip() for cell in cells])  # Print content of the cells
        with open(f"info_{config['web_ip_blade']}.txt", 'w', encoding='utf-8') as file:
            # Записываем содержимое таблицы в файл
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                # Получаем текст всех ячеек в строке
                row_data = [cell.text.strip() for cell in cells]
                # Записываем строку в файл (элементы разделены табуляцией или пробелами)
                file.write('\t'.join(row_data) + '\n')
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
        test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
        print("Quasar-2:Сканирование информации:OK")
        return True
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
        test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
        print("Quasar-2:Сканирование информации:ERROR")
        return False
    
    #ВКЛЮЧЕНИЕ КЛИЕНТСКОЙ И ОСНОВНЫХ ЛИНИЙ
        
async def line_power_on_blade():
    TEST_ID_KIWI = 1383
    try:
        driver.find_element(By.ID, f"{config['dev_val_blade']}st_descr").click()
        driver.find_element(By.ID, f"{config['first_page_blade']}").click()
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2SwitchState']} .on-click-edit").click()        
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Cl1SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Cl1SwitchState']} .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, "#edit_param_dialog .form-unit:nth-child(4)").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
        test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
        print("Quasar-2:Включение клиентской и основных линий:OK")
        return True
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
        test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
        print("Quasar-2:Включение клиентской и основных линий:ERROR")
        return False


    #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ ALS 
async def ALS_mode_change_blade():
    TEST_ID_KIWI = 1384
    try:
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1TxState']} .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2TxState']} .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Cl1TxState']} .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
        test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
        print("Quasar-2:Включение режима 'Управляется ALS':OK")
        return True
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
        test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
        print("Quasar-2:Включение режима 'Управляется ALS':ERROR")
        return False
    
    #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ FEC

async def FEC_mode_EFEC_blade():
    TEST_ID_KIWI = 1385 
    try:
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1FECState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2FECState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        print("Quasar-2:Установка режима 'FEC':OK")
        return True
    except Exception as e:
        print("Quasar-2:Установка режима 'FEC':ERROR")
        return False
    
async def FEC_mode_G709_blade():
    TEST_ID_KIWI = 1385
    try:
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1FECState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2FECState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        print("Quasar-2:Установка режима 'G.709':OK")
        return True
    except Exception as e:
        print("Quasar-2:Установка режима 'G.709':ERROR")
        return False
    
async def FEC_mode_off_blade():
    TEST_ID_KIWI = 1385
    try:
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1FECState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2FECState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        print("Quasar-2:Установка режима 'Выкл.':OK")
        return True
    except Exception as e:
        print("Quasar-2:Установка режима 'Выкл.':ERROR")
        return False
    
async def FEC_mode_G709_rep_blade():
    TEST_ID_KIWI = 1385
    try:
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1FECState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2FECState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(5)
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
        test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
        print("Quasar-2:Установка режима 'G.709':OK")
        return True
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
        test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
        print("Quasar-2:Установка режима 'G.709':ERROR")
        return False

    #ПЕРЕКЛЮЧЕНИЕ СТАТУСОВ ALS 

async def ALS_status_ImpAuto_blade():
    TEST_ID_KIWI = 1386
    try:
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Cl1ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        print("Quasar-2:Установка режима 'Перезапуск импульсами':OK")
        return True
    except Exception as e:
        print("Quasar-2:Установка режима 'Перезапуск импульсами':ERROR")
        return False

async def ALS_status_AutoImp_blade():
    TEST_ID_KIWI = 1386
    try:
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Cl1ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        print("Quasar-2:Установка режима 'Перезапуск автоматический':OK")
        return True
    except Exception as e:
        print("Quasar-2:Установка режима 'Перезапуск автоматический':ERROR")
        return False
    
async def ALS_status_off_blade():
    TEST_ID_KIWI = 1386
    try:
        driver.find_element(By.ID, f"{config['dev_val_blade']}st_descr").click()
        driver.find_element(By.ID, f"{config['first_page_blade']}").click()
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Cl1ALSState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(15)
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
        test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
        print("Quasar-2:Установка режима 'Выкл.':OK")
        return True
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
        test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
        print("Quasar-2:Установка режима 'Выкл.':ERROR")
        return False

    #ВЫКЛЮЧЕНИЕ КЛИЕНТСКОЙ И АБОНЕНТСКИХ ЛИНИЙ

async def line_power_off_blade():
    TEST_ID_KIWI = 1387
    try:
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Cl1SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Cl1SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()

        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln2SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()

        driver.find_element(By.CSS_SELECTOR, f"#{config['dev_val_blade']}{config['Ln1SwitchState']} .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(2)
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
        test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
        print("Quasar-2:Выключение клиентской и основных линий:OK")
        return True
    except Exception as e:
        error_msg = f"Exception: {str(e)}"
        test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
        test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
        print("Quasar-2:Выключение клиентской и основных линий:ERROR")
        return False

    #ПЕРЕХОД НА ВКЛАДКУ ЖУРНАЛ ЧЕРЕЗ ССЫЛКУ В НАЗВАНИИ УСТРОЙСТВА
    
async def journal_check_blade():
        TEST_ID_KIWI = 1388
        driver.get(f"{config['quazar_IP_blade']}/slot-5/")
        await asyncio.sleep(5)
        wait = WebDriverWait(driver, 10)

        try:
            # Пример нахождения div по ID; замените 'your_div_id' на нужный ID
            div_element = wait.until(EC.visibility_of_element_located((By.ID, 'quasar_content')))
            
            # Извлекаем текст из найденного div
            div_text = div_element.text
            print("Текст из div:", div_text)
            with open(f"output-journal_{config['web_ip_blade']}.txt", 'w', encoding='utf-8') as file:
                file.write(div_text)  # Записываем текст в файл
                test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'PASSED')
                test_cfg.print_head_test("РЕЗУЛЬТАТ: ТЕСТ ПРОЙДЕН УСПЕШНО")
                driver.quit()
                return True 
        except Exception as e:
            error_msg = f"Exception: {str(e)}"
            test_cfg.update_kiwi(config['test_run_id'], TEST_ID_KIWI, 'ERROR', error_msg)
            test_cfg.add_comment_kiwi(config['test_run_id'], TEST_ID_KIWI, error_msg)
            print(f"Произошла ошибка: {e}")
            driver.quit() 
            return False




async def main():
    log_file2 = f"logging_{config['web_ip_blade']}.txt"
    if not os.path.exists(log_file2):
        with open(log_file2, "a") as f:
            f.write("Лог файл создан: " + str(datetime.now()) + "\n")
    with open(log_file2, "w") as f:
        original_stdout = sys.stdout  # Сохраняем оригинальный stdout
        sys.stdout = f  # Перенаправляем вывод на файл
        await initialization_blade()
        await tab_scan_blade()
        await line_power_on_blade()
        await ALS_mode_change_blade()
        await FEC_mode_EFEC_blade()
        await FEC_mode_G709_blade()
        await FEC_mode_off_blade()
        await FEC_mode_G709_rep_blade()
        await ALS_status_ImpAuto_blade()
        await ALS_status_AutoImp_blade()
        await ALS_status_off_blade()
        await line_power_off_blade()
        await journal_check_blade()
        
if __name__ == "__main__":
    asyncio.run(main())
