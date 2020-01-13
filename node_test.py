import util.radio as radio


#device = "COM8" #device serial port if windows i.e. COM8; if linux tr /dev/tty..... or similar

node = radio.zumlink("COM11")

config = radio.generate_config(radioMode="Gateway", txPower=0)
node.setup(config)
node.Terminal()