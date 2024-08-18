import obd

def resetErrors(connection):
    dtc_list = connection.query(obd.commands.GET_DTC)
    
    if dtc_list.is_null():
        print("No DTCs found.\n")
    else:
        for dtc in dtc_list.value:
            connection.query(obd.commands.CLEAR_DTC)
            print("DTCs cleared.\n")
            
        