# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ProyectoUnoVentana
from ProyectoUnoVentana import *
import windowaviso
from windowaviso import *
import sys
import var,events,clientes

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = ProyectoUnoVentana.ProyectoUno()
        var.ui.setupUi(self)

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir1)
        var.ui.leDNI.editingFinished.connect(clientes.Clientes.validarDNI)


class DialogSalir(QtWidgets.QDialog):

    def __init__(self):
        super(DialogSalir,self).__init__()
        var.dlgsalir = windowaviso.Ui_Dialog()
        var.dlgsalir.setupUi(self)

        var.ui.btSalir.clicked.connect(events.Eventos.Salir2)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    window.show()
    sys.exit(app.exec())





