

import ventanaprincipal
from ventanaprincipal import *
import ventanaaviso
from ventanaaviso import *
import ventanacalendario
from ventanacalendario import *
import datetime
from datetime import *
import sys, var, events, clientes

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main,self).__init__()
        var.ui = ventanaprincipal.Ui_MainWindow()
        var.ui.setupUi(self)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.pushButtonSalir.clicked.connect(events.Eventos.Salir)

        var.ui.lineEditDni.editingFinished.connect(clientes.Clientes.validarDNI)
        var.ui.buttonGroupSexo.buttonClicked.connect(clientes.Clientes.seleccionarSexo)

        var.pago = (var.ui.checkBoxTrajeta_2,var.ui.checkBoxEfectivo_2,var.ui.checkBoxTransferencia_2)

        for i in var.pago:
            i.stateChanged.connect(clientes.Clientes.seleccionarPago)

        clientes.Clientes.cargarProvincia()
        var.ui.comboBoxProvincia.activated[str].connect(clientes.Clientes.selccionarProvincia)

        var.ui.pushButtonCalendario.clicked.connect(clientes.Clientes.abrirCalendario)

        var.ui.pushButtonAceptar.clicked.connect(clientes.Clientes.mostrarClientes)


class DialogoSalir(QtWidgets.QDialog):

    def __init__(self):
        super(DialogoSalir,self).__init__()
        var.dialogoSalir= ventanaaviso.Ui_Dialog()
        var.dialogoSalir.setupUi(self)

class DialogoCalendario(QtWidgets.QDialog):

    def __init__(self):
        super(DialogoCalendario,self).__init__()
        var.dialogoCalendario =ventanacalendario.Ui_Dialog()
        var.dialogoCalendario.setupUi(self)

        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dialogoCalendario.calendario.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))

        var.dialogoCalendario.calendario.clicked.connect(clientes.Clientes.cargarFecha)




if __name__=='__main__':
    app=QtWidgets.QApplication([])
    window= Main()
    var.dialogoSalir = DialogoSalir()
    var.dialogoCalendario = DialogoCalendario()
    window.show()
    sys.exit(app.exec())