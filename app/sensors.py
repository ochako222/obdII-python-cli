import obd # type: ignore

def get_sensor_data(connection):
    """
    Retrieves commonly used live sensor data from the vehicle.
    
    Args:
        connection: An active OBD connection object.
    
    Returns:
        A dictionary where the keys are sensor names and the values are the sensor readings.
    """
    # Dictionary to store sensor data
    sensor_data = {}
    
    # List of commonly used OBD-II commands
    common_commands = [
        obd.commands.RPM,                   # Engine RPM
        obd.commands.SPEED,                 # Vehicle Speed
        obd.commands.COOLANT_TEMP,          # Coolant Temperature
        obd.commands.THROTTLE_POS,          # Throttle Position
        obd.commands.ENGINE_LOAD,           # Engine Load
        obd.commands.MAF,                   # Mass Air Flow
        obd.commands.FUEL_LEVEL,            # Fuel Level
        obd.commands.INTAKE_TEMP,           # Intake Air Temperature
        obd.commands.BAROMETRIC_PRESSURE,   # Barometric Pressure
        obd.commands.TIMING_ADVANCE,        # Timing Advance
    ]
    
    # Query each command and store the result
    for command in common_commands:
        response = connection.query(command)
        if not response.is_null():
            sensor_data[command.name] = response.value
        else:
            sensor_data[command.name] = 'No Data'

    connection = obd.OBD()
    if connection.is_connected():
        for sensor, value in sensor_data.items():
            print(f"{sensor}: {value}")
    else:
        print("Failed to connect to the OBD-II adapter.")