import util.radio as radio


device = "" #device serial port if windows i.e. COM8; if linux tr /dev/tty..... or similar

node = radio.zumlink(device)

try:
    info = node.getDeviceSettings()
    print("DEVICE: {0}\t{1}\t{2}".format(info["name"], info["firmware"], info["Serial"]))
    node.debugTerminal()
except:
    print("Try adjusting BaudRate")
    exit(-1)