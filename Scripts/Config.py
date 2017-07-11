import sys
import tcpSerial


ser=None
mdns=tcpSerial.MDNSBrowser()
(tcpHost, tcpPort)=mdns.discoverBrewpis()

if tcpHost is not None and tcpPort is not None:
    print "Connecting to BrewPi ", tcpHost, " on port ", tcpPort
    ser=tcpSerial.TCPSerial(tcpHost,tcpPort)

if ser:
        ser.write("d\n")
        reply=ser.readline()
        print reply
        ser.write("p\n")
        reply=ser.readline()
        print reply
        ser.write("c\n")
        reply=ser.readline()
        print reply
else:
    print "Connection failed"