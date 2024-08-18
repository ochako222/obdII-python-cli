import os
import time

def showOptions(options):
    inputMessage = "Pick an option:\n"

    for index, item in enumerate(options):
        inputMessage += f'{index+1}) {item}\n'

    userInput = input(inputMessage)

    if (userInput in options):
        os.system('clear')
        return userInput
    else:
        os.system('clear')
        print(options)
        print(f"your option: {userInput}\n")
        print("Selected wrong option! Pls try again...\n")
        time.sleep(2)
        os.system('clear')
        return showOptions(options)
    
    

       
        
        

