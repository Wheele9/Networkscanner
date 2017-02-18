import nmap                                                                 
import time
import dynamicprint

from info import KNOWN_MACS
"""
Scan your network with nmap.
"""


def getMAC(data):
    ''' get MAC adresses from the nested dictionary, returned by nmap'''
    macList = {}
    for IP in data['scan']:
        MAC = data["scan"][IP]["addresses"].get('mac',None)
        NAME = data["scan"][IP]["vendor"].get(MAC, None)
        macList[MAC]=[IP, NAME]

    return macList

        
nm = nmap.PortScanner()
printer = dynamicprint.multiPrinter()
logFile = "macs.log" 

while True:

    data = nm.scan(hosts="192.168.0.1/24", arguments="-sP")
    onlineDevs=getMAC(data)
    liveKnownDevices = []
    liveUnKnownDevices = []
    printer.addEmptyLine()
    printer.addLine ("Nr of online devices: {}".format(len(onlineDevs)), 'WHITE', 'BRIGHT')
    printer.addEmptyLine ()
    for MACadress in onlineDevs: 
        
        if MACadress in KNOWN_MACS:
            liveKnownDevices.append(MACadress)
        else: 
            
            liveUnKnownDevices.append([ MACadress, onlineDevs[MACadress][0],onlineDevs[MACadress][1]])
    f = open(logFile, 'a')
    printer.addLine ("Suspicous devices", 'red', 'BRIGHT')
    for device in liveUnKnownDevices:
        printer.addLine ("MAC: {}, IP: {}, NAME: {}".format(device[0], device[1], device[2]) , 'RED', )
        device2string = " ".join(list(filter(None.__ne__, device)))
        f.write(device2string)
    f.close()

    deviceNames = [KNOWN_MACS[MACadress] for MACadress in liveKnownDevices]
    printer.addEmptyLine()
    printer.addLine("Known online devices", 'CYAN', 'BRIGHT')
    for device in liveKnownDevices:
        printer.addLine(KNOWN_MACS[device], 'CYAN')
    printer.update()
    time.sleep(2)
