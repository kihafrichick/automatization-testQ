import os
import sys
import logging
import asyncio
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



#logging.basicConfig(level=logging.DEBUG)
                    #   filename='output.log',          # Имя файла для логов
                    #   ,            # Уровень логирования
                    #   format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
                    #   datefmt='%Y-%m-%d %H:%M:%S'     # Формат даты и времени

options = webdriver.ChromeOptions()
service = Service('/usr/bin/chromedriver' , log_path='/tmp/chromedriver.log')  # Путь к chromedriver
options.binary_location =  '/usr/bin/chromium-gost'  # Путь к браузеру Chrome
driver = webdriver.Chrome(service=service, options=options)
path_number_1 = 14
path_number_2 = 17
    #ПЕРЕХОД НА WEB-ИНТЕРФЕЙС
  
async def function_1():
    try:
        driver.get("http://192.168.17.227")
        driver.set_window_size(1854, 1011)
        await asyncio.sleep(3)
        driver.find_element(By.ID, "login").send_keys("Admin")
        await asyncio.sleep(3)
        driver.find_element(By.ID, "password").click()
        await asyncio.sleep(3)
        driver.find_element(By.ID, "password").send_keys("cradmin")
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(7) > .ui-dialog-buttonpane .ui-button").click()
        await asyncio.sleep(3)
        print("Quasar-1:Переход на страницу и авторизация:ОК")
        return True
    except Exception as e:
        print("Quasar-1:Переход на страницу и авторизация:ERROR")
        return False

            
        #СКАНИРОВАНИЕ ИНФОРМАЦИИ ИЗ ТАБЛИЦЫ ГЛАВНОЙ СТРАНИЦЫ
async def function_2():
    try:
        wait = WebDriverWait(driver, 20)
        table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.selected-cu-params.standard.even_odd')))

        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')  
            print([cell.text.strip() for cell in cells])  # Print content of the cells
        with open('info_227.txt', 'w', encoding='utf-8') as file:
            # Записываем содержимое таблицы в файл
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                # Получаем текст всех ячеек в строке
                row_data = [cell.text.strip() for cell in cells]
                # Записываем строку в файл (элементы разделены табуляцией или пробелами)
                file.write('\t'.join(row_data) + '\n')
        print("Quasar-1:Сканирование информации:OK")
        return True
    except Exception as e:
        print("Quasar-1:Сканирование информации:ERROR")
        return False
  
        
    #ВКЛЮЧЕНИЕ КЛИЕНТСКОЙ И ОСНОВНЫХ ЛИНИЙ
        
async def function_3():
    try:    
        driver.find_element(By.ID, "dev1stadmstate").click()
        await asyncio.sleep(1)
        driver.find_element(By.ID, "ui-id-24").click()
        await asyncio.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform() 
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.execute_script("window.scrollTo(0,0)")
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-1:Включение клиентской и основных линий:OK")
        return True
    except Exception as e:
        print("Quasar-1:Включение клиентской и основных линий:ERROR")
        return False

    #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ ALS 
    
async def function_4():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1TxEnable .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.ID, "dev1st___cls").click() 
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2TxEnable .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1TxEnable .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        print("Quasar-1:Включение режима 'Управляется ALS':OK")
        return True
    except Exception as e:
        print("Quasar-1:Включение режима 'Управляется ALS':ERROR")
        return False 

    #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ FEC

async def function_5():
    try:
        driver.find_element(By.ID, "dev1stadmstate").click()
        driver.find_element(By.ID, "ui-id-24").click()
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-1:Установка режима 'FEC':OK")
        return True
    except Exception as e:
        print("Quasar-1:Установка режима 'FEC':ERROR")
        return False



    
async def function_6():  
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-1:Установка режима 'G.709':OK")
        return True
    except Exception as e:
        print("Quasar-1:Установка режима 'G.709':ERROR")
        return False
        
    

    
async def function_7():
    try:   
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-1:Установка режима 'Выкл.':OK")
        return True
    except Exception as e:
        print("Quasar-1:Установка режима 'Выкл.':ERROR")
        return False
    

    
async def function_8():
    try:
        driver.find_element(By.ID, "dev1st___cls").click()
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(5)
        print("Quasar-1:Установка режима 'G.709':OK")
        return True
    except Exception as e:
        print("Quasar-1:Установка режима 'G.709':ERROR")
        return False



    #ПЕРЕКЛЮЧЕНИЕ СТАТУСОВ ALS 

async def function_9():
    try:
        driver.find_element(By.ID, "dev1stadmstate").click()
        driver.find_element(By.ID, "ui-id-24").click()
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).click_and_hold().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        print("Quasar-1:Установка режима 'Перезапуск автоматический':OK")
        return True
    except Exception as e:
        print("Quasar-1:Установка режима 'Перезапуск автоматический':ERROR")
        return False


async def function_10():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
         
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).click_and_hold().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        print("Quasar-1:Установка режима 'Перезапуск импульсами':OK")
        return True
    except Exception as e:
        print("Quasar-1:Установка режима 'Перезапуск импульсами':ERROR")
        return False

    

async def function_11():
    try: 
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).click_and_hold().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(15)
        print("Quasar-1:Установка режима 'Выкл.':OK")
        return True
    except Exception as e:
        print("Quasar-1:Установка режима 'Выкл.':ERROR")
        return False
    
    #ВЫКЛЮЧЕНИЕ КЛИЕНТСКОЙ И АБОНЕНТСКИХ ЛИНИЙ
    
async def function_12():
    try:
        driver.find_element(By.ID, "dev1stadmstate").click()
        driver.find_element(By.ID, "ui-id-24").click()
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
      
        driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_1}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, f".ui-dialog:nth-child({path_number_2}) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-1:Выключение клиентской и основных линий:OK")
        return True
    except Exception as e:
        print("Quasar-1:Выключение клиентской и основных линий:ERROR")
        return False

    #ПЕРЕХОД НА ВКЛАДКУ ЖУРНАЛ ЧЕРЕЗ ССЫЛКУ В НАЗВАНИИ УСТРОЙСТВА
    
async def function_13():  
    driver.get('http://192.168.17.227/slot-1/')
    await asyncio.sleep(5)
    wait = WebDriverWait(driver, 10)
    try:
        # Пример нахождения div по ID; замените 'your_div_id' на нужный ID
        div_element = wait.until(EC.visibility_of_element_located((By.ID, 'quasar_content')))
        
        # Извлекаем текст из найденного div
        div_text = div_element.text
        print("Текст из div:", div_text)
        with open('output-journal_227.txt', 'w', encoding='utf-8') as file:
            file.write(div_text)  # Записываем текст в файл
            return True
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False
        
async def main():
    log_file1 = "logging_227.txt"
    if not os.path.exists(log_file1):
        with open(log_file1, "a") as f:
            f.write("Лог файл создан: " + str(datetime.now()) + "\n")

        # Открываем файл и перенаправляем вывод
    with open(log_file1, "w") as f:
        original_stdout = sys.stdout  # Сохраняем оригинальный stdout
        sys.stdout = f  # Перенаправляем вывод на файл
        await function_1()
        await function_2()
        await function_3()
        await function_4()
        await function_5()
        await function_6()
        await function_7()
        await function_8()
        await function_9()
        await function_10()
        await function_11()
        await function_12()
        await function_13()
        
        sys.stdout = original_stdout

if __name__ == "__main__":
    asyncio.run(main())