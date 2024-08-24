import os
import time
from colorama import init, Fore, Style

init(autoreset=True)


def fancy_greeting():
    os.system('clear')
    print(Fore.YELLOW + Style.BRIGHT + """
 _____ ______ ______  _____  _____ 
|  _  || ___ \|  _  \|_   _||_   _|
| | | || |_/ /| | | |  | |    | |  
| | | || ___ \| | | |  | |    | |  
\ \_/ /| |_/ /| |/ /  _| |_  _| |_ 
 \___/ \____/ |___/   \___/  \___/ 
                                                                   
    """)
    print(Fore.GREEN + "Welcome to the OBD II Screener!")
    print(Fore.GREEN + "This tool helps you to check and reset OBDII errors.")
    print(Fore.CYAN + "-" * 50)
    time.sleep(2)

def showOptions(options):
    input_message = "Pick an option:\n"

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    user_input = input(input_message).strip()

    # Check for case-insensitive match
    normalized_options = [option.lower() for option in options]
    normalized_input = user_input.lower()

    if normalized_input in normalized_options:
        os.system('clear')
        # Return the correctly capitalized option
        return options[normalized_options.index(normalized_input)]
    else:
        os.system('clear')
        print(f"Your option: {user_input}\n")
        print("Selected wrong option! Please try again...\n")
        time.sleep(2)
        os.system('clear')
        return showOptions(options)