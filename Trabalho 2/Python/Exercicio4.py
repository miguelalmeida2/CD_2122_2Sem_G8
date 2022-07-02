import serial
from serial import Serial

portName = '/dev/cu.usbmodem14101'
# portName = "COM3"

ser = serial.Serial(portName, 9600)
data = ser.readline(4000)
print(data)


