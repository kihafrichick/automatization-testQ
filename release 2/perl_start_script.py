import subprocess
def test_analyzer():
    address_ip = "192.168.17.167"
    commands = ["2", ":SENSE:TEST:RESET", ":SENSE:DATA? CSTATUS:MAC:L2:FRAME:DETECT"]

    input_data = "\n".join(commands) + "\n"
    result = subprocess.run(
        ["perl", "RC-5800.pl", address_ip],
        input=input_data,
        text=True,
        capture_output=True
        )
    output = result.stdout.strip().splitlines()
    if len(output) >= 2: 
        status_line = output[-2]  
        
        if status_line.strip() == "> 1":
            print("Соединение активно")
        elif status_line.strip() == "> 0":
            print("Соединение разорвано")
        else:
            print("неизвестный статус:", status_line)
    else:
        print("Error: Недостаточно данных в выводе")

if __name__ == "__main__":
    test_analyzer()