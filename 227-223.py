import subprocess

def run_script(script_name):
    """Функция для запуска скрипта с помощью subprocess."""
    process = subprocess.Popen(['python', script_name])  # Запуск скрипта
    return process

if __name__ == '__main__':
    # Запускаем оба скрипта параллельно
    processes = []
    processes.append(run_script('full_without_monitoring.py'))
    processes.append(run_script('test_for_blade_223.py'))

    # Дожидаемся завершения обоих скриптов
    for process in processes:
        process.wait()  # Блокировка до завершения процесса

    print("Все скрипты завершены.")