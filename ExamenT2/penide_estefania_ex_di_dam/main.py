# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime

import ventanaprincipal
import windowcalendar
from ventanaprincipal import *
import windowaviso
from windowaviso import *
import ventanaavisomenor
from ventanaavisomenor import *
import sys
import var,events,clientes


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = ventanaprincipal.Ui_MainWindow()
        var.ui.setupUi(self)

        var.saldo=2300
        var.ui.textEditSaldo.setText(str(var.saldo))

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir1)
        var.ui.leDNI.editingFinished.connect(clientes.Clientes.validarDNI)

        var.ui.bgTransaccion.buttonClicked.connect(clientes.Clientes.selTransaccion)

        var.ui.btCalendario.clicked.connect(clientes.Clientes.abrirCalendario)

        '''var.ui.btAceptar.clicked.connect(clientes.Clientes.comprobacion)
        if(var.info):
            print('Bien')'''
        var.ui.btAceptar.clicked.connect(clientes.Clientes.operacion)

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
        var.dlgCalendario.calendario.clicked.connect(clientes.Clientes.edad)
        var.dlgCalendario.calendario.clicked.connect(clientes.Clientes.cargarFecha)

class DialogEdad(QtWidgets.QDialog):

    def __init__(self):
        super(DialogEdad,self).__init__()
        var.dlgEdad = ventanaavisomenor.Ui_Dialog()
        var.dlgEdad.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    var.dlgCalendario=DialogCalendario()
    var.dlgEdad = DialogEdad()
    window.show()
    sys.exit(app.exec())





