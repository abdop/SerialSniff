import serial
import time

com_port1 = '/dev/ttyUSB0'  # replace with your first com port path

baud_rate_FC = 19200
Data_Bits_FC = serial.EIGHTBITS
Parity_FC = serial.PARITY_ODD
Stop_Bits_FC_Tx = serial.STOPBITS_TWO
Stop_Bits_FC_Rx = serial.STOPBITS_ONE

ComRead_timeout = 0.1
Flow_Control = False
ComWr_timeout = 0.1

log = open('log.txt', 'a+')

From_PC_To_Cam = True

''' # for liaison Routeur Cisco
listener = serial.Serial(com_port1, baud_rate, timeout=ComRead_timeout, write_timeout=ComWr_timeout)
forwarder = serial.Serial(port=com_port2, baudrate=baud_rate, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                          stopbits=serial.STOPBITS_ONE, timeout=ComRead_timeout, xonxoff=False, rtscts=False,
                          write_timeout=ComWr_timeout)
'''
listener = serial.Serial(port=com_port1, baudrate=baud_rate_FC, bytesize=Data_Bits_FC, parity=Parity_FC,
                         stopbits=Stop_Bits_FC_Rx, timeout=ComRead_timeout, xonxoff=False, rtscts=False,
                         write_timeout=ComWr_timeout)

while 1:
    while (listener.inWaiting()) and From_PC_To_Cam:
        serial_out = listener.readline()
        localtime = time.asctime(time.localtime(time.time()))
        Msg = "PC " + localtime + " " + serial_out.encode('hex')
        Msg += "\n"
        log.write(Msg)
        print(serial_out.encode('hex'))  # or write it to a file
        '''
    else:
        From_PC_To_Cam = False

    while (forwarder.inWaiting()) and not From_PC_To_Cam:
        serial_out = forwarder.readline()
        localtime = time.asctime(time.localtime(time.time()))
        Msg = "CAM " + localtime + " " + serial_out + "\n"
        log.write(Msg)
        print(serial_out)  # or write it to a file
        listener.write(serial_out)
    else:
        From_PC_To_Cam = True
'''