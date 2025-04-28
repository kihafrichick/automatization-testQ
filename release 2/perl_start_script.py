import subprocess
def test_analyzer():
    
    ip = "192.168.17.167"
    commands = ["2", ":SENSE:TEST:RESET", ":SENSE:DATA? CSTATUS:MAC:L2:FRAME:DETECT"]
    input_data = "\n".join(commands) + "\n"
    try:    
        result = subprocess.run(
            ["perl", "RC-5800.pl", ip],
            input=input_data,
            text=True,
            capture_output=True
            )
        output = result.stdout.strip().splitlines()
        if len(output) >= 2: 
            status_line = output[-2]  
            
            if status_line.strip() == "> 1":
                print("Соединение активно")
                return "Success"
            elif status_line.strip() == "> 0":
                print("Соединение разорвано")
                return "Error"
            else:
                print("Неизвестный статус:", status_line)
                return "Error"
        else:
            print("Недостаточно данных в выводе")
            return "Error"
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения perl-скрипта: {e}")
        return "Error"
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return "Error"
if __name__ == "__main__":
        status = test_analyzer()
        print(f"Final status: {status}")