import util.radio as radio


device = ""

endpoint = radio.Endpoint(device, custom_config=radio.generate_config(txPower=0))

while 1:
    endpoint.recv()
