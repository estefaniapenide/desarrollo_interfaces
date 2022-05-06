from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets

import var
from dni import Dni

class Clientes:

    def validarDNI():
        try:
            dni=var.ui.lineEditDni.text()
            var.ui.lineEditDni.setText(dni.upper())

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
                    var.ui.labelValidarDni.setStyleSheet('QLabel {color:green;font-size:14pt;font-weight:bold}')
                    var.ui.labelValidarDni.setFont(QFont("Forte"))
                    var.ui.labelValidarDni.setText('V')


                else:
                    print("DNI INCORRECTO")
                    var.ui.labelValidarDni.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                    var.ui.labelValidarDni.setFont(QFont("Forte"))
                    var.ui.labelValidarDni.setText('X')

            else:
                print("DNI INCORRECTO")
                var.ui.labelValidarDni.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                var.ui.labelValidarDni.setFont(QFont("Forte"))
                var.ui.labelValidarDni.setText('X')


        except Exception as error:
            print("Error %s: " % str(error))


    def seleccionarSexo():
        global sexo
        try:
           if var.ui.radioButtonHombre_2.isChecked():
                print('marcado masculino')
                sexo='Mujer'
           elif var.ui.radioButtonMujer_2.isChecked():
                print('marcado femenino')
                sexo='Hombre'
        except Exception as error:
            print('Error en el módulo de seleccionar sexo: %s' % str(error))


    def seleccionarPago():
        try:
            var.pago = []
            if var.ui.checkBoxTrajeta_2.isChecked():
                print('pago con tarjeta')
                var.pago.append('Trajeta')
            if var.ui.checkBoxTransferencia_2.isChecked():
                print('pago con transferencia')
                var.pago.append('Transferencia')
            if var.ui.checkBoxEfectivo_2.isChecked():
                print('pago en efectivo')
                var.pago.append('Efectivo')
        except Exception as error:
            print('Error en el módulo de pago: %s' % str(error))

    def cargarProvincia():
        try:
            provincia=['','A Coruña','Pontevedra','Lugo','Ourense']
            for i in provincia:
                var.ui.comboBoxProvincia.addItem(i)
        except Exception as error:
            print('Error en módulo provincia: %s' % str(error))


    def selccionarProvincia(provincia):
        global prov
        try:
            print('Has seleccionado la provincia de ',provincia)
            prov=provincia
        except Exception as error:
            print('Error en el módulo provincia: %s' % str(error))


    def abrirCalendario():
        try:
            var.dialogoCalendario.show()
        except Exception as error:
            print('Error en el múdolo calendario: %s' % str(error))


    def cargarFecha(qDate):
        try:
            fecha=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.lineEditFecha.setText(str(fecha))
            var.dialogoCalendario.hide()
        except Exception as error:
            print('Error en el módulo calendario: %s' % str(error))


    '''def mostrarClientes():
        try:
            nuevoCliente=[]
            cliente=[var.ui.lineEditDni, var.ui.lineEditApellidos, var.ui.lineEditNombre, var.ui.lineEditFecha, var.ui.lineEditDireccion]
            for i in cliente:
                nuevoCliente.append(i.text())
            nuevoCliente.append(prov)
            #ELIMINA DUPLICADOS
            var.pago = set(var.pago)
            for j in var.pago:
                nuevoCliente.append(j)
            nuevoCliente.append(sexo)
            print(nuevoCliente)
        except Exception as error:
            print('Error %s' % str(error))'''



    def mostrarClientes():
        try:
            nuevoCliente = []
            clienteTabla = []
            cliente = [var.ui.lineEditDni, var.ui.lineEditApellidos, var.ui.lineEditNombre, var.ui.lineEditFecha, var.ui.lineEditDireccion]
            k = 0
            for i in cliente:
                nuevoCliente.append(i.text())
                if k < 5:
                    clienteTabla.append(i.text())
                    k += 1
            nuevoCliente.append(prov)
            #ELIMINA DUPLICADOS
            var.pago = set(var.pago)
            for j in var.pago:
                nuevoCliente.append(j)
            nuevoCliente.append(sexo)
            print(nuevoCliente)
            print(clienteTabla)

            row = 0
            column = 0
            var.ui.tablaClientes.insertRow(row)
            for registro in clienteTabla:
                celda = QtWidgets.QTableWidgetItem(registro)
                var.ui.tablaClientes.setItem(row, column, celda)
                column += 1
        except Exception as error:
            print('Error %s' % str(error))