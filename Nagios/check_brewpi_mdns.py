import sys
import tcpSerial


ser=None
#tcpHost="192.168.8.147"
#tcpPort=8080
mdns=tcpSerial.MDNSBrowser()
(tcpHost, tcpPort)=mdns.discoverBrewpis()

if tcpHost is not None and tcpPort is not None:
    #print "Connecting to BrewPi ", tcpHost, " on port ", tcpPort
    ser=tcpSerial.TCPSerial(tcpHost,tcpPort)

if ser:
        ser.write("l\n")
        reply=ser.readline()
        print reply
else:
    print "Connection failed"
