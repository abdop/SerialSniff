import serial
import time

baud_rate = 9600  # whatever baudrate you are listening to
com_port2 = '/dev/ttyUSB0'  # replace with your first com port path
com_port1 = '/dev/ttyACM0'  # replace with your second com port path
Data_Bits = 'serial.EIGHTBITS'
Parity = 'serial.PARITY_NONE'
Stop_Bits = 'serial.STOPBITS_ONE'
ComRead_timeout = 2
Flow_Control = False
ComWr_timeout = 2
log = open('log.txt', 'a+')

From_PC_To_Cam = True

listener = serial.Serial(com_port1, baud_rate, timeout=ComRead_timeout, write_timeout=ComWr_timeout)
# forwarder = serial.Serial(port=com_port2, baudrate=baud_rate, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
#                           stopbits=serial.STOPBITS_ONE, timeout=ComRead_timeout, xonxoff=False, rtscts=False,
#                           write_timeout=ComWr_timeout)

while 1:
    while (listener.inWaiting()) and From_PC_To_Cam:
        serial_out = listener.readline()  # type: 
        localtime = time.asctime(time.localtime(time.time()))
        Msg = localtime + serial_out
        log.write(Msg)
        print(serial_out)  # or write it to a file
        #forwarder.write(serial_out)
    # else:
    #     From_PC_To_Cam = False

    # while (forwarder.inWaiting()) and not From_PC_To_Cam:
    #     serial_out = forwarder.readline()
    #     localtime = time.asctime(time.localtime(time.time()))
    #     log.write(localtime, serial_out)
    #     print(serial_out)  # or write it to a file
    #     listener.write(serial_out)
    # else:
    #     From_PC_To_Cam = True
