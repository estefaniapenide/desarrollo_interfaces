from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets

import var
from dni import Dni
import datetime
from datetime import *


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
                    var.ui.lblValidarDni.setStyleSheet('QLabel {color:blue;font-size:14pt;font-weight:bold}')
                    var.ui.lblValidarDni.setFont(QFont("Forte"))
                    var.ui.lblValidarDni.setText('V')


                else:
                    print("DNI INCORRECTO")
                    var.ui.lblValidarDni.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                    var.ui.lblValidarDni.setFont(QFont("Forte"))
                    var.ui.lblValidarDni.setText('X')

            else:
                print("DNI INCORRECTO")
                var.ui.lblValidarDni.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                var.ui.lblValidarDni.setFont(QFont("Forte"))
                var.ui.lblValidarDni.setText('X')
        except Exception as error:
            print("Error %s: " % str(error))


    def selTransaccion(self):
        try:
            global transaccion
            if var.ui.rbIngresar.isChecked():
                print('marcado ingresar')
                transaccion=True
            if var.ui.rbRetirar.isChecked():
                print('marcado retirar')
                transaccion=False
        except Exception as error:
            print('Error en módulo seleccionar transacción:',error)

    def operacion():
        try:
            var.cantidad = int(var.ui.leCantidad.text())
            if(transaccion==True):
                var.saldo=var.saldo+var.cantidad
                var.ui.textEditSaldo.setText(str(var.saldo))
            elif(transaccion==False):
                var.saldo=var.saldo-var.cantidad
                var.ui.textEditSaldo.setText(str(var.saldo))
            else:
                var.saldo=var.saldo
                var.ui.textEditSaldo.setText(str(var.saldo))
        except Exception as error:
            print('Error en el modulo operación: ',error)

    def abrirCalendario(self):
        try:
            var.dlgCalendario.show()
        except Exception as error:
            print('Error: %s' % str(error))

    def edad(qDate):
        try:
            #global age
            today = datetime.now()
            var.age = today.year - qDate.year() - ((today.month, today.day) < (qDate.month(), qDate.day()))
            print(var.age)
        except Exception as error:
            print('Error en el modulo de edad: ',error)

    def cargarFecha(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            if var.age <= 18:
                var.dlgEdad.show()
                var.ui.leFecha.setText("")
                var.ui.leDNI.setText("")
                var.ui.leApellido1.setText("")
                var.ui.leApellido2.setText("")
                var.ui.leNombre.setText("")
                var.ui.leCantidad.setText("")
            else:
                var.ui.leFecha.setText(str(data))
            var.dlgCalendario.hide()
        except Exception as error:
            print('Error: %' % str(error))

    def comprobacion():
        if (var.ui.lblValidarDni.text()=="" or var.ui.lblValidarDni.text()=="X") or var.ui.leFecha.text()=="":
            var.info=False
            print('FALTAN EL DNI O AL FECHA DE NACIMIENTO')
        else:
            var.info=True


