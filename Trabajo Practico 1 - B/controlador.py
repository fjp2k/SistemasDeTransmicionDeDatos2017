from conexion import Conexion

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


class Controlador:

    def __init__(self, gui):

        self.gui = gui
        self.conexion = Conexion(self.gui)

        self.tipo_conexion_seleccionada = IntVar()
        self.list_box_error_index = 1

    # Configuracion Extra GUI

    def configurar_gui(self):

        # Radio buttons
        self.gui.puertoSerialRB.config(variable=self.tipo_conexion_seleccionada, value=1)
        self.gui.tcpRB.config(variable=self.tipo_conexion_seleccionada, value=2)

        # Botones Conexion
        self.dibujar_estado_desconectado()

        # Entries Configuracion Puerto Serie
        self.gui.puertoSerialEntry.config(state=DISABLED)
        self.gui.timeoutEntry.config(state=DISABLED)
        self.gui.baudiosEntry.config(state=DISABLED)
        self.gui.intentosEntry.config(state=DISABLED)

        # Entries Configuracion TCP
        self.gui.direccionIPEntry.config(state=DISABLED)
        self.gui.puertoTCPEntry.config(state=DISABLED)

    # Accion botones

    def seleccionar_puerto_serial(self):
        # Entries Configuracion Puerto Serie
        self.gui.puertoSerialEntry.config(state=NORMAL)
        self.gui.timeoutEntry.config(state=NORMAL)
        self.gui.baudiosEntry.config(state=NORMAL)
        self.gui.intentosEntry.config(state=NORMAL)

        # Entries Configuracion TCP
        self.gui.direccionIPEntry.config(state=DISABLED)
        self.gui.puertoTCPEntry.config(state=DISABLED)

    def seleccionar_tcp(self):
        # Entries Configuracion Puerto Serie
        self.gui.puertoSerialEntry.config(state=DISABLED)
        self.gui.timeoutEntry.config(state=DISABLED)
        self.gui.baudiosEntry.config(state=DISABLED)
        self.gui.intentosEntry.config(state=DISABLED)

        # Entries Configuracion TCP
        self.gui.direccionIPEntry.config(state=NORMAL)
        self.gui.puertoTCPEntry.config(state=NORMAL)

    def conectar(self):

        self.limpiar_resultados()

        if self.tipo_conexion_seleccionada.get() == 0:
            self.dibujar_estado_desconectado()
            self.gui.valorEstadoConexionLb.config(text='Elegir tipo conexion')
        else:
            if self.verificar_datos():
                conectado = False
                if self.tipo_conexion_seleccionada.get() == 1:
                    conectado = self.conectar_puerto_serie()
                elif self.tipo_conexion_seleccionada.get() == 2:
                    conectado = self.conectar_tcp()

                if conectado:
                    self.dibujar_estado_conectado()
                    if self.tipo_conexion_seleccionada.get() == 1:
                        self.ejecutar_funcion_puerto_serie()
                    elif self.tipo_conexion_seleccionada.get() == 2:
                        self.ejecutar_funcion_tcp()
                else:
                    self.dibujar_estado_desconectado()
                    if self.tipo_conexion_seleccionada.get() == 0:
                        self.gui.valorEstadoConexionLb.config(text='Elegir tipo conexion')
                    else:
                        self.gui.valorEstadoConexionLb.config(text='Error al conectar')
            else:
                self.dibujar_estado_desconectado()
                self.gui.valorEstadoConexionLb.config(text='Datos ingresados son incorrectos')

    def convertir_binario(self):
        self.conexion.imprimirRespuesta(self.conexion.datosBinario)

    def convertir_decimal(self):
        self.conexion.imprimirRespuesta(self.conexion.datosDecimal)

    def convertir_hexadecimal(self):
        self.conexion.imprimirRespuesta(self.conexion.datosHexadecimal)

    def desconectar(self):
        desconectar = self.conexion.desconectarpuerto()

        if desconectar:
            self.dibujar_estado_desconectado()
            self.limpiar_resultados()

            self.gui.valorEstadoConexionLb.config(text='Desconectado')

    # Metodos conexion

    def conectar_puerto_serie(self):
        print "Conectar por puerto serie"
        return self.conexion.conexion_puerto(puerto=self.gui.puertoEntry.get(),
                                             baudrate=self.gui.baudiosEntry.get(),
                                             timeout=self.gui.timeoutEntry.get())

    def conectar_tcp(self):
        print "Conectar por TCP"
        # TODO llamar funcion
        return False

    # Metodos ejecucion funcion

    def ejecutar_funcion_puerto_serie(self):
        funcion = self.gui.funcionCombo.get()
        self.gui.valorEstadoConexionLb.config(text='Conectado por puerto serie')
        if funcion == "3":
            print "Ejecutar funcion 03 por puerto serie"
            self.conexion.ejecutar_funcion03(intentos=self.gui.intentosEntry.get(),
                                             dispositivo=self.gui.dispositivoEntry.get(),
                                             direccion=self.gui.direccionInicialEntry.get(),
                                             cantidadRegistros=self.gui.cantidadVariablesEntry.get())
        if funcion == "6":
            print "Ejecutar funcion 06 por puerto serie"
            self.conexion.ejecutar_funcion06(intentos=self.gui.intentosEntry.get(),
                                             dispositivo=self.gui.dispositivoEntry.get(),
                                             direccion=self.gui.direccionInicialEntry.get(),
                                             variable=self.gui.variable1Entry.get())

        if funcion == "16":
            print "Ejecutar funcion 16 por puerto serie"
            self.conexion.ejecutar_funcion16(intentos=self.gui.intentosEntry.get(),
                                             registros=self.gui.cantidadVariablesEntry.get(),
                                             dispositivo=self.gui.dispositivoEntry.get(),
                                             direccion=self.gui.direccionInicialEntry.get(),
                                             variable1=self.gui.variable1Entry.get(),
                                             variable2=self.gui.variable2Entry.get(),
                                             variable3=self.gui.variable3Entry.get(),
                                             variable4=self.gui.variable4Entry.get())

    def ejecutar_funcion_tcp(self):
        funcion = self.gui.funcionCombo.get()
        self.gui.valorEstadoConexionLb.config(text='Conectado por TCP')
        if funcion == "3":
            print "Ejecutar funcion 03 por TCP"
            # TODO Llamar funcion

        if funcion == "6":
            print "Ejecutar funcion 06 por TCP"
            # TODO Llamar funcion

        if funcion == "16":
            print "Ejecutar funcion 16 por TCP"
            # TODO Llamar funcion

    # Metodos Util

    def limpiar_resultados(self):
        self.gui.tramasSolicitudListBox.delete(0, END)
        self.gui.tramasRespuestaListBox.delete(0, END)
        self.gui.respuestaListBox.delete(0, END)

        self.conexion.datosDecimal = []
        self.conexion.datosHexadecimal = []
        self.conexion.datosBinario = []

    def dibujar_estado_conectado(self):
        self.gui.conectarBtn.config(state=DISABLED)
        self.gui.desconectarBtn.config(state=NORMAL)

    def dibujar_estado_desconectado(self):
        self.gui.conectarBtn.config(state=NORMAL)
        self.gui.desconectarBtn.config(state=DISABLED)

    # Metodos vericacion

    def verificar_datos(self):

        self.limpiar_resultados()
        self.list_box_error_index = 1

        datos_correctos = True

        if self.tipo_conexion_seleccionada.get() == 1:
            datos_correctos = self.verificar_datos_puerto_serie(datos_correctos)

        elif self.tipo_conexion_seleccionada.get() == 2:
            datos_correctos = self.verificar_datos_tcp(datos_correctos)

        return self.verificar_datos_llamada(datos_correctos)

    def verificar_datos_puerto_serie(self, datos_correctos):
        print "Verificar datos puerto serie"

        if self.gui.puertoSerialEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Puerto incorrecto")
            self.list_box_error_index = self.list_box_error_index + 1

        if self.gui.timeoutEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Timeout incorrecto")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not self.gui.timeoutEntry.get().isdigit():
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Timeout incorrecto")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not isinstance(int(self.gui.timeoutEntry.get()), (int, long)):
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Timeout incorrecto")
            self.list_box_error_index = self.list_box_error_index + 1

        if self.gui.baudiosEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Baudios incorrectos")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not self.gui.baudiosEntry.get().isdigit():
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Baudios incorrectos")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not isinstance(int(self.gui.baudiosEntry.get()), (int, long)):
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Baudios incorrectos")
            self.list_box_error_index = self.list_box_error_index + 1

        if self.gui.intentosEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Cantidad intentos incorrectos")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not self.gui.intentosEntry.get().isdigit():
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Cantidad intentos incorrectos")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not isinstance(int(self.gui.intentosEntry.get()), (int, long)):
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Cantidad intentos incorrectos")
            self.list_box_error_index = self.list_box_error_index + 1

        return datos_correctos

    def verificar_datos_tcp(self, datos_correctos):
        print "Verificar datos TCP"

        if self.gui.direccionIPEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Direccion IP incorrecta")
            self.list_box_error_index = self.list_box_error_index + 1

        if self.gui.puertoTCPEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Puerto TCP incorrecto")
            self.list_box_error_index = self.list_box_error_index + 1

        return datos_correctos

    def verificar_datos_llamada(self, datos_correctos):
        print "Verificar datos llamada"

        if self.gui.dispositivoEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Numero dispositivo incorrecto")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not self.gui.dispositivoEntry.get().isdigit():
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Numero dispositivo incorrecto")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not isinstance(int(self.gui.dispositivoEntry.get()), (int, long)):
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Numero dispositivo incorrecto")
            self.list_box_error_index = self.list_box_error_index + 1

        if self.gui.direccionInicialEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Direccion inicial incorrecta")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not self.gui.direccionInicialEntry.get().isdigit():
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Direccion inicial incorrecta")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not isinstance(int(self.gui.direccionInicialEntry.get()), (int, long)):
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Direccion inicial incorrecta")
            self.list_box_error_index = self.list_box_error_index + 1

        if (self.gui.funcionCombo.get() == '' or not (
                            self.gui.funcionCombo.get() == '3' or
                            self.gui.funcionCombo.get() == '6' or
                            self.gui.funcionCombo.get() == '16')):
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Funcion incorrecta")
            self.list_box_error_index = self.list_box_error_index + 1

        cantidad_de_variables = 0
        if self.gui.cantidadVariablesEntry.get() == '':
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Cantidad variables incorrecta")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not self.gui.cantidadVariablesEntry.get().isdigit():
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Cantidad variables incorrecta")
            self.list_box_error_index = self.list_box_error_index + 1
        elif not isinstance(int(self.gui.cantidadVariablesEntry.get()), (int, long)):
            datos_correctos = False
            self.gui.respuestaListBox.insert(self.list_box_error_index, "Cantidad variables incorrecta")
            self.list_box_error_index = self.list_box_error_index + 1
        else:
            cantidad_de_variables = int(self.gui.cantidadVariablesEntry.get())

        if self.gui.funcionCombo.get() == '6':
            if self.gui.variable1Entry.get() == '':
                datos_correctos = False
                self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable incorrecta")
                self.list_box_error_index = self.list_box_error_index + 1
            elif not self.gui.variable1Entry.get().isdigit():
                datos_correctos = False
                self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable incorrecta")
                self.list_box_error_index = self.list_box_error_index + 1
            elif not isinstance(int(self.gui.variable1Entry.get()), (int, long)):
                datos_correctos = False
                self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable incorrecta")
                self.list_box_error_index = self.list_box_error_index + 1

        if self.gui.funcionCombo.get() == '16':
            if cantidad_de_variables >= 1:
                if self.gui.variable1Entry.get() == '':
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 1 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif not self.gui.variable1Entry.get().isdigit():
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 1 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif not isinstance(int(self.gui.variable1Entry.get()), (int, long)):
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 1 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif int(self.gui.variable1Entry.get()) > 65535:
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 1 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1

            if cantidad_de_variables >= 2:
                if self.gui.variable2Entry.get() == '':
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 2 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif not self.gui.variable2Entry.get().isdigit():
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 2 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif not isinstance(int(self.gui.variable2Entry.get()), (int, long)):
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 2 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif int(self.gui.variable2Entry.get()) > 65535:
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 2 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1

            if cantidad_de_variables >= 3:
                if self.gui.variable3Entry.get() == '':
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 3 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif not self.gui.variable3Entry.get().isdigit():
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 3 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif not isinstance(int(self.gui.variable3Entry.get()), (int, long)):
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 3 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif int(self.gui.variable3Entry.get()) > 65535:
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 3 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1

            if cantidad_de_variables == 4:
                if self.gui.variable4Entry.get() == '':
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 4 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif not self.gui.variable4Entry.get().isdigit():
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 4 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif not isinstance(int(self.gui.variable4Entry.get()), (int, long)):
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 4 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1
                elif int(self.gui.variable4Entry.get()) > 65535:
                    datos_correctos = False
                    self.gui.respuestaListBox.insert(self.list_box_error_index, "Variable 4 incorrecta")
                    self.list_box_error_index = self.list_box_error_index + 1

                return datos_correctos
