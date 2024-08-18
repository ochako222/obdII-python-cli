from app.helpers import showOptions
from app.reset import resetFlow
from app.check import checkFlow

# state variables
currentState = 'HomePage'
previousState = ''

# available options
check_errors = "Check errors"
reset_errors = "Reset errors"
exit = "Exit"
back = "Back"

def flow(option):
    global currentState, previousState
    if option == check_errors:
        previousState = currentState
        currentState = 'CheckView'
        return checkFlow()
    elif option == reset_errors:
        previousState = currentState
        currentState = 'ResetView'
        return resetFlow()
    elif option == exit:
        currentState = 'Exit'
    elif option == back:
        currentState = previousState

# main function to change page view
def view(state):
    match state:
        case "HomePage":
            print("Welcome to the OBD II Screener\n")
            print("Select option by typing it number\n")
            flow(showOptions([check_errors, reset_errors, exit]))
        case "ResetView":
            # print(f"You logged as {loggedUser.username}\n")
            flow(showOptions(['Foo1','Foo2',back, exit]))
        case "CheckView":
            # print(f"You logged as {loggedUser.username}\n")
            flow(showOptions(['Boo1','Boo2',back, exit]))
        
    if (state != 'Exit'):
        view(currentState)
        
# entrypoint
view(currentState)