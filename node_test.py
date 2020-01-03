import util.radio as radio


device = "" #device serial port if windows i.e. COM8; if linux tr /dev/tty..... or similar

node = radio.zumlink(device)

config = radio.generate_config(radioMode="Gateway", txPower=0)
node.setup(config)
node.Terminal()