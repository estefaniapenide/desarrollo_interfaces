import var

class Eventos():

    def Saludo():
        try:
            var.ui.lblPulsa.setGeometry(235, 90, 196, 41)
            var.ui.lblPulsa.setText('<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00ff00;\">HAS PULSADO EL BOTÓN</span></p></body></html>')
        except Exception as error:
            print('Error: %s ' % str(error))
