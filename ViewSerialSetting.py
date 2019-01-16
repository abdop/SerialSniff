import serial


com_port1 = 'COM1'

listener = serial.Serial(com_port1)
listener
print(listener)
