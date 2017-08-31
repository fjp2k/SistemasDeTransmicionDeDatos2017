#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Aug 30, 2017 06:47:52 PM


import sys
from conexion import  Conexion

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

def set_Tk_var():
    global combobox
    combobox = StringVar()

def conectar():
    print('principal_support.conectar')
    conectado = conexion.conexion_puerto(puerto=w.puertoEntry.get(), baudrate = w.baudiosEntry.get(), timeout =w.timeoutEntry.get(),
                                         intentos=w.intentosEntry.get(), funcion=03, dispositivo=w.dispositivoEntry.get(),
                                         direccion=w.direccionEntry.get(), cantidadRegistros=w.variablesEntry.get())
    if (conectado):
        w.estadoLabel.config(text='Conectado')
        conexion.obtenerRespuestas()
    else:
        w.estadoLabel.config(text='Error al conectar')
    sys.stdout.flush()

def convertirBinario():
    print('principal_support.convertirBinario')
    sys.stdout.flush()

def convertirDecimal():
    print('principal_support.convertirDecimal')
    sys.stdout.flush()

def convertirHexadecimal():
    print('principal_support.convertirHexadecimal')
    sys.stdout.flush()

def desconectar():
    print('principal_support.desconectar')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root, conexion
    w = gui
    top_level = top
    root = top
    conexion = Conexion(gui=w)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import principal

    principal.vp_start_gui()