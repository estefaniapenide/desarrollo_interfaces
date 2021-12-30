import ventana
from ventana import *
import sys
import var,events

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = ventana.Ui_Proyecto1()
        var.ui.setupUi(self)

        '''Conexión con los eventos'''
        var.ui.btnAceptar.clicked.connect(events.Eventos.Saludo)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

