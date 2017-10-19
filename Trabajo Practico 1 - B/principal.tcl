#############################################################################
# Generated by PAGE version 4.9
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    namespace eval ::widgets::$base {
        set dflt,origin 1
        set runvisible 1
    }
    set site_3_0 $base.scr58
    set site_3_0 $base.cpd61
    set site_3_0 $base.cpd62
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#e7e7e7} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1250x700
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1250 700
    wm minsize $top 1250 650
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm title $top "Trabajo Practico 1"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure Entry -background #d9d9d9
    ttk::style configure Entry -foreground #000000
    ttk::style configure Entry -font TkDefaultFont
    entry $top.ent38 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent38" "puertoSerialEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent39 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent39" "dispositivoEntry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab41 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#000000} \
        -foreground {#000000} -highlightbackground {#e7e7e7} \
        -highlightcolor black -justify right -text {Puerto Serial} 
    vTcl:DefineAlias "$top.lab41" "puertoSerialLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab42 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text {Time Out} 
    vTcl:DefineAlias "$top.lab42" "timeOutLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab43 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text Dispositivo 
    vTcl:DefineAlias "$top.lab43" "dispositivoLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text Funcion 
    vTcl:DefineAlias "$top.lab44" "funcionLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text Baudios 
    vTcl:DefineAlias "$top.lab45" "baudiosLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text {Direccion Inicial} 
    vTcl:DefineAlias "$top.lab46" "direccionInicialLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text {Cantidad de variables} 
    vTcl:DefineAlias "$top.lab47" "cantidadDeVariablesLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text {Cantidad de Intentos} 
    vTcl:DefineAlias "$top.lab48" "cantidadIntentosLb" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent50 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent50" "direccionInicialEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.cpd51 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.cpd51" "timeoutEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.cpd52 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.cpd52" "baudiosEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.cpd53 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.cpd53" "cantidadVariablesEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.cpd54 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.cpd54" "intentosEntry" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo56 \
        -values 3,6,16 -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$top.tCo56" "funcionCombo" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr58 \
        -background {#d9d9d9} -height 75 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr58" "tramasSolicitudListBox" vTcl:WidgetProc "Toplevel1" 1

    $top.scr58.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    button $top.but59 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command conectar -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Conectar 
    vTcl:DefineAlias "$top.but59" "conectarBtn" vTcl:WidgetProc "Toplevel1" 1
    button $top.but60 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -command desconectar \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Desconectar 
    vTcl:DefineAlias "$top.but60" "desconectarBtn" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.cpd61 \
        -background {#d9d9d9} -height 75 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.cpd61" "tramasRespuestaListBox" vTcl:WidgetProc "Toplevel1" 1

    $top.cpd61.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.cpd62 \
        -background {#d9d9d9} -height 75 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.cpd62" "respuestaListBox" vTcl:WidgetProc "Toplevel1" 1

    $top.cpd62.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    button $top.but63 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command convertirHexadecimal \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Hexadecimal 
    vTcl:DefineAlias "$top.but63" "hexaBtn" vTcl:WidgetProc "Toplevel1" 1
    button $top.but64 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command convertirDecimal \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Decimal 
    vTcl:DefineAlias "$top.but64" "decimalBtn" vTcl:WidgetProc "Toplevel1" 1
    button $top.but65 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command convertirBinario \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Binario 
    vTcl:DefineAlias "$top.but65" "binarioBtn" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab66 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#e0e1f5} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief groove \
        -text {Tramas de Solicitud} 
    vTcl:DefineAlias "$top.lab66" "tramasSolicitudLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab67 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#e0e1f5} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief groove \
        -text {Tramas de Respuesta} -width 330 
    vTcl:DefineAlias "$top.lab67" "tramasRespuestaLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab37 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#e0e1f5} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief groove \
        -text Respuestas -width 660 
    vTcl:DefineAlias "$top.lab37" "respuestasLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab38 \
        -activebackground {#f9f9f9} -activeforeground black -anchor w \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#5337f2} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Desconectado 
    vTcl:DefineAlias "$top.lab38" "valorEstadoConexionLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab39 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Variable 1} 
    vTcl:DefineAlias "$top.lab39" "variable1Lb" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent40 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent40" "variable1Entry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Variable 2} 
    vTcl:DefineAlias "$top.lab49" "variable2Lb" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent51 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent51" "variable2Entry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Variable 3} 
    vTcl:DefineAlias "$top.lab52" "variable3Lb" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Variable 4} 
    vTcl:DefineAlias "$top.lab53" "variable4Lb" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent54 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent54" "variable3Entry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent55 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent55" "variable4Entry" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TCheckbutton -background #d9d9d9
    ttk::style configure TCheckbutton -foreground #000000
    ttk::style configure TCheckbutton -font TkDefaultFont
    ttk::checkbutton $top.tCh37 \
        -variable tch37 -takefocus {} -text Tcheck 
    vTcl:DefineAlias "$top.tCh37" "TCheckbutton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa40 \
        -background {#e7e7e7} -foreground {#000000} -relief flat \
        -text {Estado conexion:} 
    vTcl:DefineAlias "$top.tLa40" "estadoConexionLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd43 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text {Direccion IP} 
    vTcl:DefineAlias "$top.cpd43" "direccionIpLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd44 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text Puerto 
    vTcl:DefineAlias "$top.cpd44" "puertoTCPLb" vTcl:WidgetProc "Toplevel1" 1
    entry $top.cpd45 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.cpd45" "direccionIPEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.cpd46 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.cpd46" "puertoTCPEntry" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad38 \
        -activebackground {#d9d9d9} -activeforeground {#000000} -anchor w \
        -background {#e7e7e7} -command puertoSerialRBSeleccionado \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -relief groove -text {Puerto Serial} -variable {} 
    vTcl:DefineAlias "$top.rad38" "puertoSerialRB" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.cpd39 \
        -activebackground {#d9d9d9} -activeforeground {#000000} -anchor w \
        -background {#e7e7e7} -command tcpRBSeleccionado \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -relief groove -text TCP -variable {} 
    vTcl:DefineAlias "$top.cpd39" "tcpRB" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c8bdf4} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief groove \
        -text {Configuracion Llamada} -width 440 
    vTcl:DefineAlias "$top.lab51" "configLlamadaLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd55 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c8bdf4} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief groove \
        -text Tramas -width 660 
    vTcl:DefineAlias "$top.cpd55" "tramasLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd57 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c8bdf4} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief groove \
        -text {Configuracion Puerto Serie} -width 440 
    vTcl:DefineAlias "$top.cpd57" "configPuertoSerieLb" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd58 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c8bdf4} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief groove \
        -text {Configuracion TCP} -width 450 
    vTcl:DefineAlias "$top.cpd58" "configTCPLb" vTcl:WidgetProc "Toplevel1" 1
    entry $top.cpd41 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.cpd41" "intentosTCPEntry" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd42 \
        -activebackground {#f9f9f9} -activeforeground black -anchor e \
        -background {#e7e7e7} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text {Cantidad de intentos} 
    vTcl:DefineAlias "$top.cpd42" "timrOutTCPLb" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent38 \
        -in $top -x 660 -y 80 -width 250 -height 27 -anchor center \
        -bordermode ignore 
    place $top.ent39 \
        -in $top -x 210 -y 310 -width 250 -height 27 -anchor nw \
        -bordermode ignore 
    place $top.lab41 \
        -in $top -x 430 -y 80 -width 190 -relwidth 0 -height 30 -relheight 0 \
        -anchor center -bordermode ignore 
    place $top.lab42 \
        -in $top -x 430 -y 110 -width 190 -relwidth 0 -height 30 -relheight 0 \
        -anchor center -bordermode ignore 
    place $top.lab43 \
        -in $top -x 20 -y 310 -width 190 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 20 -y 370 -width 190 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 430 -y 140 -width 190 -relwidth 0 -height 30 -relheight 0 \
        -anchor center -bordermode ignore 
    place $top.lab46 \
        -in $top -x 20 -y 340 -width 190 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 20 -y 400 -width 190 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 430 -y 170 -width 190 -relwidth 0 -height 30 -relheight 0 \
        -anchor center -bordermode ignore 
    place $top.ent50 \
        -in $top -x 210 -y 340 -width 250 -height 27 -anchor nw \
        -bordermode ignore 
    place $top.cpd51 \
        -in $top -x 660 -y 110 -width 250 -height 27 -anchor center \
        -bordermode inside 
    place $top.cpd52 \
        -in $top -x 660 -y 140 -width 250 -height 27 -anchor center \
        -bordermode inside 
    place $top.cpd53 \
        -in $top -x 210 -y 400 -width 250 -height 27 -anchor nw \
        -bordermode inside 
    place $top.cpd54 \
        -in $top -x 660 -y 170 -width 250 -relwidth 0 -height 27 -relheight 0 \
        -anchor center -bordermode inside 
    place $top.tCo56 \
        -in $top -x 210 -y 370 -width 250 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.scr58 \
        -in $top -x 560 -y 270 -width 330 -relwidth 0 -height 148 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but59 \
        -in $top -x 10 -y 120 -width 120 -relwidth 0 -height 50 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but60 \
        -in $top -x 150 -y 120 -width 120 -relwidth 0 -height 50 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd61 \
        -in $top -x 890 -y 270 -width 330 -relwidth 0 -height 148 \
        -relheight 0 -anchor nw -bordermode inside 
    place $top.cpd62 \
        -in $top -x 700 -y 460 -width 520 -relwidth 0 -height 188 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but63 \
        -in $top -x 570 -y 470 -width 120 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but64 \
        -in $top -x 570 -y 520 -width 120 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but65 \
        -in $top -x 570 -y 570 -width 120 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 560 -y 240 -width 330 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab67 \
        -in $top -x 890 -y 240 -width 330 -anchor nw -bordermode ignore 
    place $top.lab37 \
        -in $top -x 560 -y 430 -width 660 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab38 \
        -in $top -x 170 -y 190 -width 349 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab39 \
        -in $top -x 20 -y 460 -width 190 -height 30 -anchor nw \
        -bordermode ignore 
    place $top.ent40 \
        -in $top -x 210 -y 460 -width 250 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 20 -y 490 -width 190 -height 30 -anchor nw \
        -bordermode ignore 
    place $top.ent51 \
        -in $top -x 210 -y 490 -width 250 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 20 -y 520 -width 190 -height 30 -anchor nw \
        -bordermode ignore 
    place $top.lab53 \
        -in $top -x 20 -y 550 -width 190 -height 30 -anchor nw \
        -bordermode ignore 
    place $top.ent54 \
        -in $top -x 210 -y 520 -width 250 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent55 \
        -in $top -x 210 -y 550 -width 250 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCh37 \
        -in $top -x -120 -y 480 -anchor nw -bordermode ignore 
    place $top.tLa40 \
        -in $top -x 10 -y 190 -width 150 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd43 \
        -in $top -x 790 -y 60 -width 190 -height 30 -anchor nw \
        -bordermode inside 
    place $top.cpd44 \
        -in $top -x 790 -y 90 -width 190 -height 30 -anchor nw \
        -bordermode inside 
    place $top.cpd45 \
        -in $top -x 1110 -y 70 -width 250 -height 27 -anchor center \
        -bordermode inside 
    place $top.cpd46 \
        -in $top -x 1110 -y 100 -width 250 -relwidth 0 -height 27 \
        -relheight 0 -anchor center -bordermode inside 
    place $top.rad38 \
        -in $top -x 20 -y 20 -width 197 -relwidth 0 -height 37 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd39 \
        -in $top -x 20 -y 60 -width 197 -height 37 -anchor nw \
        -bordermode inside 
    place $top.lab51 \
        -in $top -x 20 -y 260 -width 440 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd55 \
        -in $top -x 890 -y 220 -width 660 -relwidth 0 -height 41 -relheight 0 \
        -anchor center -bordermode inside 
    place $top.cpd57 \
        -in $top -x 570 -y 30 -width 440 -relwidth 0 -height 41 -relheight 0 \
        -anchor center -bordermode inside 
    place $top.cpd58 \
        -in $top -x 1240 -y 10 -width 450 -relwidth 0 -height 41 -relheight 0 \
        -anchor ne -bordermode inside 
    place $top.cpd41 \
        -in $top -x 1110 -y 130 -width 250 -height 27 -anchor center \
        -bordermode inside 
    place $top.cpd42 \
        -in $top -x 790 -y 120 -width 190 -height 30 -anchor nw \
        -bordermode inside 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top37

