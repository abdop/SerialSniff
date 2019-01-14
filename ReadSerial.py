import serial

baud_rate = 9600 #whatever baudrate you are listening to
com_port2 = '/dev/ttyUSB0' #replace with your first com port path
com_port1 = '/dev/ttyACM0' #replace with your second com port path
Data_Bits = 'EIGHTBITS'
Parity = 'PARITY_NONE' 
Stop_Bits = 'STOPBITS_ONE'
ComRead_timeout = 2
Flow_Control = False
ComWrite_timeout = 2

From_PC_To_Cam = True


listener = serial.Serial(com_port1, baud_rate, timeout=ComRead_timeout, write_timeout=ComWrite_timeout)
forwarder = serial.Serial(com_port2, baud_rate, timeout=ComRead_timeout, write_timeout=ComWrite_timeout)
listener.write('sh run')

while 1:
#listener.inWaiting():
    serial_out = listener.readline()
    print serial_out #or write it to a file 
    forwarder.write(serial_out)


