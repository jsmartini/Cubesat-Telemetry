import util.radio as radio

device = ""

gateway = radio.Gateway(device, custom_config=radio.generate_config(radioMode="Gateway", txPower=0))

msg = "Hello ARA!"
filename = "ARA.txt"
f = open(filename)
f.write(msg)
f.close()

gateway.send(filename)
