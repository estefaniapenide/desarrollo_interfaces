from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets

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


    def selSexo(self):
        try:
            global sex
            if var.ui.rbMujer.isChecked():
                #print('marcado muller')
                sex='Muller'
            if var.ui.rbHombre.isChecked():
                #print('marcado home')
                sex='Home'
        except Exception as error:
            print('Error en módulo seleccionar sexo:',error)

    def selPago(self):
        try:
            var.pay = []
            if var.ui.cbEfectivo.isChecked():
                print('pagas con efectivo')
                var.pay.append('Efectivo')
            if var.ui.cbTarjeta.isChecked():
                print('pagas con tajeta')
                var.pay.append('Tarxeta')
            if var.ui.cbTransferencia.isChecked():
                print('pagas con transferencia')
                var.pay.append('Transferencia')
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarPovincia():
        try:
            prov=['','A Coruña','Lugo','Ourense','Pontevedra']
            for i in prov:
                var.ui.comBoxProvincia.addItem(i)
        except Exception as error:
            print('Error: %s'% str(error))

    def seleccionarProvincia(prov):
        try:
            global vprov
            #print('Has seleccionado la provincia de ',prov)
            vprov=prov
        except Exception as error:
            print('Error: %s' % str(error))

    def abrirCalendario(self):
        try:
            var.dlgCalendario.show()
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarFecha(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.leFecha.setText(str(data))
            var.dlgCalendario.hide()
        except Exception as error:
            print('Error: %' % str(error))

    '''def mostrarClientes():
        try:
            #Preparamos el registro
            nuevoCli = []
            cliente =[var.ui.leDNI, var.ui.leApellidos, var.ui.leNombre, var.ui.leFecha,var.ui.leDireccion ]
            for i in cliente:
                nuevoCli.append(i.text())
            nuevoCli.append(vprov)
            nuevoCli.append(sex)
            #elimina duplicados
            var.pay = set(var.pay)
            for j in var.pay:
                nuevoCli.append(j)
            print(nuevoCli)
        except Exception as error:
            print('Error: %s '%str(error))'''

    def mostrarClientes():
        try:
            # Preparamos el registro
            nuevoCli = []
            clitab= []
            cliente = [var.ui.leDNI, var.ui.leApellidos, var.ui.leNombre, var.ui.leFecha, var.ui.leDireccion]
            k = 0
            for i in cliente:
                nuevoCli.append(i.text())
                #cargaremos los valores para la tabla que solo tiene DNI, Apelidos y Nome
                if k < 3:
                    clitab.append(i.text())
                    k += 1
            nuevoCli.append(vprov)
            nuevoCli.append(sex)
            # elimina duplicados
            var.pay = set(var.pay)
            for j in var.pay:
                nuevoCli.append(j)
            print(nuevoCli)
            print(clitab)
            row = 0  #posición de la fila, problema: coloca al último comoprimero en cada click
            column = 0  #posición de la columna
            var.ui.cliTabla.insertRow(row) #insertamos una fila nueva con cada click de botón
            for registro in clitab:
                #la celda tiene una posición fila, columna y cragamos en ella el dato
                cell= QtWidgets.QTableWidgetItem(registro) #carga en cell cada dato de la lista
                var.ui.cliTabla.setItem(row,column,cell) #lo escribe
                column += 1
        except Exception as error:
            print('Error: %s ' % str(error))

