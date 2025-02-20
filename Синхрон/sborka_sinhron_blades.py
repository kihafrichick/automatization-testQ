
import time
import logging
import asyncio
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
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
    # 1 | open | /monitor/monclassic.html?bts=2023-11-09-16_13_32&debug=true | 
    driver.get("http://192.168.17.223/monitor/monclassic.html?bts=2023-11-09-16_13_32&debug=true")
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
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(8) > .ui-dialog-buttonpane .ui-button").click()
    await asyncio.sleep(3)

            #СКАНИРОВАНИЕ ИНФОРМАЦИИ ИЗ ТАБЛИЦЫ ГЛАВНОЙ СТРАНИЦЫ

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
int_code2()
    
        #ВКЛЮЧЕНИЕ КЛИЕНТСКОЙ И АБОНЕНТСКИХ ЛИНИЙ
async def function_12():
    # 3 | click | id=dev6stadmstate | 
    driver.find_element(By.ID, "dev6st_descr").click()
    # 4 | click | id=ui-id-45 | 
    driver.find_element(By.ID, "ui-id-37").click()
    # 5 | click | css=#dev6_Ln1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1PortState .on-click-edit").click()
    # 7 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 8 | mouseDownAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 9 | mouseMoveAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 10 | mouseUpAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 11 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 12 | click | css=#dev6_Ln2PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2PortState .on-click-edit").click()
    # 13 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 14 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 15 | mouseDownAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 16 | mouseMoveAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 17 | mouseUpAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 18 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 19 | click | css=#dev6_Ln1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1PortState .on-click-edit").click()
    # 20 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 21 | select | id=param_select_value | label=IS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
    # 22 | mouseDownAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 23 | mouseMoveAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 24 | mouseUpAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 25 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 26 | click | css=#dev6_Ln2PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2PortState .on-click-edit").click()
    # 27 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
    # 29 | mouseDownAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 30 | mouseMoveAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 31 | mouseUpAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 32 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 33 | click | css=#dev6_Cl1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1PortState .on-click-edit").click()
    # 34 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 35 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 36 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 37 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 38 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 39 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 40 | click | css=#dev6_Cl1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1PortState .on-click-edit").click()
    # 41 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 42 | click | css=#edit_param_dialog .form-unit:nth-child(4) | 
    driver.find_element(By.CSS_SELECTOR, "#edit_param_dialog .form-unit:nth-child(4)").click()
    # 43 | select | id=param_select_value | label=IS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'IS']").click()
    # 44 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 45 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 46 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 47 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
function_12()
        #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ FEC

async def function_13():
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1FECSet .on-click-edit").click()
    # 49 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 50 | select | id=param_select_value | label=EFEC
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
    # 51 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 52 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 53 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 54 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 55 | click | css=#dev6_Ln2FECSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2FECSet .on-click-edit").click()
    # 56 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 59 | select | id=param_select_value | label=EFEC
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'EFEC']").click()
    # 60 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 61 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 62 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 63 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 64 | click | css=#dev6_Ln1FECSet .on-click-edit | 
    await asyncio.sleep(3)
function_13()
   
async def function_14():
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1FECSet .on-click-edit").click()
    # 65 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 66 | select | id=param_select_value | label=G.709
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
    # 67 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 68 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 69 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 70 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 71 | click | css=#dev6_Ln2FECSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2FECSet .on-click-edit").click()
    # 72 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 73 | select | id=param_select_value | label=G.709
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
    # 74 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 75 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 76 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 77 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 78 | click | css=#dev6_Ln1FECSet .on-click-edit | 
    await asyncio.sleep(3)
function_14()
    
async def function_15():
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1FECSet .on-click-edit").click()
    # 79 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 

    # 80 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 81 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 82 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 83 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 84 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 85 | click | css=#dev6_Ln2FECSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2FECSet .on-click-edit").click()
    # 86 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
   
    # 87 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 88 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 89 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 90 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 91 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 92 | click | css=#dev6_Ln1FECSet .on-click-edit | 
    await asyncio.sleep(3)
function_15()
    
async def function_16():    
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1FECSet .on-click-edit").click()
    # 93 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 94 | select | id=param_select_value | label=G.709
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
    # 95 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 96 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 97 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 98 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 99 | click | css=#dev6_Ln2FECSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2FECSet .on-click-edit").click()
    # 100 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 101 | select | id=param_select_value | label=G.709
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'G.709']").click()
    # 102 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 103 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 104 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(5)
function_16()


    #ПЕРЕКЛЮЧЕНИЕ РЕЖИМОВ/СТАТУСОВ ALS 
async def function_17():   
    # 106 | click | css=#dev6_Ln1TxEnable .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1TxEnable .on-click-edit").click()
    # 107 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 108 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 109 | click | css=#dev6_Ln2TxEnable .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2TxEnable .on-click-edit").click()
    # 110 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 111 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 112 | click | css=#dev6_Cl1TxEnable .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1TxEnable .on-click-edit").click()
    # 113 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 114 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 115 | click | css=#dev6_Ln1ALSSet .on-click-edit | 
    await asyncio.sleep(10)
function_17()

async def function_18():
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1ALSSet .on-click-edit").click()
    # 116 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 

    # 117 | select | id=param_select_value | label=Перезапуск импульсами
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
    # 118 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 119 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 120 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 121 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 122 | click | css=#dev6_Ln2ALSSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2ALSSet .on-click-edit").click()
    # 123 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 124 | select | id=param_select_value | label=Перезапуск импульсами
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
    # 125 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 126 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 127 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 128 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 129 | click | css=#dev6_Cl1ALSSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1ALSSet .on-click-edit").click()
    # 130 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 131 | select | id=param_select_value | label=Перезапуск импульсами
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск импульсами']").click()
    # 132 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 133 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 134 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 135 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 136 | click | css=#dev6_Ln1ALSSet .on-click-edit | 
    await asyncio.sleep(10)
function_18()

async def function_19():
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1ALSSet .on-click-edit").click()
    # 137 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 138 | select | id=param_select_value | label=Перезапуск автоматический
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
    # 139 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 140 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 141 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 142 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 143 | click | css=#dev6_Ln2ALSSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2ALSSet .on-click-edit").click()
    # 144 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 145 | select | id=param_select_value | label=Перезапуск автоматический
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
    # 146 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 147 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 148 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 149 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 150 | click | css=#dev6_Cl1ALSSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1ALSSet .on-click-edit").click()
    # 151 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    # 152 | select | id=param_select_value | label=Перезапуск автоматический
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Перезапуск автоматический']").click()
    # 153 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 154 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 155 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 156 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 157 | click | css=#dev6_Ln2ALSSet .on-click-edit | 
    await asyncio.sleep(10)
function_19()
    
async def function_20():
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2ALSSet .on-click-edit").click()
    # 158 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 159 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 160 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 161 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 162 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 163 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 164 | click | css=#dev6_Ln1ALSSet .on-click-edit | 
    await asyncio.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1ALSSet .on-click-edit").click()
    # 165 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 166 | select | id=param_select_value | label=Выкл
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'Выкл']").click()
    # 167 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 168 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 169 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 170 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 171 | click | css=#dev6_Ln1PortState .on-click-edit | 
    await asyncio.sleep(3)
function_20()


#ВЫКЛЮЧЕНИЕ КЛИЕНТСКОЙ И АБОНЕНТСКИХ ЛИНИЙ
async def function_21():
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1PortState .on-click-edit").click()
    # 172 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 173 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 174 | mouseDownAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 175 | mouseMoveAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 176 | mouseUpAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 177 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 178 | click | css=#dev6_Ln2PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2PortState .on-click-edit").click()
    # 179 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 180 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 181 | mouseDownAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 182 | mouseMoveAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 183 | mouseUpAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 184 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 185 | click | css=#dev6_Cl1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1PortState .on-click-edit").click()
    # 186 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 187 | select | id=param_select_value | label=OOS-MT
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS-MT']").click()
    # 188 | mouseDownAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 189 | mouseMoveAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 190 | mouseUpAt | id=param_select_value | -0.171875,-0.328125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 191 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 192 | click | css=#dev6_Cl1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Cl1PortState .on-click-edit").click()
    # 193 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 194 | select | id=param_select_value | label=OOS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
    # 195 | mouseDownAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 196 | mouseMoveAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 197 | mouseUpAt | id=param_select_value | -0.171875,-0.34375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 198 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 199 | click | css=#dev6_Ln2PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln2PortState .on-click-edit").click()
    # 200 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 201 | select | id=param_select_value | label=OOS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
    # 202 | mouseDownAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 203 | mouseMoveAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 204 | mouseUpAt | id=param_select_value | -0.171875,-0.828125
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 205 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    # 206 | click | css=#dev6_Ln1PortState .on-click-edit | 
    driver.find_element(By.CSS_SELECTOR, "#dev6_Ln1PortState .on-click-edit").click()
    # 207 | click | css=.ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    
    # 208 | select | id=param_select_value | label=OOS
    dropdown = driver.find_element(By.ID, "param_select_value")
    dropdown.find_element(By.XPATH, "//option[. = 'OOS']").click()
    # 209 | mouseDownAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 210 | mouseMoveAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 211 | mouseUpAt | id=param_select_value | -0.171875,-0.84375
    element = driver.find_element(By.ID, "param_select_value")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 212 | click | css=.ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2) | 
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(15) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(18) > .ui-dialog-buttonpane .ui-button:nth-child(2)").click()
    await asyncio.sleep(3)
function_21()


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
#function_group = [function_12, function_13, function_14, function_15, function_16, function_17, function_18, function_19, function_20, function_21, function_22]    
function_22()

async def main():
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
    
    
if __name__ == "__main__":
    asyncio.run(main())

