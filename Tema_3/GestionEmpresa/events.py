import sys

import var


class Eventos:
    def Salir():
        try:
            var.dialogoSalir.show()
            if var.dialogoSalir.exec():
                sys.exit()
            else:
                var.dialogoSalir.hide()
        except Exception as error:
            print("Error %s: " % str(error))