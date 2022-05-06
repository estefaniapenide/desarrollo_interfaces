from PyQt5.QtGui import QFont

import var
from dni import Dni



class Clientes:

    def validarDNI():
        try:
            dni=var.ui.leDNI.text()
            var.ui.leDNI.setText(dni.upper())

            if (len(dni) == 9):
                numero = ""
                i = 0
                while (i < 8):
                    numero = numero + dni[i]
                    i += 1
                letra = dni[8]
                letra=letra.upper()
                dniCorrecto = Dni(numero)
                if (dniCorrecto.letra == letra):
                    print("DNI CORRECTO")
                    var.ui.lblValidarDNI.setStyleSheet('QLabel {color:green;font-size:14pt;font-weight:bold}')
                    var.ui.lblValidarDNI.setFont(QFont("Forte"))
                    var.ui.lblValidarDNI.setText('V')


                else:
                    print("DNI INCORRECTO")
                    var.ui.lblValidarDNI.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                    var.ui.lblValidarDNI.setFont(QFont("Forte"))
                    var.ui.lblValidarDNI.setText('X')

            else:
                print("DNI INCORRECTO")
                var.ui.lblValidarDNI.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                var.ui.lblValidarDNI.setFont(QFont("Forte"))
                var.ui.lblValidarDNI.setText('X')


        except Exception as error:
            print("Error %s: " % str(error))