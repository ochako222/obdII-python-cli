import obd

# ports = obd.scan_serial()       # return list of valid USB or RF ports
# print (ports) 

connection = obd.OBD('/dev/tty.usbserial-2140') # auto-connects to USB or RF port

if connection.is_connected():
    print("Connected to the vehicle!")
    

    dtc_list = connection.query(obd.commands.GET_DTC)

    # Print the list of DTCs
    if dtc_list.is_null():
        print("No DTCs found.")
    else:
        for dtc in dtc_list.value:
            print(f"Code: {dtc[0]}, Description: {dtc[1]}")
            # connection.query(obd.commands.CLEAR_DTC)
            # print("DTCs cleared.")

    # # Query a specific OBD-II command
    # response = connection.query(obd.commands.RPM)  # Example command
    # print(response.value)  # Print the RPM value

else:
    print("Failed to connect to the vehicle.")

# Disconnect after use
connection.close()