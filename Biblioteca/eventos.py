import var

class Calendario:

    def abrirCalendarioPrestamo(self):
        try:
            var.uiCalendarioPrestamo.show()
        except Exception as error:
            print('Error abrir calendario: %s' % str(error))

    def abrirCalendarioDevolucion(self):
        try:
            var.uiCalendarioDevolucion.show()
        except Exception as error:
            print('Error abrir calendario: %s' % str(error))

    def abrirCalendarioSancion(self):
        try:
            var.uiCalendarioSancion.show()
        except Exception as error:
            print('Error abrir calendario: %s' % str(error))

    def cargarFechaDesde(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.lineEditFechaDesde.setText(str(data))
            var.uiCalendarioPrestamo.hide()
        except Exception as error:
            print('Error cargar fecha prestamo: %' % str(error))

    def cargarFechaHasta(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.addDays(15).day(), qDate.addDays(15).month(), qDate.addDays(15).year()))
            var.ui.textBrowserFechaHasta.setText(str(data))
        except Exception as error:
            print('Error cargar fecha devolución: %s' % str(error))

    def cargarFechaDevolucion(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.lineEditFechaDevolucion.setText(str(data))
            var.uiCalendarioDevolucion.hide()
        except Exception as error:
            print('Error cargar fecha devolución: %' % str(error))

    def cargarFechaSancion(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.lineEditSancionHasta.setText(str(data))
            var.uiCalendarioSancion.hide()
        except Exception as error:
            print('Error cargar fecha sancion: %' % str(error))

