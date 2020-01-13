import serial

class x(serial.Serial):

    def __init__(self):
        super.__init__(port="COM11", baudrate=9600)