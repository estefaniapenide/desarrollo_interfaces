import sys

import clientes
import var


class Eventos:
    def Salir1(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    def Salir2(self):
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec():
                sys.exit()
            else:
                var.dlgsalir.hide()
        except Exception as error:
            print("Error %s: " % str(error))

