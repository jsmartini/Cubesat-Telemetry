import util.zumlink as zum

device = input("device:\t")
radio = zum.zumlink(device=device)
radio.terminal()