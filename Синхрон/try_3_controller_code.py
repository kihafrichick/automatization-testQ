# import time
# import logging
# from queue import Queue

# #logging.basicConfig(level=logging.DEBUG)

# # Определяем классы задач
# class FunctionTask:
#     def __init__(self, func, pause=0):
#         self.func = func
#         self.pause = pause

#     def run(self):
#         try:
#             logging.debug(f"Запуск функции: {self.func.__name__}")
#             self.func()
#         except Exception as e:
#             logging.error(f"Ошибка в {self.func.__name__}: {e}")
#         finally:
#             if self.pause > 0:
#                 logging.info(f"Пауза на {self.pause} секунд после {self.func.__name__}...")
#                 time.sleep(self.pause)

# # Импортируем ваши модули
# import sborka_sinhron
# import sborka_sinhron_blades

# if __name__ == "__main__":
#     # Создаем очередь
#     task_queue = Queue()

#     # Заполняем очередь функциями, которые нужно выполнять
#     task_queue.put(FunctionTask(sborka_sinhron.int_code1, 1))  # Пример с паузой
#     task_queue.put(FunctionTask(sborka_sinhron_blades.int_code2, 5))
    
#     # Основные функции
#     task_queue.put(FunctionTask(sborka_sinhron.function_1, 1))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_12, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_2, 1))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_13, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_3, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_14, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_4, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_15, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_5, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_16, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_6, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_17, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_7, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_18, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_8, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_19, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_9, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_20, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_10, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_21, 2))
#     task_queue.put(FunctionTask(sborka_sinhron.function_11, 2))
#     task_queue.put(FunctionTask(sborka_sinhron_blades.function_22, 2))

#     # Запуск задач из очереди
#     while not task_queue.empty():
#         task = task_queue.get()
#         task.run()
    
#     logging.info("Все задачи завершены.")



# import multiprocessing
# import time
# import logging
# import importlib


# logging.basicConfig(level=logging.DEBUG)

# def run_function(func):
#     try:
#         func()
#     except Exception as e:
#         print(f"Ошибка в {func.__name__}: {e}")
        
# def run_function_group(func_pair):
#     processes = []
#     for func in func_pair:
#         print(f"Создание процесса для функции: {func.__name__}")
#         process = multiprocessing.Process(target=run_function, args=(func,))
#         processes.append(process)
#         process.start()
    
        
#     for process in processes:
#         process.join() 
        
# if __name__ == "__main__":
#     sborka_sinhron = importlib.import_module('sborka_sinhron')
#     sborka_sinhron_blades = importlib.import_module('sborka_sinhron_blades')
    
#     function_group = [
#         (sborka_sinhron.int_code1, sborka_sinhron_blades.int_code2)
#         (sborka_sinhron.function_1, sborka_sinhron_blades.function_12),   
#         (sborka_sinhron.function_2, sborka_sinhron_blades.function_13),
#         (sborka_sinhron.function_3, sborka_sinhron_blades.function_14),
#         (sborka_sinhron.function_4, sborka_sinhron_blades.function_15),
#         (sborka_sinhron.function_5, sborka_sinhron_blades.function_16),
#         (sborka_sinhron.function_6, sborka_sinhron_blades.function_17),
#         (sborka_sinhron.function_7, sborka_sinhron_blades.function_18),
#         (sborka_sinhron.function_8, sborka_sinhron_blades.function_19),
#         (sborka_sinhron.function_9, sborka_sinhron_blades.function_20),
#         (sborka_sinhron.function_10, sborka_sinhron_blades.function_21),
#         (sborka_sinhron.function_11, sborka_sinhron_blades.function_22),
#     ]
   
#     for i, func_pair in enumerate(function_group):
#         print(f"Запуск группы {i + 1}: {func_pair}")
#         run_function_group(func_pair)  # Запуск группы функций
        
#         if i < len(function_group) - 1:
#             print("Группа запущена, ожидание 15 секунд перед запуском следующей группы...")
#             time.sleep(15)  # если необходимо, можно оставить эту задержку
    

#     print("Все группы завершили свою работу.")










# import multiprocessing
# import time
# from sborka_sinhron import function_1 as f1_1, function_2 as f1_2
# from sborka_sinhron_blades import function_12 as f2_12, function_13 as f2_13
# import logging
# import sys
# print(sys.path)  # Проверьте, что текущий каталог присутствует в этом списке


# logging.basicConfig(level=logging.DEBUG)

# def run_functions(pair):
#     f1, f2 = pair
#     process1 = multiprocessing.Process(target=f1)
#     process2 = multiprocessing.Process(target=f2)
    
#     process1.start()
#     process2.start()
    
#     process1.join()
#     process2.join()

# if __name__ == "__main__":
#     # Создаем пары функций для запуска
#     function_pairs = [
#         (f1_1, f1_2),  # Первая пара
#         (f2_12, f2_13),  # Вторая пара
#         # Добавьте другие пары по необходимости
#     ]
   
#     for i, pair in enumerate(function_pairs):
#         print(f"Запуск пары {i + 1}: {pair[0].__name__} и {pair[1].__name__}")
#         run_functions(pair)  # Запуск пары функций

#         if i < len(function_pairs) - 1:
#             print("Задержка перед запуском следующей пары...")
#             time.sleep(10)  # Задержка между парами, здесь 10 секунд

#     print("Все пары завершили свою работу.")





# import threading
# import time
# import sborka_sinhron 
# import sborka_sinhron_blades 
# import logging

# logging.basicConfig(level=logging.DEBUG)

# def run_function(func):
#     try:
#         print(f"Запуск функции: {func.__name__}")
#         func()  # Выполняем функцию
#     except Exception as e:
#         print(f"Ошибка в {func.__name__}: {e}")

# def run_function_group(func_pair):
#     threads = []
#     for func in func_pair:
#         print(f"Создание потока для функции: {func.__name__}")
#         thread = threading.Thread(target=run_function, args=(func,)) 
#         threads.append(thread)
#         thread.start()
    
#     for thread in threads:
#         thread.join()  # Ждем завершения потока

# if __name__ == "__main__":
#     function_group = [
#         (sborka_sinhron.int_code1, sborka_sinhron_blades.int_code2)
#         (sborka_sinhron.function_1, sborka_sinhron_blades.function_12),   
#         (sborka_sinhron.function_2, sborka_sinhron_blades.function_13),
#         (sborka_sinhron.function_3, sborka_sinhron_blades.function_14),
#         (sborka_sinhron.function_4, sborka_sinhron_blades.function_15),
#         (sborka_sinhron.function_5, sborka_sinhron_blades.function_16),
#         (sborka_sinhron.function_6, sborka_sinhron_blades.function_17),
#         (sborka_sinhron.function_7, sborka_sinhron_blades.function_18),
#         (sborka_sinhron.function_8, sborka_sinhron_blades.function_19),
#         (sborka_sinhron.function_9, sborka_sinhron_blades.function_20),
#         (sborka_sinhron.function_10, sborka_sinhron_blades.function_21),
#         (sborka_sinhron.function_11, sborka_sinhron_blades.function_22),
#     ]

#     for i, func_pair in enumerate(function_group):
#         print(f"Запуск группы {i + 1}: {func_pair}")
#         run_function_group(func_pair)  # Здесь выполняем обе функции в группе
        
#         if i < len(function_group) - 1:
#             print("Группа завершила работу, ожидание 15 секунд перед запуском следующей группы...")
#             time.sleep(15)

#     print("Все группы завершили свою работу.")



import asyncio
import time
import sborka_sinhron
import sborka_sinhron_blades
import logging

#logging.basicConfig(level=logging.DEBUG)

async def run_function(func):
    try:
        print(f"Запуск функции: {func.__name__}")
        await func()  # Выполняем функцию
    except Exception as e:
        print(f"Ошибка в {func.__name__}: {e}")

async def run_function_group(func_pair):
    tasks = []
    for func in func_pair:
        print(f"Создание задачи для функции: {func.__name__}")
        task = asyncio.create_task(run_function(func))
        tasks.append(task)

    await asyncio.gather(*tasks)  # Ждем завершения всех задач

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

    for i, func_pair in enumerate(function_group):
        print(f"Запуск группы {i + 1}: {func_pair}")
        await run_function_group(func_pair)  # Здесь выполняем обе функции в группе

        if i < len(function_group) - 1:
            print("Группа завершила работу, ожидание 15 секунд перед запуском следующей группы...")
            await asyncio.sleep(15)

    print("Все группы завершили свою работу.")

if __name__ == "__main__":
    asyncio.run(main())
