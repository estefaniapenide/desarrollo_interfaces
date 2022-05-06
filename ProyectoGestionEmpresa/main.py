# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime

#import printer
import ventanaprincipal
import windowcalendar
import windowaviso
from windowaviso import *
import conexion
import sys
import var,events,clientes
#import xlrd



class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = ventanaprincipal.Ui_MainWindow()
        var.ui.setupUi(self)

        var.formaEnvio='RECOGIDA POR CLIENTE'#Forma de envio prederterminada
        var.filedb='gestionEmpresa.db'
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.mostrarClientes(self)

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir1)

        var.ui.leDNI.editingFinished.connect(clientes.Clientes.validarDNI)
        var.ui.bgSexo.buttonClicked.connect(clientes.Clientes.selSexo)

        var.cbPago = (var.ui.cbEfectivo, var.ui.cbTarjeta, var.ui.cbTransferencia)
        for i in var.cbPago:
            i.stateChanged.connect(clientes.Clientes.selPago)

        clientes.Clientes.cargarPovincia()
        var.ui.comBoxProvincia.activated[str].connect(clientes.Clientes.seleccionarProvincia)

        var.ui.btCalendario.clicked.connect(clientes.Clientes.abrirCalendario)

        var.ui.btAlta.clicked.connect(clientes.Clientes.altaClientes)

        var.ui.btBaja.clicked.connect(clientes.Clientes.bajaCliente)

        var.ui.btLimpiar.clicked.connect(clientes.Clientes.limpiarCliente)

        var.ui.btRefresh.clicked.connect(conexion.Conexion.mostrarClientes)
        var.ui.btRefresh.clicked.connect(clientes.Clientes.limpiarCliente)

        var.ui.btBuscar.clicked.connect(conexion.Conexion.buscarCliente)

        var.ui.btModificar.clicked.connect(clientes.Clientes.modificarCliente)

        var.ui.statusbar.addPermanentWidget(var.ui.tbEstado,1)

        var.ui.toolbarSalir.triggered.connect(events.Eventos.Salir1)

        var.ui.toolbarAbrirCarpeta.triggered.connect(events.Eventos.AbrirDir)
        var.ui.actionAbrir.triggered.connect(events.Eventos.AbrirDir)

        var.ui.toolbarComprimir.triggered.connect(events.Eventos.Backup)
        var.ui.actionCrear_Backup.triggered.connect(events.Eventos.Backup)

        var.ui.sbEnvio.valueChanged.connect(clientes.Clientes.seleccionarFormaEnvio)

        var.ui.actionImportar_Base_de_Datos.triggered.connect(events.Eventos.importarBaseDatos)

        var.ui.actionRecuperar_Backup.triggered.connect(events.Eventos.recuperarBackup)

        #var.ui.actionVisualizar_datos_archivo_xls.triggered.connect(events.Eventos.mostarDatosXLS)

        #var.ui.actionImportar_Datos.triggered.connect(events.Eventos.importarDatosXLS)

        #var.ui.btInforme.clicked.connect(printer.Printer.reportCli)




class DialogSalir(QtWidgets.QDialog):

    def __init__(self):
        super(DialogSalir,self).__init__()
        var.dlgsalir = windowaviso.Ui_Dialog()
        var.dlgsalir.setupUi(self)

        var.ui.btSalir.clicked.connect(events.Eventos.Salir2)


class DialogCalendario(QtWidgets.QDialog):

    def __init__(self):
        super(DialogCalendario,self).__init__()
        var.dlgCalendario = windowcalendar.Ui_Dialog()
        var.dlgCalendario.setupUi(self)
        diaActual=datetime.now().day
        mesActual=datetime.now().month
        anoActual=datetime.now().year

        var.dlgCalendario.calendario.setSelectedDate(QtCore.QDate(anoActual,mesActual,diaActual))
        var.dlgCalendario.calendario.clicked.connect(clientes.Clientes.cargarFecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir,self).__init__()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    var.dlgCalendario=DialogCalendario()
    var.filedlgabrir=FileDialogAbrir()
    window.show()
    sys.exit(app.exec())





