# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ventanaGC
from ventanaGC import *
import sys
import var,events

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = ventanaGC.GestionClientes()
        var.ui.setupUi(self)

        '''Conexión con los eventos'''
        var.ui.btnAceptar.clicked.connect(events.Eventos.AceptarDatos)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
