import serial
import time
z = serial.Serial(
    port = "COM11",
    bytesize = serial.EIGHTBITS,
    stopbits = serial.STOPBITS_ONE,
    baudrate = 9600
)

assert z.isOpen() == True
print("is open")

def send(filename: str) -> None:
    z.write(open(filename, 'rb').read().encode())

def recv(self):
    output = b''
    while z.inWaiting() > 0:
        output = z.readline().decode()
        print(output, end = '') 

while 1:
    req = input(">>>")
    if req == "exit()":
        break
                #if req == "send()":
                 #   req = input("FILENAME:\t")
                 #   self.send(req)
    req = req.encode()
    z.write(req + b'\r\n')
    output = b''
    time.sleep(0.5) #set at half second, if device doesnt res increment
    while z.inWaiting() > 0:
        output = z.read(1)
        if output != '':
            print(output.decode(), end='')

