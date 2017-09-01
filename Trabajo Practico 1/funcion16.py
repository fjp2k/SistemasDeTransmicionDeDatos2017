import binascii
from array import array

import serial
import funcion03

puertoEnvia=serial.Serial()
puertoRecibe=serial.Serial()
dispositivo=17
funcion=16
direccion=1

def devolverValoresDecimal():
    i=0
    print("\tValores en decimal: ")
    while(i<registros):
        valorDecimal = int(valoresIngresados[i],16)
        print("\t\tRegistro %d: %d" %(i,valorDecimal))
        i+=1

def devolverValoresHexadecimal():
    i=0
    print("\tValores en Hexadecimal: ")
    while(i<registros):
        print("\t\tRegistro %d: %s" %(i, valoresIngresados[i]))
        i+=1

def devolverValoresBinario():
    i=0
    print("\tValores en Binario: ")
    while(i<registros):
        valorDecimal=int(valoresIngresados[i],16)
        print("\t\tRegistro %d: %s" %(i,bin(valorDecimal)))
        i+=1

def solicitud(trama):
    print("Trama Enviada: %s" %trama)
    resultado = puertoEnvia.write(binascii.unhexlify(trama))
    devolucion = binascii.hexlify(puertoRecibe.read(6))
    crc= funcion03.calc(devolucion)
    devolucion = devolucion + crc
    print("Trama devuelta: %s" % devolucion)

def obtenerTrama():
    intDispo= int(dispositivo)
    device = ('%.2x' % intDispo)
    intFunc= int(funcion)
    function_code = ('%.2x' %intFunc)
    intDir=int(direccion)
    start_at_reg= ('%.4x' %intDir)
    intReg=int(registros)
    num_of_reg=('%.4x'%intReg)
    intBytes=int(registros*2)
    numBytes=('%.2x'%intBytes)
    read_device = device + function_code + start_at_reg + num_of_reg + numBytes
    i=0
    while(i<registros):
        read_device= read_device+valoresIngresados[i]
        i+=1
    crc = funcion03.calc(read_device)
    return (read_device+crc)

def conectarPuertoEnvia(puerto,baudrate,timeout):
    puertoEnvia.port=puerto
    puertoEnvia.baudrate=baudrate
    puertoEnvia.timeout=timeout
    puertoEnvia.open()
    puertoEnvia.is_open
    if(puertoEnvia.is_open):
        return True
    else:
        return False

def conectarPuertoRecibe(puerto,baudrate,timeout):
    puertoRecibe.port=puerto
    puertoRecibe.baudrate=baudrate
    puertoRecibe.timeout=timeout
    puertoRecibe.open()
    puertoRecibe.is_open
    if(puertoRecibe.is_open):
        return True
    else:
        return False

def desconectarPuertoEnvia():
    puertoEnvia.close()

def desconectarPuertoRecibe():
    puertoRecibe.close()

registros=input("Cantidad de registros a escribir: ")
conexion1=conectarPuertoEnvia("COM3",9600,1)
conexion2=conectarPuertoRecibe("COM4",9600,1)
if((conexion1==True) and (conexion2==True)):
    i=0
    valoresIngresados=[]
    while(i<registros):
        print("Registro numero %d:"%i)
        valor=int(input("Ingreso valor: "))
        valor=('%.4x'%valor)
        valoresIngresados.insert(i,valor)
        i+=1
    print("Resultados de la Funcion 16")
    trama=obtenerTrama()
    solicitud(trama)
    devolverValoresDecimal()
    devolverValoresHexadecimal()
    devolverValoresBinario()

    desconectarPuertoEnvia()
    desconectarPuertoRecibe()

    #11 10 9c42 0002 04 000c 000a

    #11 10 0000 0002 04 000a 0102

    #11 10 0001 0002