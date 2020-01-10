import serial
import time

def generate_config(radioMode = "Endpoint", rfDataRate = "RATE_1M", txPower=10, networkId = 77777, frequencyKey=0, radioFrequency=915.0000, radioHoppingMode="Hopping_On", beaconInterval="ONE_HUNDRED_MS", beaconBurstCount=1, lnaBypass=0, maxLinkDistanceInMiles=5, maxPacketSize=900, cliBaudRate=115200, packetizedBaudRate=3000000, passthruBaudRate = 3000000, databits=8, parity="None", stopbits=1, flowControl="Hardware", passthruLatencyMode="auto", passthruLatencyTimer=16):
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

    def __init__(self, device: str):
        super.__init__(
            port = device,
            bytesize = serial.EIGHTBITS,
            stopbits = serial.STOPBITS_ONE,
            baudrate = 9600
        )
        #making sure connection is open
        assert super.isOpen() == True
        print("{0} Connection opened".format(device))

    def command(self, c: str) -> str:
        assert super.isOpen() == True
        #test function
        super.write(c.encode() + b"\r\n")
        output = b''
        while super.inWaiting() > 0:
            output += super.read(1)
        return output.decode()

    def terminal(self):
        while True:
            req = input(">>>")
            if req == "exit()":
                break
                    #if req == "send()":
                    #   req = input("FILENAME:\t")
                    #   self.send(req)
            if req == "send()":
                dataFile = input("Data File for Transfer:\t")
                self.send(dataFile=dataFile)

            req = req.encode()
            super.write(req + b'\r\n')
            output = b''
            time.sleep(0.5) #set at half second, if device doesnt res increment
            while super.inWaiting() > 0:
                output = z.read(1)
                if output != '':
                    print(output.decode(), end='')

    def send(self, dataFile: str) -> None:
        #writes data to the serial port device
        #to be tested
        super.write(open(dataFile, "rb").read())

    def recv(self) -> str:
        #to be tested
        #reads data from the serial port device
        return super.readline().decode("utf-8")

    def setup(self, settings = generate_config()):
        assert super.isOpen() == True
        for radioSetting in settings["radioSettings"]:
            self.command("radioSettings." + radioSetting)
        """Serial settings should not change, but uncomment if needed
        for serialSetting in settings["serialSettings"]:
            self.command("serialSettings." + serialSetting)
        """

class Gateway(zumlink):
    #gateway node in the network
    def __init__(self, device: str, settings = generate_config(radioMode="Gateway", txPower=30)):
        super.__init__(device)
        super.setup(settings = setttings)

class Endpoint(zumlink):
    #endpoint node in the network
    def __init__(self, device:str, datafile = "flightLog.data",settings = generate_config(radioMode="Endpoint", txPower=30))
        super.__init__(device)
        super.setup(settings = settings)
        if os.path.exists("./"+datafile):
            os.mknod("./"+datafile)
        self.logname = datafile

            
