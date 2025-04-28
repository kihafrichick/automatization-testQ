
import asyncio
import sys
from perl_start_script import test_analyzer 
import streamlit as st
import sborka_sinhron
import sborka_sinhron_blades
from datetime import datetime
import logging


# logging.basicConfig(level=logging.DEBUG)
sys.stdout = open('logging_test.txt','w')

def print_with_timestamp(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

async def run_function(func):
    try:
        #print(f"Запуск функции: {func.__name__}")
        await func()
    except Exception as e:
        print_with_timestamp(f"Ошибка в {func.__name__}: {e}")

async def run_function_group(func_pair):
    tasks = []
    for func in func_pair:
        #print(f"Создание задачи для функции: {func.__name__}")
        task = asyncio.create_task(run_function(func))
        tasks.append(task)

    await asyncio.gather(*tasks) 

async def main():
    function_group = [
        (sborka_sinhron.int_code1, sborka_sinhron_blades.int_code2),
        (sborka_sinhron.function_1, sborka_sinhron_blades.function_12),
        (sborka_sinhron.function_2, sborka_sinhron_blades.function_13),
        (sborka_sinhron.function_3, sborka_sinhron_blades.function_14),
        (sborka_sinhron.function_4, sborka_sinhron_blades.function_15),
        (sborka_sinhron.function_5, sborka_sinhron_blades.function_16),
        (sborka_sinhron.function_6, sborka_sinhron_blades.function_17),
        (sborka_sinhron.function_7, sborka_sinhron_blades.function_18),
        (sborka_sinhron.function_8, sborka_sinhron_blades.function_19),
        (sborka_sinhron.function_9, sborka_sinhron_blades.function_20),
        (sborka_sinhron.function_10, sborka_sinhron_blades.function_21),
        (sborka_sinhron.function_11, sborka_sinhron_blades.function_22),
    ]

    CHECKPOINTS = {2,3,4,5,6,7,8,9}
    
    for i, func_pair in enumerate(function_group):
        #print(f"Запуск группы {i + 1}: {func_pair}")
        await run_function_group(func_pair) 
        
        if i in CHECKPOINTS:  # Проверяем только в контрольных точках
            await asyncio.sleep(7) # Пауза для подгрузки соединения
            status = test_analyzer()  # Простой синхронный вызов
            print_with_timestamp(f"Проверка анализатора: {status}")

        if i < len(function_group) - 1:
            print_with_timestamp("Группа завершила работу, ожидание 10 секунд перед запуском следующей группы...")
            await asyncio.sleep(10)

    print_with_timestamp("Все группы завершили свою работу.")

if __name__ == "__main__":
    asyncio.run(main())

sys.stdout.close()
sys.stdout = sys.__stdout__