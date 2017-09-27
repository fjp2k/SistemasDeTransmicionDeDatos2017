import binascii
import serial
import funcion03

puertoEnvia=serial.Serial()
puertoRecibe=serial.Serial()
dispositivo=01
funcion=06
direccion=0012
#valor=15

def solicitud():
    tramaEnvia=funcion03.obtenerTrama(dispositivo,funcion,direccion,valor)
    print("\tTrama enviada: %s" %tramaEnvia)
    resultado = puertoEnvia.write(binascii.unhexlify(tramaEnvia))
    devolucion = binascii.hexlify(puertoRecibe.read(resultado))
    print("\tTrama devuelta: %s" %devolucion)

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

def convertirBinario():
    return bin(valor)

def convertirDecimal():
    return int(valor)

def convertirHexadecimal():
    return hex(valor)

def desconectarPuertoEnvia():
    puertoEnvia.close()

def desconectarPuertoRecibe():
    puertoRecibe.close()

#empieza
registros=input("Cantidad de registros a escribir: ")
conexion1=conectarPuertoEnvia("COM3",9600,1)
conexion2=conectarPuertoRecibe("COM4",9600,1)
if((conexion1==True) and (conexion2==True)):
    print("Resultados de la Funcion 06")
    i=1
    while(i<=registros):
        print("Registro numero %d:"%i)
        valor=input("Ingreso valor: ")
        solicitud()
        print("\tValor en binario: %s" %(convertirBinario()))
        print("\tValor en decimal: %s" % (convertirDecimal()))
        print("\tValor en hexadecimal: %s" % (convertirHexadecimal()))
        i+=1
    desconectarPuertoEnvia()
    desconectarPuertoRecibe()


