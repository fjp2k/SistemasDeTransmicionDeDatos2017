import serial
import funcion03

puertoEnvia=serial.Serial()
puertoRecibe=serial.Serial()
dispositivo=01
funcion=06
direccion=0000
registos=0001

def solicitud():
    puertoEnvia.port="COM4"
    puertoEnvia.baudrate=9600
    puertoEnvia.timeout=1
    puertoEnvia.open()
    if(puertoEnvia.is_open):
        print "que onda"
        generarTrama()


def generarTrama():
    dispositivoTrama=('%.2x'%dispositivo)
    funcionTrama=('%.2x'%funcion)
    direccionTrama=('%.4x'%direccion)
    registrosTrama=('%.4x'%registos)
    print("estamos aca")

    tramaEnvia= funcion03.obtenerTrama(dispositivoTrama,funcionTrama,direccionTrama,registrosTrama)
    print(tramaEnvia)
solicitud()

