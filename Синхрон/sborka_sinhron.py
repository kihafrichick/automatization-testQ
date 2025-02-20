
import time
import logging
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
#import pytest
#import json
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.chrome.options import Options



logging.basicConfig(level=logging.DEBUG)
                    #   filename='output.log',          # Имя файла для логов
                    #   ,            # Уровень логирования
                    #   format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
                    #   datefmt='%Y-%m-%d %H:%M:%S'     # Формат даты и времени

options = webdriver.ChromeOptions()
service = Service('/usr/bin/chromedriver' , log_path='/tmp/chromedriver.log')  # Путь к chromedriver
options.binary_location =  '/usr/bin/chromium-browser'  # Путь к браузеру Chrome
driver = webdriver.Chrome(service=service, options=options)

    #ПЕРЕХОД НА WEB-ИНТЕРФЕЙС
async def int_code1():
    driver.get("http://192.168.17.227/monitor/monclassic.html?bts=2024-09-27-09_50_40")
        # 2 | setWindowSize | 1857x1028 | 
    driver.set_window_size(1857, 1028)
        # 3 | type | id=login | Admin
    await asyncio.sleep(3)
    driver.find_element(By.ID, "login").send_keys("Admin")
        # 4 | click | id=password | 
    await asyncio.sleep(3)
    driver.find_element(By.ID, "password").click()
        # 5 | type | id=password | cradmin
    await asyncio.sleep(3)
    driver.find_element(By.ID, "password").send_keys("cradmin")
        # 6 | click | css=.ui-dialog:nth-child(8) > .ui-dialog-buttonpane .ui-button | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(8) > .ui-dialog-buttonpane .ui-button").click()\
            
    await asyncio.sleep(3)
            
            #СКАНИРОВАНИЕ ИНФОРМАЦИИ ИЗ ТАБЛИЦЫ ГЛАВНОЙ СТРАНИЦЫ

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
int_code1()            
        #ВКЛЮЧЕНИЕ КЛИЕНТСКОЙ И АБОНЕНТСКИХ ЛИНИЙ
        
async def function_1():       
    driver.find_element(By.ID, "dev1stadmstate").click()
        # 4 | click | id=ui-id-24 | 
    await asyncio.sleep(2)
    driver.find_element(By.ID, "ui-id-24").click()
    await asyncio.sleep(2)
        # 5 | click | css=#dev1_Ln1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1PortState .on-click-edit").click()
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        # 7 | mouseDownAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 8 | mouseMoveAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 9 | mouseUpAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 10 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 11 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 12 | click | css=#dev1_Ln2PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2PortState .on-click-edit").click()
        # 13 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        # 14 | mouseDownAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 15 | mouseMoveAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 16 | mouseUpAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 17 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 18 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 19 | click | css=#dev1_Cl1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1PortState .on-click-edit").click()
        # 20 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
        # 21 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 22 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 23 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 24 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 25 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 26 | click | css=#dev1_Cl1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1PortState .on-click-edit").click()
        # 27 | select | id=param_select_value | label=IS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        # 28 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 29 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 30 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 31 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 32 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 33 | runScript | window.scrollTo(0,0) | 
    driver.execute_script("window.scrollTo(0,0)")
        # 34 | click | css=#dev1_Ln2PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2PortState .on-click-edit").click()
        # 35 | select | id=param_select_value | label=IS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
        # 36 | mouseDownAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 37 | mouseMoveAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 38 | mouseUpAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 39 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 40 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 41 | click | css=#dev1_Ln1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1PortState .on-click-edit").click()
        # 42 | select | id=param_select_value | label=IS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
    # 43 | mouseDownAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 44 | mouseMoveAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 45 | mouseUpAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 46 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 47 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
function_1()
    
  
        
        #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ FEC

async def function_2():  
    driver.find_element(By.ID, "dev1stadmstate").click()
        # 8 | click | id=ui-id-24 | 
    driver.find_element(By.ID, "ui-id-24").click()
        # 9 | click | css=#dev1_Ln1FECSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1FECSet .on-click-edit").click()
        # 10 | select | id=param_select_value | label=EFEC
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
        # 11 | mouseDownAt | id=param_select_value | -0.671875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 12 | mouseMoveAt | id=param_select_value | -0.671875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 13 | mouseUpAt | id=param_select_value | -0.671875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 14 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 15 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
        # 16 | click | css=#dev1_Ln2FECSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2FECSet .on-click-edit").click()
        # 17 | select | id=param_select_value | label=EFEC
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
        # 18 | mouseDownAt | id=param_select_value | -0.671875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 19 | mouseMoveAt | id=param_select_value | -0.671875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 20 | mouseUpAt | id=param_select_value | -0.671875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 21 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 22 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
function_2()   


    
async def function_3():  
        # 23 | click | css=#dev1_Ln1FECSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1FECSet .on-click-edit").click()
        # 24 | select | id=param_select_value | label=G.709
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        # 25 | mouseDownAt | id=param_select_value | -0.671875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 26 | mouseMoveAt | id=param_select_value | -0.671875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 27 | mouseUpAt | id=param_select_value | -0.671875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 28 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 29 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
        # 30 | click | css=#dev1_Ln2FECSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2FECSet .on-click-edit").click()
        # 31 | select | id=param_select_value | label=G.709
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
        # 32 | mouseDownAt | id=param_select_value | -0.671875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
        # 33 | mouseMoveAt | id=param_select_value | -0.671875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
        # 34 | mouseUpAt | id=param_select_value | -0.671875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
        # 35 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 36 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
function_3()   
    

    
async def function_4():      
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1FECSet .on-click-edit").click()
    # 6 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 7 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 8 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 9 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 10 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 11 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 12 | click | css=#dev1_Ln2FECSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2FECSet .on-click-edit").click()
    # 13 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 14 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 15 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 16 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 17 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 18 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
function_4()    
    
   
    
async def function_5():  
    # 19 | click | id=dev1st___cls | 
    driver.find_element(By.ID, "dev1st___cls").click()
    # 20 | click | css=#dev1_Ln1FECSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1FECSet .on-click-edit").click()
    # 21 | select | id=param_select_value | label=G.709
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
    # 22 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 23 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 24 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 25 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 26 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 27 | click | css=#dev1_Ln2FECSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2FECSet .on-click-edit").click()
    # 28 | select | id=param_select_value | label=G.709
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
    # 29 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 30 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 31 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 32 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 33 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(5)
function_5()
    
  
    
async def function_6():  
    #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ/СТАТУСОВ ALS 
        
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1TxEnable .on-click-edit").click()
        # 6 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 7 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 8 | click | id=dev1st___cls | 
    driver.find_element(By.ID, "dev1st___cls").click()
        # 9 | click | css=#dev1_Ln2TxEnable .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2TxEnable .on-click-edit").click()
        # 10 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
        # 11 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1TxEnable .on-click-edit").click()
    # 6 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 7 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 8 | click | css=#dev1_Cl1TxEnable .on-click-edit | 

    await asyncio.sleep(10)
function_6() 



async def function_7():  
    driver.find_element(By.ID, "dev1stadmstate").click()
    # 4 | click | id=ui-id-24 | 
    driver.find_element(By.ID, "ui-id-24").click()
    # 5 | click | css=#dev1_Ln1ALSSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1ALSSet .on-click-edit").click()
    # 6 | select | id=param_select_value | label=Перезапуск автоматический
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
    # 7 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 8 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 9 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 10 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 11 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 12 | click | css=#dev1_Ln2ALSSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2ALSSet .on-click-edit").click()
    # 27 | select | id=param_select_value | label=Перезапуск автоматический
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
    # 28 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 29 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 30 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 31 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 32 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1ALSSet .on-click-edit").click()
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
    # 7 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 8 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 9 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 10 | click | css=#dev1_Cl1ALSSet .on-click-edit | 
    await asyncio.sleep(10)
function_7()




async def function_8():  
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2ALSSet .on-click-edit").click()
    # 13 | select | id=param_select_value | label=Перезапуск импульсами
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
    # 14 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 17 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 18 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
    # 19 | click | css=#dev1_Ln1ALSSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1ALSSet .on-click-edit").click()
    # 20 | select | id=param_select_value | label=Перезапуск импульсами
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 23 | mouseUpAt | id=param_select_value | -0.1875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 24 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 25 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 26 | click | css=#dev1_Ln2ALSSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1ALSSet .on-click-edit").click()
    # 11 | select | id=param_select_value | label=Перезапуск импульсами
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
    # 12 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 13 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 14 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 15 | click | css=#dev1_Cl1ALSSet .on-click-edit | 
    await asyncio.sleep(10)
function_8() 
    

async def function_9():  
    # 33 | click | css=#dev1_Ln1ALSSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1ALSSet .on-click-edit").click()
    # 34 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 35 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 36 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 37 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 38 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 39 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 40 | click | css=#dev1_Ln2ALSSet .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2ALSSet .on-click-edit").click()
    # 41 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 42 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 43 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 44 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 45 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 46 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 47 | click | css=.ui-dialog:nth-child(15) .ui-button:nth-child(1) | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1ALSSet .on-click-edit").click()
    # 16 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 17 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 18 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 21 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()

    await asyncio.sleep(15)
function_9()
    
    #ВЫКЛЮЧЕНИЕ КЛИЕНТСКОЙ И АБОНЕНТСКИХ ЛИНИЙ
async def function_10():
    driver.find_element(By.ID, "dev1stadmstate").click()
    # 4 | click | id=ui-id-24 | 
    driver.find_element(By.ID, "ui-id-24").click()
    # 5 | click | css=#dev1_Ln1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1PortState .on-click-edit").click()
    # 6 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 7 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 8 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 9 | click | css=#dev1_Ln2PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2PortState .on-click-edit").click()
    # 10 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 11 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 12 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 13 | click | css=#dev1_Ln1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln1PortState .on-click-edit").click()
    # 14 | select | id=param_select_value | label=OOS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
    # 15 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 16 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 17 | click | css=#dev1_Ln2PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Ln2PortState .on-click-edit").click()
    # 18 | select | id=param_select_value | label=OOS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
    # 19 | mouseDownAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 20 | mouseMoveAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 21 | mouseUpAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 22 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 23 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 24 | click | css=#dev1_Cl1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1PortState .on-click-edit").click()
    # 25 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 26 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 27 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 28 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 29 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 30 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 31 | click | css=#dev1_Cl1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev1_Cl1PortState .on-click-edit").click()
    # 32 | select | id=param_select_value | label=OOS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
    # 33 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 34 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 35 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 36 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 37 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
function_10()
    
async def function_11():  
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
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
function_11()
#function_group = [function_1, function_2, function_3, function_4, function_5, function_6, function_7, function_8, function_9, function_10, function_11]
async def main():
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
    

if __name__ == "__main__":
    asyncio.run(main())


