import serial
import time

device = input("device:")
baud   = input("baud:")
mode   = input("mode:")


z = serial.Serial(
    port = device,
    bytesize = serial.EIGHTBITS,
    stopbits = serial.STOPBITS_ONE,
    baudrate = baud
)

assert z.isOpen() == True
print("is open")

def send(filename: str) -> None:
    z.write(open(filename, 'rb').read().encode())

def recv(self):
    while 1:
        print(z.readline().decode())
    
def term9600():
    while 1:
        req = input("term>>>")
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

def term3000000():
    while 1:
        req = input("echo>>>")
        if req == "exit()":
            break
        z.write(req.encode() + b'/r/n')

def recv():
    while 1:
        time.sleep(0.1)
        print(z.readline().decode())

if mode.upper() == "ENDPOINT":
    recv()
if mode.upper() == "GATEWAY":
    term3000000()
if mode.upper() == "TERM":
    term9600()
else:
    print("Bad Mode")