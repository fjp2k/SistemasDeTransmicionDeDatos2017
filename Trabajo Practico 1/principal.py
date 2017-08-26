#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Aug 26, 2017 07:42:27 PM
import sys

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

import principal_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    principal_support.set_Tk_var()
    top = Trabajo_Practico_1 (root)
    principal_support.init(root, top)
    root.mainloop()

w = None
def create_Trabajo_Practico_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    principal_support.set_Tk_var()
    top = Trabajo_Practico_1 (w)
    principal_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Trabajo_Practico_1():
    global w
    w.destroy()
    w = None


class Trabajo_Practico_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1000x590+316+156")
        top.title("Trabajo Practico 1")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.puertoEntry = Entry(top)
        self.puertoEntry.place(relx=0.17, rely=0.02, relheight=0.05
                , relwidth=0.25)
        self.puertoEntry.configure(background="white")
        self.puertoEntry.configure(disabledforeground="#a3a3a3")
        self.puertoEntry.configure(font="TkFixedFont")
        self.puertoEntry.configure(foreground="#000000")
        self.puertoEntry.configure(highlightbackground="#d9d9d9")
        self.puertoEntry.configure(highlightcolor="black")
        self.puertoEntry.configure(insertbackground="black")
        self.puertoEntry.configure(selectbackground="#c4c4c4")
        self.puertoEntry.configure(selectforeground="black")

        self.dispositivoEntry = Entry(top)
        self.dispositivoEntry.place(relx=0.17, rely=0.07, relheight=0.05
                , relwidth=0.25)
        self.dispositivoEntry.configure(background="white")
        self.dispositivoEntry.configure(disabledforeground="#a3a3a3")
        self.dispositivoEntry.configure(font="TkFixedFont")
        self.dispositivoEntry.configure(foreground="#000000")
        self.dispositivoEntry.configure(highlightbackground="#d9d9d9")
        self.dispositivoEntry.configure(highlightcolor="black")
        self.dispositivoEntry.configure(insertbackground="black")
        self.dispositivoEntry.configure(selectbackground="#c4c4c4")
        self.dispositivoEntry.configure(selectforeground="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.04, rely=0.02, height=30, width=130)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor=E)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify=RIGHT)
        self.Label1.configure(text='''Puerto Serial''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.44, rely=0.02, height=30, width=190)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor=E)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(justify=RIGHT)
        self.Label2.configure(text='''Time Out''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.04, rely=0.07, height=30, width=130)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor=E)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify=RIGHT)
        self.Label3.configure(text='''Dispositivo''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.04, rely=0.17, height=30, width=130)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor=E)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(justify=RIGHT)
        self.Label4.configure(text='''Funcion''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.43, rely=0.12, height=30, width=190)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor=E)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(justify=RIGHT)
        self.Label5.configure(text='''Baudios''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.04, rely=0.12, height=30, width=130)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor=E)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(justify=RIGHT)
        self.Label6.configure(text='''Direccion Inicial''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.44, rely=0.17, height=30, width=190)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor=E)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(justify=RIGHT)
        self.Label7.configure(text='''Cantidad de variables''')

        self.Label8 = Label(top)
        self.Label8.place(relx=0.44, rely=0.07, height=30, width=190)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor=E)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(justify=RIGHT)
        self.Label8.configure(text='''Cantidad de Intentos''')

        self.direccionEntry = Entry(top)
        self.direccionEntry.place(relx=0.17, rely=0.12, relheight=0.05
                , relwidth=0.25)
        self.direccionEntry.configure(background="white")
        self.direccionEntry.configure(disabledforeground="#a3a3a3")
        self.direccionEntry.configure(font="TkFixedFont")
        self.direccionEntry.configure(foreground="#000000")
        self.direccionEntry.configure(highlightbackground="#d9d9d9")
        self.direccionEntry.configure(highlightcolor="black")
        self.direccionEntry.configure(insertbackground="black")
        self.direccionEntry.configure(selectbackground="#c4c4c4")
        self.direccionEntry.configure(selectforeground="black")

        self.timeoutEntry = Entry(top)
        self.timeoutEntry.place(relx=0.63, rely=0.02, relheight=0.05
                , relwidth=0.25)
        self.timeoutEntry.configure(background="white")
        self.timeoutEntry.configure(disabledforeground="#a3a3a3")
        self.timeoutEntry.configure(font="TkFixedFont")
        self.timeoutEntry.configure(foreground="#000000")
        self.timeoutEntry.configure(highlightbackground="#d9d9d9")
        self.timeoutEntry.configure(highlightcolor="black")
        self.timeoutEntry.configure(insertbackground="black")
        self.timeoutEntry.configure(selectbackground="#c4c4c4")
        self.timeoutEntry.configure(selectforeground="black")

        self.baudiosEntry = Entry(top)
        self.baudiosEntry.place(relx=0.63, rely=0.12, relheight=0.05
                , relwidth=0.25)
        self.baudiosEntry.configure(background="white")
        self.baudiosEntry.configure(disabledforeground="#a3a3a3")
        self.baudiosEntry.configure(font="TkFixedFont")
        self.baudiosEntry.configure(foreground="#000000")
        self.baudiosEntry.configure(highlightbackground="#d9d9d9")
        self.baudiosEntry.configure(highlightcolor="black")
        self.baudiosEntry.configure(insertbackground="black")
        self.baudiosEntry.configure(selectbackground="#c4c4c4")
        self.baudiosEntry.configure(selectforeground="black")

        self.variablesEntry = Entry(top)
        self.variablesEntry.place(relx=0.63, rely=0.17, relheight=0.05
                , relwidth=0.25)
        self.variablesEntry.configure(background="white")
        self.variablesEntry.configure(disabledforeground="#a3a3a3")
        self.variablesEntry.configure(font="TkFixedFont")
        self.variablesEntry.configure(foreground="#000000")
        self.variablesEntry.configure(highlightbackground="#d9d9d9")
        self.variablesEntry.configure(highlightcolor="black")
        self.variablesEntry.configure(insertbackground="black")
        self.variablesEntry.configure(selectbackground="#c4c4c4")
        self.variablesEntry.configure(selectforeground="black")

        self.intentosEntry = Entry(top)
        self.intentosEntry.place(relx=0.63, rely=0.07, relheight=0.05
                , relwidth=0.25)
        self.intentosEntry.configure(background="white")
        self.intentosEntry.configure(disabledforeground="#a3a3a3")
        self.intentosEntry.configure(font="TkFixedFont")
        self.intentosEntry.configure(foreground="#000000")
        self.intentosEntry.configure(highlightbackground="#d9d9d9")
        self.intentosEntry.configure(highlightcolor="black")
        self.intentosEntry.configure(insertbackground="black")
        self.intentosEntry.configure(selectbackground="#c4c4c4")
        self.intentosEntry.configure(selectforeground="black")

        self.funcionCombo = ttk.Combobox(top)
        self.funcionCombo.place(relx=0.17, rely=0.17, relheight=0.05
                , relwidth=0.25)
        self.value_list = [3,6,16,]
        self.funcionCombo.configure(values=self.value_list)
        self.funcionCombo.configure(textvariable=principal_support.combobox)
        self.funcionCombo.configure(takefocus="")

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.27, rely=0.32, relheight=0.25
                , relwidth=0.33)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)

        self.conectarBtn = Button(top)
        self.conectarBtn.place(relx=0.06, rely=0.32, height=50, width=120)
        self.conectarBtn.configure(activebackground="#d9d9d9")
        self.conectarBtn.configure(activeforeground="#000000")
        self.conectarBtn.configure(background="#d9d9d9")
        self.conectarBtn.configure(command=principal_support.conectar)
        self.conectarBtn.configure(disabledforeground="#a3a3a3")
        self.conectarBtn.configure(foreground="#000000")
        self.conectarBtn.configure(highlightbackground="#d9d9d9")
        self.conectarBtn.configure(highlightcolor="black")
        self.conectarBtn.configure(pady="0")
        self.conectarBtn.configure(text='''Conectar''')

        self.desconectarBtn = Button(top)
        self.desconectarBtn.place(relx=0.06, rely=0.42, height=50, width=120)
        self.desconectarBtn.configure(activebackground="#d9d9d9")
        self.desconectarBtn.configure(activeforeground="#000000")
        self.desconectarBtn.configure(background="#d9d9d9")
        self.desconectarBtn.configure(disabledforeground="#a3a3a3")
        self.desconectarBtn.configure(foreground="#000000")
        self.desconectarBtn.configure(highlightbackground="#d9d9d9")
        self.desconectarBtn.configure(highlightcolor="black")
        self.desconectarBtn.configure(pady="0")
        self.desconectarBtn.configure(text='''Desconectar''')

        self.Scrolledlistbox2 = ScrolledListBox(top)
        self.Scrolledlistbox2.place(relx=0.62, rely=0.32, relheight=0.25
                , relwidth=0.33)
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(foreground="black")
        self.Scrolledlistbox2.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox2.configure(selectforeground="black")
        self.Scrolledlistbox2.configure(width=10)

        self.Scrolledlistbox3 = ScrolledListBox(top)
        self.Scrolledlistbox3.place(relx=0.27, rely=0.66, relheight=0.32
                , relwidth=0.68)
        self.Scrolledlistbox3.configure(background="white")
        self.Scrolledlistbox3.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox3.configure(font="TkFixedFont")
        self.Scrolledlistbox3.configure(foreground="black")
        self.Scrolledlistbox3.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox3.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox3.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox3.configure(selectforeground="black")
        self.Scrolledlistbox3.configure(width=10)

        self.hexaBtn = Button(top)
        self.hexaBtn.place(relx=0.06, rely=0.66, height=40, width=120)
        self.hexaBtn.configure(activebackground="#d9d9d9")
        self.hexaBtn.configure(activeforeground="#000000")
        self.hexaBtn.configure(background="#d9d9d9")
        self.hexaBtn.configure(disabledforeground="#a3a3a3")
        self.hexaBtn.configure(foreground="#000000")
        self.hexaBtn.configure(highlightbackground="#d9d9d9")
        self.hexaBtn.configure(highlightcolor="black")
        self.hexaBtn.configure(pady="0")
        self.hexaBtn.configure(text='''Hexadecimal''')

        self.decimalBtn = Button(top)
        self.decimalBtn.place(relx=0.06, rely=0.74, height=40, width=120)
        self.decimalBtn.configure(activebackground="#d9d9d9")
        self.decimalBtn.configure(activeforeground="#000000")
        self.decimalBtn.configure(background="#d9d9d9")
        self.decimalBtn.configure(disabledforeground="#a3a3a3")
        self.decimalBtn.configure(foreground="#000000")
        self.decimalBtn.configure(highlightbackground="#d9d9d9")
        self.decimalBtn.configure(highlightcolor="black")
        self.decimalBtn.configure(pady="0")
        self.decimalBtn.configure(text='''Decimal''')

        self.binarioBtn = Button(top)
        self.binarioBtn.place(relx=0.06, rely=0.81, height=40, width=120)
        self.binarioBtn.configure(activebackground="#d9d9d9")
        self.binarioBtn.configure(activeforeground="#000000")
        self.binarioBtn.configure(background="#d9d9d9")
        self.binarioBtn.configure(disabledforeground="#a3a3a3")
        self.binarioBtn.configure(foreground="#000000")
        self.binarioBtn.configure(highlightbackground="#d9d9d9")
        self.binarioBtn.configure(highlightcolor="black")
        self.binarioBtn.configure(pady="0")
        self.binarioBtn.configure(text='''Binario''')

        self.Label10 = Label(top)
        self.Label10.place(relx=0.34, rely=0.25, height=31, width=200)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Tramas de Solicitud''')

        self.Label11 = Label(top)
        self.Label11.place(relx=0.68, rely=0.25, height=31, width=200)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Tramas de Respuesta''')

        self.Label9 = Label(top)
        self.Label9.place(relx=0.5, rely=0.59, height=31, width=200)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Respuestas''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)







# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()



