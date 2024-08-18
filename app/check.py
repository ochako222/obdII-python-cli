import obd

def showAllErrors(connection):
    print('showing all errors')
    # dtc_list = connection.query(obd.commands.GET_DTC)
    
    # if dtc_list.is_null():
    #     print("No DTCs found.")
    # else:
    #     for dtc in dtc_list.value:
    #         print(f"Code: {dtc[0]}, Description: {dtc[1]}")
    #         # connection.query(obd.commands.CLEAR_DTC)
    #         # print("DTCs cleared.")
            
        