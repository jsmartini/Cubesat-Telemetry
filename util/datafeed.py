import serial
import asyncio
import threading
import os
import json
from datetime import datetime


"""
                    THIS IS ALL SUBJECt to CHANGE WILL PROBABLY GET THROWN

"""

class device_interface(serial.Serial):

    def __init__(self,device: "str", data_label: "str", BaudRate = 9600, bytesize = serial.EIGHTBITS, stopbits = serial.STOPBITS_ONE):
        super.__init__(device, buadrate=BaudRate, bytesize=bytesize, stopbits=stopbits)
        self.data_label = data_label
    #do be defined for each device
    def get_data(self):
        return

    def get_info(self) -> "str":
        return

    def data_label(self):
        return self.data_label

class DataFeed:

    def __init__(self, device: "device_interface"):
        self.device = device
        print("DATAFEED FOR {0} Initiated".format(device.get_info()))

    def read(self):
        return (datetime.now(),self.device.get_info, self.device.data_label(), self.device.get_data())
        
class FeedAggregator:
    #may make more sense to just hard code the sensors into actual functions not class functions
    def __init__(self, update_wait=1):
        self.interval = update_wait
        self.feed_list = []

    def add(self, device: "DataFeed"):
        self.feed_list.append(device)    

    async def read(self, dev: "DataFeed"):
        await asyncio.sleep(1)
        return dev.read()

    async def main(self):
        function_list = []
        for datafeed in self.feed_list:
            function_list.append(self.read(datafeed))
        await asyncio.gather(function_list)             
        
#example with hardcoded

arduino_temperature = DataFeed(device_interface(device="/dev/tty9", data_label="Temperature"))
arduino_pressure    = DataFeed(device_interface(device="/dev/tty8", data_label="Pressure"))

async def Temperature():
    await asyncio.sleep(1)
    return arduino_temperature.read()

async def Pressure():
    await asyncio.sleep(1)
    return arduino_pressure.read()

async def main():
    await asyncio.gather(Temperature(), Pressure())
    