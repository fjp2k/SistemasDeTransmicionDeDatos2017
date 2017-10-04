import socket
import errorController

import binascii

ip = 0
puerto = 0
sock = 0
transaction = 1
BUFFER_SIZE = 1024
datosImprimir=[]
datosBinarios=[]
datosDecimal=[]
datosHexadecimal=[]

def configurarSocket(ipIngresada,puertoIngresado):
    global ip
    ip = ipIngresada

    global puerto
    puerto = puertoIngresado

def conectarSocket():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((ip, puerto))
        print("conexion exitosa")
        return True

    except Exception as e:
        print("no se pudo conectar")
        return False

def cerrarSocket():
    global sock
    sock.close()


def armarHeaderFuncion16(direccionRecibida,cantVariablesRecibidas,valores,dispositivoRecibido):
    global transaction
    transaction += 1
    intTransactionId = int(transaction)
    intProtocolId = 0000

    cantBytes = cantVariablesRecibidas * 2
    intMessageLength = 7 + cantBytes
    print("Longitud a leer: %s" %intMessageLength)
    intUnitId = int(dispositivoRecibido)

    transactionId = ('%.4x' % intTransactionId)
    protocolId = ('%.4x' % intProtocolId)
    messageLength = ('%.4x' % intMessageLength)
    unitId = ('%.2x' % intUnitId)
    headerTCP= transactionId + protocolId + messageLength + unitId
    armarTramaFuncion16(headerTCP,direccionRecibida,cantVariablesRecibidas,valores)


def armarTramaFuncion16(headerTCP,direccionRecibida,cantVariablesRecibidas,valores):
    intFunctionCode= 16
    intAddress = int(direccionRecibida)
    intTotalRegister = int(cantVariablesRecibidas)

    functionCode = ('%.2x' % intFunctionCode)
    address = ('%.4x' % intAddress)
    totalRegister = ('%.4x' % intTotalRegister)
    intCantBytes = cantVariablesRecibidas * 2
    cantBytes = ('%.2x' % intCantBytes)

    tramaTCP = headerTCP + functionCode + address +totalRegister + cantBytes

    for i in valores.__len__():
        tramaTCP = tramaTCP + valores(i)


    enviarTramaTCP(tramaTCP)

def enviarTramaTCP(tramaTCP):
    global sock
    global BUFFER_SIZE

    #request = struct.pack(tramaTCP)
    request = tramaTCP


    sock.send(binascii.unhexlify(request))
    print("Request: %s" %request)

    received = sock.recv(BUFFER_SIZE)
    received = binascii.hexlify(received).decode()
    print("Received: %s " %received)


    verificar = received[received.__len__()-6:]

    print("Verificar: %s" %verificar)

    error = errorController.controlar_trama(verificar)

    print("Error: %r" %error)

    if(error==True):
        generarContenido(received)
        print("datos imprimir: %s" %datosImprimir)
        imprimirBinario()
        imprimirDecimal()
        imprimirHexadecimal()
    else:
        errorDescription = errorController.obtener_error(verificar)
        print("Error: %s" %errorDescription)



def generarContenido(received):
    global datosImprimir
    datosImprimir = received[20:]

def imprimirBinario():
    i = 0
    while (i < datosImprimir.__len__()):
        conversion = int(datosImprimir[i:i + 4], 16)
        datosBinarios.append(bin(conversion))
        i = i + 4

    print("DATOS BINARIOS")
    i=0
    while (i < datosBinarios.__len__()):
        print("Direccion %d: %s" %(i,datosBinarios[i]) )
        i = i + 1


def imprimirHexadecimal():
    i = 0
    while (i < datosImprimir.__len__()):
        conversion = int(datosImprimir[i:i + 4], 16)
        datosHexadecimal.append(hex(conversion))
        i = i + 4

    print("DATOS HEZADECIMAL")
    i = 0
    while (i < datosHexadecimal.__len__()):
        print("Direccion %d: %s" % (i, datosHexadecimal[i]))
        i = i + 1

def imprimirDecimal():
    i = 0
    while (i < datosImprimir.__len__()):
        conversion = int(datosImprimir[i:i + 4], 16)
        datosDecimal.append(conversion)
        i = i + 4

    i = 0
    print("DATOS DECIMAL")
    while (i < datosDecimal.__len__()):
        print("Direccion %d: %s" % (i, datosDecimal[i]))
        i = i + 1

configurarSocket("127.0.0.1",502)
if(conectarSocket()):
    armarHeaderFuncion16(500,4,[1,2,3,4],1)
else:
    print("todo mal")

