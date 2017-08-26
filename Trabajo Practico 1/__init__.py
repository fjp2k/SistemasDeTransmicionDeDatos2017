import serial
import binascii
import time
import math


cantidadRegistros=126
intentos = 3
segundos = 3
ser = serial.Serial()


def comunicacionPuerto(dispositivo,funcion,direccion,cantidad):
    serialEnviado = '01030000007ec5ea'
    global ser
    ser.write(binascii.unhexlify(serialEnviado))
    #serialObtenido = ser.read(len(serialEnviado))


    #if (len(serialObtenido) == (5 + cantidad * 2)):
    #mensaje = binascii.hexlify(serialObtenido)
    mensaje=binascii.hexlify(ser.read(5+cantidad*2))
        # conversion=bytearray.fromhex(mensaje)
    print("Mensaje devuelto: %s" % mensaje)
    datosConvertir = mensaje[6:mensaje.__len__() - 4]
    i = 0
    while (i < datosConvertir.__len__()):
        conversion = int(datosConvertir[i:i + 4], 16)
        print("Traduccion: %d" % conversion)
        i = i + 4

    # else:
    #     global intentos
    #     intentos = intentos - 1
    #     global segundos
    #     print("Intentos restantes: %d" % intentos)
    #     print('Proximo intento en: %d' % segundos)
    #     time.sleep(3)

def conexionPuerto(puerto,baudrate,timeout):
    ser.port = "COM4"
    ser.baudrate = 9600
    ser.timeout = 1
    ser.open()
    conexion = ser.is_open
    if(conexion):
        print("Conexion exitosa")
    else:
        print("No se pudo establecer conexion")

conexionPuerto(1,2,3)
while(intentos>0):
    if(cantidadRegistros<=125):
        comunicacionPuerto(dispositivo=01,funcion=03,direccion=0000,cantidad=cantidadRegistros)
        time.sleep(1000000)
    else:
        totalPedidos=cantidadRegistros*2
        iteraciones = math.ceil(totalPedidos/250)
        registros=125
        registrosRecorridos=0
        i=1
        while(i<=iteraciones):
            if(i!=iteraciones):
                i += 1
                comunicacionPuerto(dispositivo=01,funcion=03,direccion=registrosRecorridos,cantidad=registros)
                registrosRecorridos += 125
                time.sleep(2)
            else:
                registrosRestantes=cantidadRegistros-registrosRecorridos
                comunicacionPuerto(dispositivo=01,funcion=03,direccion=registrosRecorridos,cantidad=registrosRestantes)
                time.sleep(2)


ser.close()
exit();
