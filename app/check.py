import obd # type: ignore

def showAllErrors(connection):
    dtc_list = connection.query(obd.commands.GET_DTC)
    
    if connection.is_connected():
        if dtc_list.is_null():
           print("No DTCs found.\n")
        else:
            for dtc in dtc_list.value:
                print(f"Code: {dtc[0]}, Description: {dtc[1]}\n")
    else:
        print("Failed to connect to the OBD-II adapter.")
            
        