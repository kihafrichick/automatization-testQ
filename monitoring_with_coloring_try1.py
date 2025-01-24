
import time
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.DEBUG)

options = webdriver.ChromeOptions()
service = Service('/usr/bin/chromedriver' , log_path='/tmp/chromedriver.log')  # Путь к chromedriver
options.binary_location =  '/usr/bin/chromium-browser'  # Путь к браузеру Chrome
driver = webdriver.Chrome(service=service, options=options)

# 1 | open | /monitor/monclassic.html?bts=2023-11-09-16_13_32&debug=true | 
driver.get("http://192.168.17.227/monitor/monclassic.html?bts=2024-09-27-09_50_40")
# 2 | setWindowSize | 1857x1028 | 
driver.set_window_size(1857 , 1028)
# 3 | type | id=login | Admin
time.sleep(3)
driver.find_element(By.ID, "login").send_keys("Admin")
# 4 | click | id=password | 
time.sleep(3)
driver.find_element(By.ID, "password").click()
# 5 | type | id=password | cradmin
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("cradmin")
# 6 | click | css=.ui-dialog:nth-child(8) > .ui-dialog-buttonpane .ui-button | 
driver.find_element(By.CSS_SELECTOR, ".ui-dialog:nth-child(8) > .ui-dialog-buttonpane .ui-button").click()
time.sleep(3)

# 3 | click | id=dev1stpid | 
driver.find_element(By.ID, "dev1stadmstate").click()
time.sleep(3)

# 4 | click | linkText=журнал | 
driver.find_element(By.LINK_TEXT, "журнал").click()
time.sleep(3)

# 5 | click | name=event_type | 
driver.find_element(By.NAME, "event_type").click()
time.sleep(3)

# 6 | click | css=p:nth-child(1) > .nobr:nth-child(2) > input | 
driver.find_element(By.CSS_SELECTOR, "p:nth-child(1) > .nobr:nth-child(2) > input").click()
# 7 | click | css=p:nth-child(1) > .nobr:nth-child(3) > input | 
driver.find_element(By.CSS_SELECTOR, "p:nth-child(1) > .nobr:nth-child(3) > input").click()
# 8 | click | css=p:nth-child(1) > .nobr:nth-child(4) > input | 
driver.find_element(By.CSS_SELECTOR, "p:nth-child(1) > .nobr:nth-child(4) > input").click()
# 9 | click | css=p:nth-child(1) > .nobr:nth-child(5) > input | 
driver.find_element(By.CSS_SELECTOR, "p:nth-child(1) > .nobr:nth-child(5) > input").click()
# 10 | click | css=.nobr:nth-child(6) > input | 
driver.find_element(By.CSS_SELECTOR, ".nobr:nth-child(6) > input").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".center > .ui-button").click()
time.sleep(3)
# 12 | click | css=.on-click-select:nth-child(1) > .wide | 
driver.find_element(By.CSS_SELECTOR, ".on-click-select:nth-child(1) > .wide").click()
time.sleep(3)
# 13 | click | name=event_type | 
driver.find_element(By.NAME, "event_type").click()
# 14 | click | css=.center > .ui-button | 

time.sleep(2)
def get_background_color(element):
    """ Получение цвета фона элемента. """
    return element.value_of_css_property('background-color')

def write_data_to_html(data, color):
        # Создаем файл, если он не существует
    if not os.path.exists("output.html"):
        # Если файл не существует, создаем его с заголовком
        with open('output1.html', 'w', encoding='utf-8') as file:
            file.write("""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Логи</title>
    <style>
        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
        }
        div {
            margin: 5px 0;
        }
    </style>
</head>
<body>\n""")

    # Добавляем данные в файл
    with open('output1.html', 'a', encoding='utf-8') as file:
        line = ' | '.join(data)
        file.write(f"<div style='color: {color};'>{line}</div>\n")

def close_html_file():
    # Закрываем HTML-теги, когда программа завершается
    with open('output1.html', 'a', encoding='utf-8') as file:
        file.write("</body>\n</html>")

# Хранение предыдущих данных для сравнения
previous_events = set()

# Цикл для отслеживания изменений
try:
    while True:
        event_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr[data-event]"))
        )

        for row in event_rows:
            data_event_value = row.get_attribute("data-event")

            if data_event_value not in previous_events:
                logging.debug(f"Новый лог: {data_event_value}")

                row_color = get_background_color(row)

                cell_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]

                write_data_to_html(cell_data, row_color)
                previous_events.add(data_event_value)

        time.sleep(1)

except KeyboardInterrupt:
    logging.info("Запись данных завершена.")

finally:
    driver.quit()