import serial
from serial import Serial

portName = "COM3"

ser = serial.Serial(portName,9600)
data = ser.readline(1000)
print(data)
