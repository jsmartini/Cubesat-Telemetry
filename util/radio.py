import serial 
import json
import time


def generate_config(radioMode = "Endpoint", rfDataRate = "RATE_1M", txPower=10, networkId = 77777, frequencyKey=0, radioFrequency=915.0000, radioHoppingMode="Hopping_On", beaconInterval=ONE_HUNDRED_MS, beaconBurstCount=1, lnaBypass=0, maxLinkDistanceInMiles=5, maxPacketSize=900, cliBaudRate=115200, packetizedBaudRate=3000000, passthruBaudRate = 3000000, databits=8, parity="None", stopbits=1, flowControl="Hardware", passthruLatencyMode="auto", passthruLatencyTimer=16):
    return {
        "radioSettings":[
            "radioMode={0}".format(radioMode),
            "rfDataRate={0}".format(rfDataRate),
            "txPower={0}".format(txPower),
            "networkId={0}".format(networkId),
            "frequencyKey={0}".format(frequencyKey),
            "radioFrequency={0}".format(radioFrequency),
            "radioHoppingMode={0}".format(radioFrequency),
            "beaconInterval={0}".format(beaconInterval),
            "beaconBurstCount={0}".format(beaconBurstCount),
            "lnaBypass={0}".format(lnaBypass),
            "maxLinkDistanceInMiles={0}".format(maxLinkDistanceInMiles),
            "maxPacketSize={0}".format(maxPacketSize),
            "frequencyMasks="
        ],
        "serialPortConfig":[
            "cliBaudRate={0}".format(cliBaudRate),
            "packetizedBaudRate={0}".format(packetizedBaudRate),
            "passthruBaudRate={0}".format(passthruBaudRate),
            "databits={0}".format(databits),
            "parity={0}".format(parity),
            "stopbits={0}".format(stopbits),
            "flowControl={0}".format(flowControl),
            "passthruLatencyMode={0}".format(passthruLatencyMode),
            "passthruLatencyTimer={0}".format(passthruLatencyTimer)
        ]
    }

class zumlink(serial.Serial):

    #look over the config for data speeds config 16.12; 16.
    #set txPower=0 during testing or we are going to get cancer
    #serialPort.Config.passthruBaudRate=3Mbps or > radioSettings.rfDataRate

    def __init__(self, device):
        try:
            #baudrate might be wrong
            super().__init__(device, btyesize = serial.EIGHTBITS, baudrate = 9600, stopbits = serial.STOPBITS_ONE)
        except:
            raise serial.SerialException("Device Not Setup")
            exit(-1)
        else:
            print("Device Configured")
    
    def debugTerminal(self):
        if super.isOpen():
            print("Zumlink Terminal Mode\r\ntype exit() to leave, send() for transmit prompt")
            while 1:
                req = input(">>>")
                if req == "exit()":
                    break
                if req == "send()":
                    req = input("FILENAME:\t")
                    self.send(req)
                super.write(req + '\r\n')
                output = ''
                time.sleep(0.5) #set at half second, if device doesnt res increment
                while super.inWaiting() > 0:
                    output += super.read(1)
                if output != '':
                    print("[*]"+ output)
        else:
            exit(-1)

    def command(self, c):
        super.write(c + "\r\n")

    def readSetting(self, c):
        output = ''
        super.write(c + "\r\n")
        time.sleep(0.5)
        while super.inWaiting() > 0:
            output += super.read(1)
        if output == '':
            return "error"
        return output

    def getDeviceSettings(self):
        info = {}
        info["firmware"] = readSetting("FirmwareVersion")
        info["name"]     = readSetting("deviceName")
        info["Serial"]   = readSetting("deviceSerialNumber")
        return info

    def send(self, dataFile):
        super.write(open(dataFile, "rb").read())

    def recv(self):
        print(super.readline().decode("utf-8"))

    def __del__(self):
        super.__del__()
        exit(-1)    

class Gateway(zumlink):

    configuration = {

        "radioSettings":
        [
            "radioMode=Gateway",
            "rfDataRate=RATE_1M",
            "txPower=30",
            "frequencyKey=0",
            "networkId=77777"
            "radioFrequency=915.0000",
            "radioHoppingMode=Hopping_On",
            "beaconInterval=ONE_HUNDRED_MS",
            "beaconBurstCount=1",
            "lnaBypass=0",
            #"maxLinkDistanceInMiles=10",    #distance to change probably
            "maxPacketSize=900"             #packet sizes to change probably
        ],
        "serialPortConfig":
        [
            "cliBaudRate=115200",
            "packetizedBaudRate=3000000",
            "passthruBaudRate=3000000",
            "databits=8",
            "parity=None",
            "stopbits=1",
            "flowControl=Hardware",
            "passthruLatencyMode=Auto",
            "passthruLatencyTimer=16"
        ]
    }

    def __init__(self, device, custom_config=None):
        if custom_config != None:
            self.configuration = custom_config
        super.__init__(device)
        for setting in configuration["radioSettings"]:
            super.command("radioSettings."+setting)
        for setting in configuration["serialPortConfig"]:
            super.command("serialPortConfig."+setting)
        super.command("save")

class Endpoint(zumlink):

    configuration = {
        "radioSettings" :
        [
            "radioMode=Endpoint",
            "rfDataRate=RATE_1M",
            "txPower=30",
            "networkId=77777",
            "frequencyKey=0",
            "radioFrequency=915.0000",
            "radioHoppingMode=Hopping_On",
            "beaconInterval=ONE_HUNDRED_MS",
            "beaconBurstCount=1",
            "lnaBypass=0",
            #"maxLinkDistanceInMiles=10" #milage to change
            "maxPacketSize=900"         #packet size to change
        ],
        "serialPortConfig":
        [
            "cliBaudRate=115200",
            "packetizedBaudRate=3000000",
            "passthruBaudRate=3000000",
            "databits=8",
            "parity=None",
            "stopbits=1",
            "flowControl=Hardware",
            "passthruLatency=Auto",
            "passthruLatencyTimer=16"
        ]
    }

    def __init__(self, device, custom_config=None):
        super.__init__(device)
        if custom_config != None:
            self.configuration = custom_config
        for setting in configuration["radioSettings"]:
            super.command("radioSetting."+setting)
        for setting in configuration["serialPortConfig"]:
            super.command("serialPortConfig."+setting)
        super.command("save")

    