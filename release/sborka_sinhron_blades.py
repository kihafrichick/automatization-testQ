import os
import sys
import logging
import asyncio
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
service = Service('/usr/bin/chromedriver' , log_path='/tmp/chromedriver.log')  # Путь к chromedriver
options.binary_location =  '/usr/bin/chromium-browser'  # Путь к браузеру Chrome
driver = webdriver.Chrome(service=service, options=options)

    #ПЕРЕХОД НА WEB-ИНТЕРФЕЙС


async def int_code2():
    try:
        driver.get("http://192.168.17.223/monitor/monclassic.html?bts=2025-01-19-21_25_17")
        driver.set_window_size(1857, 1028)
        await asyncio.sleep(3)
        driver.find_element(By.ID, "login").send_keys("Admin")
        await asyncio.sleep(3)
        driver.find_element(By.ID, "password").click()
        await asyncio.sleep(3)
        driver.find_element(By.ID, "password").send_keys("cradmin")
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(8) > .ui-dialog-buttonpane .ui-button").click()
        await asyncio.sleep(3)
        print("Quasar-2:Переход на страницу и авторизация:OK")
    except Exception as e:
        print('Quasar-2:Переход на страницу и авторизация:ERROR')
        
        #СКАНИРОВАНИЕ ИНФОРМАЦИИ ИЗ ТАБЛИЦЫ ГЛАВНОЙ СТРАНИЦЫ

    try:
        wait = WebDriverWait(driver, 20)
        table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.selected-cu-params.standard.even_odd')))
        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')  
            print([cell.text.strip() for cell in cells])  # Print content of the cells
        with open('info_223.txt', 'w', encoding='utf-8') as file:
            # Записываем содержимое таблицы в файл
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                # Получаем текст всех ячеек в строке
                row_data = [cell.text.strip() for cell in cells]
                # Записываем строку в файл (элементы разделены табуляцией или пробелами)
                file.write('\t'.join(row_data) + '\n')
        print("Quasar-2:Сканирование информации:OK")
    except Exception as e:
        print("Quasar-2:Сканирование информации:ERROR")
    
    #ВКЛЮЧЕНИЕ КЛИЕНТСКОЙ И ОСНОВНЫХ ЛИНИЙ
        
async def function_12():
    try:
        driver.find_element(By.ID, "dev6st_descr").click()
        driver.find_element(By.ID, "ui-id-33").click()
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2PortState .on-click-edit").click()        
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1PortState .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, "#edit_param_dialog .form-unit:nth-child(4)").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-2:Включение клиентской и основных линий:OK")
    except Exception as e:
        print("Quasar-2:Включение клиентской и основных линий:ERROR")

    #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ FEC

async def function_13():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-2:Установка режима 'FEC':OK")
    except Exception as e:
        print("Quasar-2:Установка режима 'FEC':ERROR")

async def function_14():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-2:Установка режима 'G.709':OK")
    except Exception as e:
        print("Quasar-2:Установка режима 'G.709':ERROR")
    
async def function_15():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-2:Установка режима 'Выкл.':OK")
    except Exception as e:
        print("Quasar-2:Установка режима 'Выкл.':ERROR")
    
async def function_16():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2FECSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(5)
        print("Quasar-2:Установка режима 'G.709':OK")
    except Exception as e:
        print("Quasar-2:Установка режима 'G.709':ERROR")


    #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ/СТАТУСОВ ALS 
async def function_17():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1TxEnable .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2TxEnable .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1TxEnable .on-click-edit").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        print("Quasar-2:Включение режима 'Управляется ALS':OK")
    except Exception as e:
        print("Quasar-2:Включение режима 'Управляется ALS':ERROR")


async def function_18():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        print("Quasar-2:Установка режима 'Перезапуск импульсами':OK")
    except Exception as e:
        print("Quasar-2:Установка режима 'Перезапуск импульсами':ERROR")

async def function_19():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(10)
        print("Quasar-2:Установка режима 'Перезапуск автоматический':OK")
    except Exception as e:
        print("Quasar-2:Установка режима 'Перезапуск автоматический':ERROR")
    
async def function_20():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1ALSSet .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-2:Установка режима 'Выкл.':OK")
    except Exception as e:
        print("Quasar-2:Установка режима 'Выкл.':ERROR")

    #ВЫКЛЮЧЕНИЕ КЛИЕНТСКОЙ И АБОНЕНТСКИХ ЛИНИЙ

async def function_21():
    try:
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        
        driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()

        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()

        driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1PortState .on-click-edit").click()
        dropdown = driver.find_element(By.ID, "param_select_value")
        dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
        element = driver.find_element(By.ID, "param_select_value")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        await asyncio.sleep(3)
        print("Quasar-2:Выключение клиентской и основных линий:OK")
    except Exception as e:
        print("Quasar-2:Выключение клиентской и основных линий:ERROR")

    #ПЕРЕХОД НА ВКЛАДКУ ЖУРНАЛ ЧЕРЕЗ ССЫЛКУ В НАЗВАНИИ УСТРОЙСТВА
    
async def function_22():
        driver.get('http://192.168.17.223/slot-6/')
        await asyncio.sleep(5)
        wait = WebDriverWait(driver, 10)

        try:
            # Пример нахождения div по ID; замените 'your_div_id' на нужный ID
            div_element = wait.until(EC.visibility_of_element_located((By.ID, 'quasar_content')))
            
            # Извлекаем текст из найденного div
            div_text = div_element.text
            print("Текст из div:", div_text)
            with open('output-journal_223.txt', 'w', encoding='utf-8') as file:
                file.write(div_text)  # Записываем текст в файл
                
        except Exception as e:
            print(f"Произошла ошибка: {e}")



async def main():
    log_file2 = "logging_223.txt"
    if not os.path.exists(log_file2):
        with open(log_file2, "a") as f:
            f.write("Лог файл создан: " + str(datetime.now()) + "\n")
    with open(log_file2, "w") as f:
        original_stdout = sys.stdout  # Сохраняем оригинальный stdout
        sys.stdout = f  # Перенаправляем вывод на файл
        await function_12(),
        await function_13(),
        await function_14(),
        await function_15(),
        await function_16(),
        await function_17(),
        await function_18(),
        await function_19(),
        await function_20(),
        await function_21(),
        await function_22()
    
        sys.stdout = original_stdout
        
if __name__ == "__main__":
    asyncio.run(main())
