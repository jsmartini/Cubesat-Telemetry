import serial

class x(serial.Serial):

    def __init__(self):
        super().__init__(port="COM11", baudrate=3000000)
        assert super().isOpen == True
        print("open") 

x()