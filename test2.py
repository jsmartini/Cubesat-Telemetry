import util.zumlink as zum
from util.zumlink import generate_config
mode = input(">>>") 
device = input("device:\t")
radio = zum.zumlink(device=device)

if mode.upper() == "ENDPOINT":
    radio = zum.zumlink(device=device, mode = False)
    radio.recv_test()

if mode.upper() == "GATEWAY":
    radio = zum.zumlink(device=device, mode = True)
    radio.setup(settings=generate_config(radioMode="Gateway", txPower=0))
    radio.transmit_test()

