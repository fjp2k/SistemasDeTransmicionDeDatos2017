import conexionPop

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

        self.valor_ssl = IntVar()
        self.valor_ssl.set(0)
        self.index_textbox = 0

        self.gui = gui

        conexionPop.iniciar_conector(self)

    def configurar_gui(self):
        """
        self.gui.conectar_btn
        self.gui.desconectar_btn
        self.gui.estado_conexion_info

        self.gui.servidor_entry.get()
        self.gui.usuario_entry.get()
        self.gui.contrasenia_entry.get()
        self.gui.frecuencia_entry.get()

        self.gui.puerto_entry.get()
        self.gui.ssl_check.set(0)

        self.gui.info_listbox.delete(0, END)
        """
        print "Configurando GUI"

        self.gui.servidor_entry.insert(0, 'localhost')
        self.gui.usuario_entry.insert(0, 'test')
        self.gui.contrasenia_entry.insert(0, '123456')
        self.gui.frecuencia_entry.insert(0, '5')
        self.gui.puerto_entry.insert(0, '')

        self.gui.ssl_check.configure(variable=self.valor_ssl, onvalue=1, offvalue=0)

    def conectar(self):

        if self.verificar_datos():

            if self.valor_ssl.get() == 1:
                ssl_activado = True
                conexionPop.conectar_a_servidor(ssl=ssl_activado,
                                                servidor=self.gui.servidor_entry.get(),
                                                username=self.gui.usuario_entry.get(),
                                                contrasenia=self.gui.contrasenia_entry.get(),
                                                frecuencia=int(self.gui.frecuencia_entry.get()),
                                                puerto=self.gui.puerto_entry.get()
                                                )
            else:
                ssl_activado = False
                conexionPop.conectar_a_servidor(ssl=ssl_activado,
                                                servidor=self.gui.servidor_entry.get(),
                                                username=self.gui.usuario_entry.get(),
                                                contrasenia=self.gui.contrasenia_entry.get(),
                                                frecuencia=int(self.gui.frecuencia_entry.get())
                                                )
        else:
            self.cambiar_mensaje_estado("Datos incorrectos")

    # noinspection PyMethodMayBeStatic
    def desconectar(self):
        conexionPop.desconectar()

    def cambiar_mensaje_estado(self, mensaje):
        self.gui.estado_conexion_info.configure(text=''+mensaje+'')

    # noinspection PyMethodMayBeStatic
    def cargar_datos_bd(self):
        conexionPop.obtener_datos_almacenados()

    def limpiar_pantalla(self):
        self.gui.info_listbox.delete(0, END)
        self.index_textbox = 0

    def imprimir(self, mensaje):
        self.gui.info_listbox.insert(self.index_textbox, mensaje)
        self.index_textbox += 1

    def imprimir_error(self, mensaje):
        self.limpiar_pantalla()
        self.imprimir(mensaje)

    # noinspection PyMethodMayBeStatic
    def verificar_datos(self):

        self.limpiar_pantalla()

        datos_correctos = True

        if self.gui.servidor_entry.get() == '':
            datos_correctos = False
            self.imprimir("Direccion de servidor vacia")

        if self.gui.usuario_entry.get() == '':
            datos_correctos = False
            self.imprimir("Usuario vacio")

        if self.gui.contrasenia_entry.get() == '':
            datos_correctos = False
            self.imprimir("Contrasenia vacia")

        if self.gui.frecuencia_entry.get() == '':
            datos_correctos = False
            self.imprimir("Frecuencia vacia")
        elif not self.gui.frecuencia_entry.get().isdigit():
            datos_correctos = False
            self.imprimir("La frecuencia debe ser un entero positivo")
        elif not isinstance(int(self.gui.frecuencia_entry.get()), (int, long)):
            datos_correctos = False
            self.imprimir("La frecuencia debe ser un entero positivo")

        if self.valor_ssl.get() == 1:
            if self.gui.puerto_entry.get() == '':
                datos_correctos = False
                self.imprimir("Puerto SSL vacio")

        return datos_correctos
