import subprocess

def run_script(script_name):
    """Функция для запуска скрипта с помощью subprocess."""
    process = subprocess.Popen(['python', script_name])  # Запуск скрипта
    return process

if __name__ == '__main__':
    # Запускаем оба скрипта параллельно
    processes = []
    #processes.append(run_script('try_3_controller_code.py'))
    processes.append(run_script('tabs_check.py'))
    processes.append(run_script('tabs_check_not_blades.py'))
    #processes.append(run_script('coloring_try3.py'))
    #processes.append(run_script('coloring_try_blades.py'))
    # Дожидаемся завершения первых трех скриптов
    for i in range(3):  # Ждем только первые три процесса завершиться
        processes[i].wait()  # Блокировка до завершения процесса

    print("Первые три скрипта завершены. Завершаем последние два...")

    # Завершаем последние два скрипта
    for i in range(3, len(processes)):  # Находим последние два процесса
        if processes[i].poll() is None:  # Проверяем, если процесс еще запущен
            processes[i].terminate()  # Завершаем процесс

    # Опционально, ждём завершения последних двух скриптов
    for i in range(3, len(processes)):
        processes[i].wait() 

    print("Все скрипты завершены.")