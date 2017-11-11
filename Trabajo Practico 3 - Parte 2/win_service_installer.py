import win32service
import win32serviceutil

import controlador_conexion


class PySvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "ServicioPopTransmision"
    _svc_display_name_ = "Servicio Pop Transmision de datos"
    _svc_description_ = "Transmision de datos Practico 3 Servicio Pop"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)

    # Inicio servicio
    def SvcDoRun(self):
        controlador_conexion.conectar()

    # Finalizacion servicio
    def SvcStop(self):
        controlador_conexion.desconectar()
        # tell the SCM we're shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PySvc)