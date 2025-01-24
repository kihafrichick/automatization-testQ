import subprocess

def run_script(script_name):
    """Функция для запуска скрипта с помощью subprocess."""
    process = subprocess.Popen(['python', script_name])  # Запуск скрипта
    return process

if __name__ == '__main__':
    # Запускаем оба скрипта параллельно
    processes = []
    processes.append(run_script('sborka_bez_monitoringa.py'))
    processes.append(run_script('sborka_bez_monitoringa_blades.py'))

    # Дожидаемся завершения обоих скриптов
    for process in processes:
        process.wait()  # Блокировка до завершения процесса

    print("Все скрипты завершены.")