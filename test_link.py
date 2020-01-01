from dronekit import Vehicle, connect, VehicleMode, LocationGlobal
from pymavlink import mavutil

import dronekit

vehicle = connect("/dev/serial0", wait_ready=True, baud=57600)
print("System Status: " + vehicle.system_status.state)
print("Battery: " + str(vehicle.battery.voltage))
vehicle.close()
