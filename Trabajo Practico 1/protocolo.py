from Tkinter import *
import serial
import binascii
from crccheck.crc import Crc32c
from crccheck.checksum import Checksum32

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'

cantidadRegistros = 10

ser.open()

print(ser.is_open)

ser.write(binascii.unhexlify('01030000000ac5cd'))

data = binascii.hexlify(ser.read(5+cantidadRegistros*2))
ser.close()

newData = data[6:data.__len__()-4]

i = 0
while i < len(newData):
    firstnum = newData[i:i+4]
    decimal = int(firstnum, 16)
    print(decimal)
    i += 4

#print(binascii.hexlify(ser.read(5+cantidadRegistros*2)))


