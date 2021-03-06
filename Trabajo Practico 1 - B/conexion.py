import serial
import binascii
import time
import math
import socket
import principal_support
import threading
from Tkinter import *
from errorController import *

class Conexion():

    def __init__(self, controlador):

        self.controlador = controlador
        self.ser = serial.Serial()

        self.puerto = ""
        self.baudrate = 0
        self.timeout = 0

        self.intentos = 0
        self.segundos = 3

        self.funcion = 0
        self.dispositivo = 0
        self.direccion = 0
        self.cantidadRegistros = 0
        self.variable1 = 0
        self.variable2 = 0
        self.variable3 = 0
        self.variable4 = 0

        self.trama = ''
        self.devolucion=""
        self.datosBinario = []
        self.datosHexadecimal = []
        self.datosDecimal = []
        self.datosConvertir=[]
        self.datosImprimir=[]
        self.descripcionError=""
        self.cantBytes=0
        #todo tcp

        self.ip = 0
        #usamos la misma variable de puerto tanto para tcp com serial
        self.sock = 0
        self.transaction = 1
        self.BUFFER_SIZE = 1024


    def conexion_puerto(self,puerto,baudrate,timeout):
        self.puerto = puerto
        self.baudrate = int(baudrate)
        self.timeout = float(timeout)

        try:
            self.ser.port = self.puerto
            self.ser.baudrate = self.baudrate
            self.ser.timeout = self.timeout
            self.ser.open()
            if (self.ser.is_open):
                return True
            else:
                return False
        except:
            return False

    def ejecutar_funcion03(self,intentos, dispositivo, direccion, cantidadRegistros):
        self.intentos = int(intentos)
        self.funcion = 3
        self.dispositivo = int(dispositivo)
        self.direccion = int(direccion)
        self.cantidadRegistros = int(cantidadRegistros)

        self.obtenerRespuestas_funcion03()

    def obtenerRespuestas_funcion03(self):
        t1 = threading.Thread(target=self.obtenerRespuestas_funcion03_thread)
        t1.start()

    def obtenerRespuestas_funcion03_thread(self):
        llamada_exitosa = False
        while (self.intentos > 0):
            if (self.cantidadRegistros <= 125):
                print("Iteraciones: 1")
                tramaEnvio = self.obtenerTrama(self.dispositivo, self.funcion, self.direccion, self.cantidadRegistros)
                exitoComunicacion=self.comunicacionPuerto(tramaEnvio)
                print("exito: %s"%exitoComunicacion)
                if(exitoComunicacion):
                    print("Trama Solicitud: %s" % self.trama)
                    self.controlador.imprimir_trama_enviada(self.trama)
                    print("Trama devuelta: %s" % self.devolucion)
                    self.controlador.imprimir_trama_recibida(self.devolucion)
                    self.obtenerBinario(self.datosConvertir)
                    self.obtenerHexadecimal(self.datosConvertir)
                    self.obtenerDecimal(self.datosConvertir)
                    llamada_exitosa = True
                    break
                else:
                    self.intentos-=1
                    print("intentos restantes: %d"%self.intentos)
                    if(self.intentos==0):
                        print("se acabaron los intentos")
                        self.controlador.imprimir_error_llamada("No hay mas intentos disponibles",
                                                                self.descripcionError)
                        break
                #time.sleep(10)
            else:
                    totalPedidos = self.cantidadRegistros * 2
                    totalBytes = totalPedidos / float(250)
                    iteraciones = math.ceil(totalBytes)
                    print("Iteraciones: %d" % iteraciones)
                    registros = 125
                    registrosRecorridos = 0
                    i = 1
                    while (i <= iteraciones):
                        print("Iteracion: %d" % i)
                        if (i != iteraciones):
                            tramaEnviar = self.obtenerTrama(self.dispositivo, self.funcion, registrosRecorridos, registros)
                            exitoComunicacion = self.comunicacionPuerto(tramaEnviar)
                            if (exitoComunicacion):
                                i += 1
                                print("Trama Solicitud: %s" % self.trama)
                                self.controlador.imprimir_trama_enviada(self.trama)
                                print("Trama devuelta: %s" % self.devolucion)
                                self.controlador.imprimir_trama_recibida(self.devolucion)
                                self.obtenerBinario(self.datosConvertir)
                                self.obtenerHexadecimal(self.datosConvertir)
                                self.obtenerDecimal(self.datosConvertir)
                                registrosRecorridos += 125
                                time.sleep(2)
                            else:
                                self.intentos -= 1
                                print("intentos restantes: %d" % self.intentos)
                                if (self.intentos == 0):
                                    print("se acabaron los intentos")
                                    self.controlador.imprimir_error_llamada("No hay mas intentos disponibles",
                                                                            self.descripcionError)
                                    break

                        else:
                            registrosRestantes = self.cantidadRegistros - registrosRecorridos
                            tramaEnviar = self.obtenerTrama(self.dispositivo, self.funcion, registrosRecorridos,registrosRestantes)
                            exitoComunicacion = self.comunicacionPuerto(tramaEnviar)
                            time.sleep(2)
                            if (exitoComunicacion):
                                i += 1
                                print("Trama Solicitud: %s" % self.trama)
                                self.controlador.imprimir_trama_enviada(self.trama)
                                print("Trama devuelta: %s" % self.devolucion)
                                self.controlador.imprimir_trama_recibida(self.devolucion)
                                self.obtenerBinario(self.datosConvertir)
                                self.obtenerHexadecimal(self.datosConvertir)
                                self.obtenerDecimal(self.datosConvertir)
                                registrosRecorridos += 125
                                time.sleep(2)
                                llamada_exitosa = True
                                break
                            else:
                                self.intentos -= 1
                                print("intentos restantes: %d" % self.intentos)
                                if (self.intentos == 0):
                                    print("se acabaron los intentos")
                                    self.controlador.imprimir_error_llamada("No hay mas intentos disponibles",
                                                                            self.descripcionError)
                                    break
                                else:
                                    continue

            if llamada_exitosa:
                break


    def ejecutar_funcion06(self,intentos,dispositivo,direccion,variable):
        self.intentos = int(intentos)
        self.dispositivo = int(dispositivo)
        self.funcion = 6
        self.direccion = int(direccion)
        self.variable1 = int(variable)

        self.obtenerRespuestas_funcion06()


    def ejecutar_funcion16(self, intentos,registros,dispositivo, direccion,variable1,variable2,variable3=0,variable4=0):
        self.intentos = int(intentos)
        self.cantidadRegistros = int(registros)
        self.funcion = 16
        self.dispositivo = int(dispositivo)
        self.direccion = int(direccion)

        if(self.cantidadRegistros==2):
            self.variable1 = ('%.4x' % int(variable1))
            self.variable2 = ('%.4x' % int(variable2))
        if (self.cantidadRegistros == 3):
            self.variable1 = ('%.4x' % int(variable1))
            self.variable2 = ('%.4x' % int(variable2))
            self.variable3 = ('%.4x' % int(variable3))
        if (self.cantidadRegistros == 4):
            self.variable1 = ('%.4x' % int(variable1))
            self.variable2 = ('%.4x' % int(variable2))
            self.variable3 = ('%.4x' % int(variable3))
            self.variable4 = ('%.4x' % int(variable4))

        self.obtenerRespuestas_funcion16()

    def desconectarpuerto(self):
        self.ser.close()
        return True

    def obtenerRespuestas_funcion06(self):
        t1 = threading.Thread(target=self.obtenerRespuestas_funcion06_thread)
        t1.start()

    def obtenerRespuestas_funcion06_thread(self):
        while(self.intentos>0):
            tramaEnvio = self.obtenerTrama(self.dispositivo, self.funcion, self.direccion, self.variable1)
            exitoComunicacion=self.comunicacionPuerto(tramaEnvio)

            if (exitoComunicacion):
                print("Trama Solicitud: %s" % self.trama)
                self.controlador.imprimir_trama_enviada(self.trama)
                print("Trama devuelta: %s" % self.devolucion)
                self.controlador.imprimir_trama_recibida(self.devolucion)
                self.obtenerBinario(self.datosConvertir)
                self.obtenerHexadecimal(self.datosConvertir)
                self.obtenerDecimal(self.datosConvertir)
                break
            else:
                self.intentos -= 1
                print("intentos restantes: %d" % self.intentos)
                if (self.intentos == 0):
                    print("se acabaron los intentos")
                    self.controlador.imprimir_error_llamada("No hay mas intentos disponibles",
                                                            self.descripcionError)
                    break


    def obtenerRespuestas_funcion16(self):
        t1 = threading.Thread(target=self.obtenerRespuestas_funcion16_thread)
        t1.start()

    def obtenerRespuestas_funcion16_thread(self):
        while (self.intentos > 0):
            tramaEnvio = self.obtenerTrama(self.dispositivo, self.funcion, self.direccion, self.cantidadRegistros)
            exitoComunicacion=self.comunicacionPuerto(tramaEnvio)
            if (exitoComunicacion):
                print("Trama Solicitud: %s" % self.trama)
                self.controlador.imprimir_trama_enviada(self.trama)
                print("Trama devuelta: %s" % self.devolucion)
                self.controlador.imprimir_trama_recibida(self.devolucion)
                if (self.cantidadRegistros == 2):
                    self.datosConvertir = self.variable1 + self.variable2

                if (self.cantidadRegistros == 3):
                    self.datosConvertir = self.variable1 + self.variable2 + self.variable3

                if (self.cantidadRegistros == 4):
                    self.datosConvertir = self.variable1 + self.variable2 + self.variable3 + self.variable4
                self.obtenerBinario(self.datosConvertir)
                self.obtenerHexadecimal(self.datosConvertir)
                self.obtenerDecimal(self.datosConvertir)
                break
            else:
                self.intentos -= 1
                print("intentos restantes: %d" % self.intentos)
                if (self.intentos == 0):
                    print("se acabaron los intentos")
                    self.controlador.imprimir_error_llamada("No hay mas intentos disponibles",
                                                            self.descripcionError)
                    break


    def obtenerTrama(self, dispositivo, funcion, direccion, registros):
        intDispo = int(dispositivo)
        device = ('%.2x' % intDispo)
        intFunc = int(funcion)
        function_code = ('%.2x' % intFunc)
        intDir = int(direccion)
        start_at_reg = ('%.4x' % intDir)
        intReg = int(registros)
        num_of_reg = ('%.4x' % intReg)

        read_device = device + function_code + start_at_reg + num_of_reg
        if(self.funcion==16):
            intBytes = int(registros * 2)
            numBytes = ('%.2x' % intBytes)
            if(registros==2):
                read_device = device + function_code + start_at_reg + num_of_reg + numBytes + self.variable1 + self.variable2
            if(registros==3):
                read_device = device + function_code + start_at_reg + num_of_reg + numBytes + self.variable1 + self.variable2 +self.variable3
            if(registros==4):
                read_device = device + function_code + start_at_reg + num_of_reg + numBytes + self.variable1 + self.variable2 +self.variable3 +self.variable4
        crc = self.calc(read_device)
        return (read_device + crc)

    def calc(self, data):
        crc_tab16 = [0X0000, 0XC0C1, 0XC181, 0X0140, 0XC301, 0X03C0, 0X0280, 0XC241,
                         0XC601, 0X06C0, 0X0780, 0XC741, 0X0500, 0XC5C1, 0XC481, 0X0440,
                         0XCC01, 0X0CC0, 0X0D80, 0XCD41, 0X0F00, 0XCFC1, 0XCE81, 0X0E40,
                         0X0A00, 0XCAC1, 0XCB81, 0X0B40, 0XC901, 0X09C0, 0X0880, 0XC841,
                         0XD801, 0X18C0, 0X1980, 0XD941, 0X1B00, 0XDBC1, 0XDA81, 0X1A40,
                         0X1E00, 0XDEC1, 0XDF81, 0X1F40, 0XDD01, 0X1DC0, 0X1C80, 0XDC41,
                         0X1400, 0XD4C1, 0XD581, 0X1540, 0XD701, 0X17C0, 0X1680, 0XD641,
                         0XD201, 0X12C0, 0X1380, 0XD341, 0X1100, 0XD1C1, 0XD081, 0X1040,
                         0XF001, 0X30C0, 0X3180, 0XF141, 0X3300, 0XF3C1, 0XF281, 0X3240,
                         0X3600, 0XF6C1, 0XF781, 0X3740, 0XF501, 0X35C0, 0X3480, 0XF441,
                         0X3C00, 0XFCC1, 0XFD81, 0X3D40, 0XFF01, 0X3FC0, 0X3E80, 0XFE41,
                         0XFA01, 0X3AC0, 0X3B80, 0XFB41, 0X3900, 0XF9C1, 0XF881, 0X3840,
                         0X2800, 0XE8C1, 0XE981, 0X2940, 0XEB01, 0X2BC0, 0X2A80, 0XEA41,
                         0XEE01, 0X2EC0, 0X2F80, 0XEF41, 0X2D00, 0XEDC1, 0XEC81, 0X2C40,
                         0XE401, 0X24C0, 0X2580, 0XE541, 0X2700, 0XE7C1, 0XE681, 0X2640,
                         0X2200, 0XE2C1, 0XE381, 0X2340, 0XE101, 0X21C0, 0X2080, 0XE041,
                         0XA001, 0X60C0, 0X6180, 0XA141, 0X6300, 0XA3C1, 0XA281, 0X6240,
                         0X6600, 0XA6C1, 0XA781, 0X6740, 0XA501, 0X65C0, 0X6480, 0XA441,
                         0X6C00, 0XACC1, 0XAD81, 0X6D40, 0XAF01, 0X6FC0, 0X6E80, 0XAE41,
                         0XAA01, 0X6AC0, 0X6B80, 0XAB41, 0X6900, 0XA9C1, 0XA881, 0X6840,
                         0X7800, 0XB8C1, 0XB981, 0X7940, 0XBB01, 0X7BC0, 0X7A80, 0XBA41,
                         0XBE01, 0X7EC0, 0X7F80, 0XBF41, 0X7D00, 0XBDC1, 0XBC81, 0X7C40,
                         0XB401, 0X74C0, 0X7580, 0XB541, 0X7700, 0XB7C1, 0XB681, 0X7640,
                         0X7200, 0XB2C1, 0XB381, 0X7340, 0XB101, 0X71C0, 0X7080, 0XB041,
                         0X5000, 0X90C1, 0X9181, 0X5140, 0X9301, 0X53C0, 0X5280, 0X9241,
                         0X9601, 0X56C0, 0X5780, 0X9741, 0X5500, 0X95C1, 0X9481, 0X5440,
                         0X9C01, 0X5CC0, 0X5D80, 0X9D41, 0X5F00, 0X9FC1, 0X9E81, 0X5E40,
                         0X5A00, 0X9AC1, 0X9B81, 0X5B40, 0X9901, 0X59C0, 0X5880, 0X9841,
                         0X8801, 0X48C0, 0X4980, 0X8941, 0X4B00, 0X8BC1, 0X8A81, 0X4A40,
                         0X4E00, 0X8EC1, 0X8F81, 0X4F40, 0X8D01, 0X4DC0, 0X4C80, 0X8C41,
                         0X4400, 0X84C1, 0X8581, 0X4540, 0X8701, 0X47C0, 0X4680, 0X8641,
                         0X8201, 0X42C0, 0X4380, 0X8341, 0X4100, 0X81C1, 0X8081, 0X4040]
        crc = 0xFFFF
        a = 0
        while a < len(data):
            crc = (crc >> 8) ^ crc_tab16[(crc ^ int(data[a:a + 2], 16)) & 0x00FF]
            a += 2
        crc = hex(crc)[2:]
        while len(crc) < 4:
            crc = "0" + crc
        return crc[2:] + crc[:2]


    def comunicacionPuerto(self,trama):
        self.trama = trama
        resultado=self.ser.write(binascii.unhexlify(self.trama))
        if(self.funcion==3):
            self.devolucion = binascii.hexlify(self.ser.read(5+self.cantidadRegistros*2))
            llamadaExitosa=self.verificarTrama(self.devolucion)
            if(llamadaExitosa==False):
                return False
            else:
                llamadaExitosa=controlar_trama(self.devolucion)
                if(llamadaExitosa):
                    return True
                else:
                    self.descripcionError=obtener_error(self.devolucion)
                    return False


        if(self.funcion==6):
            self.devolucion = binascii.hexlify(self.ser.read(resultado))
            llamadaExitosa = self.verificarTrama(self.devolucion)
            if (llamadaExitosa == False):
                return False
            else:
                llamadaExitosa = controlar_trama(self.devolucion)
                if (llamadaExitosa):
                    return True
                else:
                    print("estamos aca")
                    self.descripcionError = obtener_error(self.devolucion)
                    return False

        if(self.funcion==16):
            self.devolucion = binascii.hexlify(self.ser.read(8))
            llamadaExitosa = self.verificarTrama(self.devolucion)
            if (llamadaExitosa == False):
                return False
            else:
                llamadaExitosa = controlar_trama(self.devolucion)
                if (llamadaExitosa):
                    return True
                else:
                    self.descripcionError = obtener_error(self.devolucion)
                    return False

    def verificarTrama(self,devolucion):

        igualdad = self.verficarCrc(devolucion)
        print(igualdad)
        if (igualdad):
                self.datosConvertir = devolucion[6:devolucion.__len__() - 4]
                print("Crc de respuesta correcto")
                return True
        else:
                print("Error crc distintos")
                return False


    def verficarCrc(self,devolucion):
        crc1=devolucion[devolucion.__len__()-4:devolucion.__len__()]
        sinCrc=devolucion[0:devolucion.__len__()-4]
        crc2=self.calc(sinCrc)
        print(crc1)
        print(crc2)
        if(crc1==crc2):
            return True
        else:
            return False


    def obtenerBinario(self,datosConvertir):
        i=0
        while (i < datosConvertir.__len__()):
            conversion = int(datosConvertir[i:i + 4], 16)
            self.datosBinario.append(bin(conversion))
            i = i + 4


    def obtenerHexadecimal(self,datosConvertir):
        i=0
        while (i < datosConvertir.__len__()):
            conversion = int(datosConvertir[i:i + 4], 16)
            self.datosHexadecimal.append(hex(conversion))
            i = i + 4


    def obtenerDecimal(self,datosConvertir):
        i = 0
        while (i < datosConvertir.__len__()):
            conversion = int(datosConvertir[i:i + 4], 16)
            self.datosDecimal.append(conversion)
            i = i + 4


#TODO TCP

    def conectarTCP(self, ip, puerto, intentos):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(10)
        self.intentos = int(intentos)
        try:
            self.sock.connect((ip, int(puerto)))
            print("conexion tcp exitosa")
            return True

        except Exception as e:
            print("no se pudo conectar tcp")
            print(e);
            return False

    def cerrarConexionTCP(self):
        self.sock.close()
        return True

    def ejecutar_funcion_tcp(self,dispositivoRecibido,direccionRecibida,cantVariablesRecibidas,funcionRecibida,variable1=0,variable2=0,variable3=0,variable4=0):
            try:
                self.transaction += 1
                intTransactionId = int(self.transaction)
                intProtocolId = 0000
                if(funcionRecibida=="16"):
                    self.cantidadRegistros=int(cantVariablesRecibidas)
                    self.cantBytes = int(cantVariablesRecibidas) * 2
                    print(self.cantBytes)
                    intMessageLength = 7 + self.cantBytes
                    print("message: %s"%intMessageLength)
                    if (cantVariablesRecibidas == "2"):
                        self.variable1 = ('%.4x' % int(variable1))
                        self.variable2 = ('%.4x' % int(variable2))
                    if (cantVariablesRecibidas == "3"):
                        self.variable1 = ('%.4x' % int(variable1))
                        self.variable2 = ('%.4x' % int(variable2))
                        self.variable3 = ('%.4x' % int(variable3))
                    if (cantVariablesRecibidas == "4"):
                        self.variable1 = ('%.4x' % int(variable1))
                        self.variable2 = ('%.4x' % int(variable2))
                        self.variable3 = ('%.4x' % int(variable3))
                        self.variable4 = ('%.4x' % int(variable4))
                else:
                    intMessageLength = 0006

                intUnitId = int(dispositivoRecibido)
                transactionId = ('%.4x' % intTransactionId)
                protocolId = ('%.4x' % intProtocolId)
                messageLength = ('%.4x' % intMessageLength)
                unitId = ('%.2x' % intUnitId)
                headerTCP = transactionId + protocolId + messageLength + unitId
                print("HEADER TCP: %s"%headerTCP)
                if(funcionRecibida=="3"):
                    self.obtenerRespuestas_funcion03_tcp(headerTCP, direccionRecibida, cantVariablesRecibidas,funcionRecibida)
                else:
                    tramaEnviada=self.armarTramaFuncion(headerTCP, direccionRecibida, cantVariablesRecibidas,funcionRecibida)
                    comunicacion = self.enviarTramaTCP(tramaEnviada)
                    if (comunicacion):
                        #la trama y la devoluacion fue seteada en la funcion enviarTramaTCP
                        print("Trama Solicitud: %s" % self.trama)
                        self.controlador.imprimir_trama_enviada(self.trama)
                        print("Trama devuelta: %s" % self.devolucion)
                        self.controlador.imprimir_trama_recibida(self.devolucion)
                        self.generarContendio(self.devolucion)
                    else:
                        self.controlador.imprimir_error_llamada("Se ha producido un error: ",self.descripcionError)
            except Exception as e:
                print (e)
                self.controlador.imprimir_error_llamada("Error no se pudo completar la conexion ",e.message)

    def armarTramaFuncion(self,headerTCP,direccionRecibida,cantVariablesRecibidas,funcionRecibida):
        if(funcionRecibida=="3"):
            self.funcion=03

        if(funcionRecibida=="6"):
            self.funcion=06

        if(funcionRecibida=="16"):
            self.funcion=16
            intCantBytes = ('%.2x' % self.cantBytes)

            intFunctionCode = self.funcion
            intAddress = int(direccionRecibida)
            intTotalRegister = int(cantVariablesRecibidas)

            functionCode = ('%.2x' % intFunctionCode)
            address = ('%.4x' % intAddress)
            totalRegister = ('%.4x' % intTotalRegister)

            tramaTCP = headerTCP + functionCode + address + totalRegister + intCantBytes

            if(cantVariablesRecibidas=="2"):
                tramaTCP = headerTCP + functionCode + address + totalRegister + intCantBytes + self.variable1 + self.variable2

            if (cantVariablesRecibidas == "3"):
                tramaTCP = headerTCP + functionCode + address + totalRegister + intCantBytes + self.variable1 + self.variable2 + self.variable3

            if (cantVariablesRecibidas == "4"):
                tramaTCP = headerTCP + functionCode + address + totalRegister + intCantBytes + self.variable1 + self.variable2 + self.variable3 + self.variable4

            return tramaTCP

        else:
            intFunctionCode= self.funcion
            intAddress = int(direccionRecibida)
            intTotalRegister = int(cantVariablesRecibidas)

            functionCode = ('%.2x' % intFunctionCode)
            address = ('%.4x' % intAddress)
            totalRegister = ('%.4x' % intTotalRegister)

            tramaTCP = headerTCP + functionCode + address + totalRegister
            print("TRAMA TCP: %s" %tramaTCP)
            return tramaTCP



    def enviarTramaTCP(self,tramaTCP):

        self.trama = tramaTCP
        self.sock.send(binascii.unhexlify(self.trama))
        print("Request: %s" % self.trama)

        self.devolucion = self.sock.recv(self.BUFFER_SIZE)
        self.devolucion = binascii.hexlify(self.devolucion).decode()
        print("Received: %s " % self.devolucion)

        #PASAMOS LOS ULTIMOS SEIS BIT RECIBIDOS PORQUE SIEMPRE ENTRE ESOS SEIS SE ENCUENTRA EL ERROR
        verificarError = self.devolucion[self.devolucion.__len__() - 6:]
        print("Verificar: %s" % verificarError)

        noExisteEerror = controlar_trama(verificarError)
        print("Error: %r" % noExisteEerror)

        if (noExisteEerror == True):
            return True

        else:
            self.descripcionError= obtener_error(verificarError)
            return False


    def generarContendio(self,received):

        if(self.funcion==03):

            self.datosImprimir = received[18:]

        if(self.funcion==06):
            self.datosImprimir = received[20:]

        if(self.funcion==16):
            if(self.cantidadRegistros==2):
                self.datosImprimir = self.variable1+self.variable2

            if (self.cantidadRegistros == 3):
                self.datosImprimir = self.variable1+self.variable2+self.variable3

            if (self.cantidadRegistros == 4):
                self.datosImprimir = self.variable1 + self.variable2 + self.variable3+ self.variable4

        self.obtenerBinario(self.datosImprimir)
        self.obtenerDecimal(self.datosImprimir)
        self.obtenerHexadecimal(self.datosImprimir)


    def obtenerRespuestas_funcion03_tcp(self,headerTCP, direccionRecibida, cantVariablesRecibidas,funcionRecibida):
        t1 = threading.Thread(target=self.obtenerRespuestas_funcion03_tcp_thread(headerTCP, direccionRecibida, cantVariablesRecibidas,funcionRecibida))
        t1.start()

    def obtenerRespuestas_funcion03_tcp_thread(self,headerTCP, direccionRecibida, cantVariablesRecibidas,funcionRecibida):
        self.cantidadRegistros=int(cantVariablesRecibidas)
        llamada_exitosa = False
        while (self.intentos > 0):
            if (self.cantidadRegistros <= 125):
                print("Iteraciones: 1")
                tramaEnvio = self.armarTramaFuncion(headerTCP, direccionRecibida, cantVariablesRecibidas,funcionRecibida)
                exitoComunicacion=self.enviarTramaTCP(tramaEnvio)
                print("exito: %s"%exitoComunicacion)
                if(exitoComunicacion):
                    print("Trama Solicitud: %s" % self.trama)
                    self.controlador.imprimir_trama_enviada(self.trama)
                    print("Trama devuelta: %s" % self.devolucion)
                    self.controlador.imprimir_trama_recibida(self.devolucion)
                    self.generarContendio(self.devolucion)
                    break
                else:
                    self.intentos-=1
                    print("intentos restantes: %d"%self.intentos)
                    if(self.intentos==0):
                        print("se acabaron los intentos")
                        self.controlador.imprimir_error_llamada("No hay mas intentos disponibles",
                                                                self.descripcionError)
                        break
                time.sleep(5)
            else:
                    totalPedidos = self.cantidadRegistros * 2
                    totalBytes = totalPedidos / float(250)
                    iteraciones = math.ceil(totalBytes)
                    print("Iteraciones: %d" % iteraciones)
                    registros = 125
                    registrosRecorridos = 0
                    i = 1
                    while (i <= iteraciones):
                        print("Iteracion: %d" % i)
                        if (i != iteraciones):
                            tramaEnviar = self.armarTramaFuncion(headerTCP, registrosRecorridos, registros,funcionRecibida)
                            exitoComunicacion = self.enviarTramaTCP(tramaEnviar)
                            if (exitoComunicacion):
                                i += 1
                                print("Trama Solicitud: %s" % self.trama)
                                self.controlador.imprimir_trama_enviada(self.trama)
                                print("Trama devuelta: %s" % self.devolucion)
                                self.controlador.imprimir_trama_recibida(self.devolucion)
                                self.generarContendio(self.devolucion)
                                registrosRecorridos += 125
                                time.sleep(2)
                            else:
                                self.intentos -= 1
                                print("intentos restantes: %d" % self.intentos)
                                if (self.intentos == 0):
                                    print("se acabaron los intentos")
                                    self.controlador.imprimir_error_llamada("No hay mas intentos disponibles",
                                                                            self.descripcionError)
                                    break

                        else:
                            registrosRestantes = self.cantidadRegistros - registrosRecorridos
                            tramaEnviar = self.armarTramaFuncion(headerTCP, registrosRecorridos, registrosRestantes,funcionRecibida)
                            exitoComunicacion = self.enviarTramaTCP(tramaEnviar)
                            time.sleep(2)
                            if (exitoComunicacion):
                                i += 1
                                print("Trama Solicitud: %s" % self.trama)
                                self.controlador.imprimir_trama_enviada(self.trama)
                                print("Trama devuelta: %s" % self.devolucion)
                                self.controlador.imprimir_trama_recibida(self.devolucion)
                                self.generarContendio(self.devolucion)
                                registrosRecorridos += 125
                                time.sleep(2)
                                llamada_exitosa = True
                                break
                            else:
                                self.intentos -= 1
                                print("intentos restantes: %d" % self.intentos)
                                if (self.intentos == 0):
                                    print("se acabaron los intentos")
                                    self.controlador.imprimir_error_llamada("No hay mas intentos disponibles",
                                                                            self.descripcionError)
                                    break
                                else:
                                    continue

            if llamada_exitosa:
                break
