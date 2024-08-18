import obd
from app.helpers import showOptions
from app.reset import resetErrors
from app.check import showAllErrors

# available view
home_view = "HomePage"
screener_view = "ScreenerView"

# available options
check_errors = "Error screener"

# actions
show_errors = "Show errors"
reset_errors = "Clean errors"
exit = "Exit"
back = "Back"

# state variables
currentState = home_view
previousState = ''

connection = obd.OBD('/dev/tty.usbserial-2140')
isConnected = connection.is_connected()


# mapping what to do after selecting corresponding action
def flow(option):
    global currentState, previousState, connection
    if option == check_errors:
        previousState = currentState
        currentState = screener_view
    elif option == reset_errors:
        return resetErrors(connection)
    elif option == show_errors:
        return showAllErrors(connection)
    elif option == exit:
        currentState = 'Exit'
    elif option == back:
        currentState = previousState

# main function to change page view
# after typing 'Exit' the program will close, because there are not
# such case for ExitFlow, if case didn't match view() method just finish execution
def view(view_option):
    if view_option == home_view:
        print("Welcome to the OBD II Screener\n")
        print("Select option by typing it number\n")
        print (f"Connection status: {isConnected}")
        if isConnected:
            flow(showOptions([check_errors, reset_errors, exit]))
        else:
            flow(showOptions([exit]))
    elif view_option == screener_view:
        flow(showOptions([show_errors,back, exit]))
        
    if (view_option != 'Exit'):
        view(currentState)
        
# entrypoint
view(currentState)