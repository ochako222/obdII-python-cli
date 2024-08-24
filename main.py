import obd
from app.helpers import fancy_greeting, showOptions
from app.reset import resetErrors
from app.check import showAllErrors
from colorama import Fore

# Constants
HOME_VIEW = "HomePage"
SHOW_ERRORS = "Show errors"
RESET_ERRORS = "Clean errors"
EXIT = "Exit"
BACK = "Back"

# State variables
current_state = HOME_VIEW
previous_state = ''

# Initialize connection
ports = obd.scan_serial()
if ports:
    port_to_connect = ports[-1]
    connection = obd.OBD(port_to_connect)
    is_connected = connection.is_connected()
else:
    print("No OBD ports found. Exiting...")
    exit()
    
    
# Function to map selected action to corresponding functionality
def flow(option):
    global current_state, previous_state, connection
    if option == RESET_ERRORS:
        resetErrors(connection)
    elif option == SHOW_ERRORS:
        showAllErrors(connection)
    elif option == EXIT:
        current_state = EXIT
    elif option == BACK:
        current_state = previous_state
        
# Main function to handle views
def view(view_option):
    global current_state
    if view_option == HOME_VIEW:
  
        print('Connected to port: ', Fore.YELLOW + f'{port_to_connect}')
        print('Connection status: ', Fore.YELLOW + f'{is_connected}\n')
        
        if is_connected:
            flow(showOptions([SHOW_ERRORS, RESET_ERRORS, EXIT]))
        else:
            flow(showOptions([EXIT]))
        
    if current_state != EXIT:
        view(current_state)

# Entrypoint
if __name__ == "__main__":
    fancy_greeting()
    view(current_state)