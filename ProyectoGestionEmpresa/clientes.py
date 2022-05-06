from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets

import conexion
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
                    var.ui.tbEstado.setText("DNI CORRECTO")
                    var.ui.lblValidarDNI.setStyleSheet('QLabel {color:green;font-size:14pt;font-weight:bold}')
                    var.ui.lblValidarDNI.setFont(QFont("Forte"))
                    var.ui.lblValidarDNI.setText('V')
                    return True
                else:
                    print("DNI INCORRECTO")
                    var.ui.tbEstado.setText("DNI INCORRECTO")
                    var.ui.lblValidarDNI.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                    var.ui.lblValidarDNI.setFont(QFont("Forte"))
                    var.ui.lblValidarDNI.setText('X')
                    return False
            else:
                print("DNI INCORRECTO")
                var.ui.tbEstado.setText("DNI INCORRECTO")
                var.ui.lblValidarDNI.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                var.ui.lblValidarDNI.setFont(QFont("Forte"))
                var.ui.lblValidarDNI.setText('X')
                return False
        except Exception as error:
            print("Error %s: " % str(error))


    def selSexo(self):
        try:
            global sex
            if var.ui.rbMujer.isChecked():
                #print('marcado muller')
                sex='Mujer'
            if var.ui.rbHombre.isChecked():
                #print('marcado home')
                sex='Hombre'
        except Exception as error:
            print('Error en módulo seleccionar sexo:',error)

    def selPago():
        try:
            var.pay = []
            for i, data in enumerate(var.ui.bgPago.buttons()):
                #los checkbox han sido agrupados en un BUttonGroup en Qt Designer
                if data.isChecked() and i==0:
                    print('pagas con tansferencia')
                    var.pay.append('Transferencia')
                if data.isChecked() and i==1:
                    print('pagas con efectivo')
                    var.pay.append('Efectivo')
                if data.isChecked() and i==2:
                    print('pagas con tarjeta')
                    var.pay.append('Tarjeta')
            print(var.pay)
            return var.pay
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

    def seleccionarFormaEnvio(self):
        try:
            indexEnvio = var.ui.sbEnvio.value()
            envio = ['RECOGIDA POR CLIENTE', 'ENVÍO NACIONAL PAQUETERÍA URGENTE', 'ENVÍO NACIONAL PAQUETERÍA NORMAL',
                     'ENVÍO INTERNACIONAL']
            var.formaEnvio = envio[indexEnvio]
            var.ui.lblEnvio.setText(var.formaEnvio)
            var.ui.tbEstado.setText(var.formaEnvio)
        except Exception as error:
            print('Error seleccionar envío: %s' % str(error))


    def altaClientes(self):
        if Clientes.validarDNI():
            try:
                # Preparamos el registro
                nuevoCli = []
                clitab= []
                #cliente = [var.ui.leDNI, var.ui.leApellidos, var.ui.leNombre, var.ui.leFecha, var.ui.leDireccion]
                cliente = [var.ui.leDNI, var.ui.leApellidos, var.ui.leNombre, var.ui.leDireccion]
                k = 0
                for i in cliente:
                    nuevoCli.append(i.text())
                    #cargaremos los valores para la tabla que solo tiene DNI, Apelidos y Nome
                    # #if k < 3:
                    if k < 6:
                        clitab.append(i.text())
                        k += 1
                nuevoCli.append(var.formaEnvio)
                nuevoCli.append(vprov)
                nuevoCli.append(sex)
                var.pay2 = Clientes.selPago()
                nuevoCli.append(var.pay2)
                nuevoCli.append(var.ui.leFecha.text())

                conexion.Conexion.cargarCliente(nuevoCli)
                conexion.Conexion.mostrarClientes(self)

            except Exception as error:
                var.ui.tbEstado.setText("DEBE CUBRIR LOS CAMPOS OBLIGATORIOS")
                print('Error alta cliente: %s ' % str(error))

    def limpiarCliente(self):
        var.ui.leDNI.setText("")
        var.ui.leFecha.setText("")
        var.ui.leApellidos.setText("")
        var.ui.leNombre.setText("")
        var.ui.leDireccion.setText("")
        var.ui.lblValidarDNI.setText("")
        var.ui.comBoxProvincia.setCurrentIndex(0)
        var.ui.sbEnvio.setValue(0)
        var.ui.tbEstado.setText("")
        #Así funciona!!
        var.ui.bgSexo.setExclusive(False)
        var.ui.rbHombre.setChecked(False)
        var.ui.rbMujer.setChecked(False)
        var.ui.bgSexo.setExclusive(True)

        var.ui.bgPago.setExclusive(False)
        var.ui.cbTransferencia.setChecked(False)
        var.ui.cbTarjeta.setChecked(False)
        var.ui.cbEfectivo.setChecked(False)
        var.ui.bgPago.setExclusive(True)


    def bajaCliente(self):
        '''Módulos para dar de baja un cliente
        :return:'''
        try:
            dni = var.ui.leDNI.text()
            if (conexion.Conexion.existeCliente(dni)):
                conexion.Conexion.bajaCliente(dni)
                conexion.Conexion.mostrarClientes(self)
                Clientes.limpiarCliente(self)
                var.ui.tbEstado.setText("CLIENTE DNI '" + dni + "' HA SIDO DADO DE BAJA")
            else:
                print('NO EXISTE EL CLIENTE')
                if var.ui.leDNI.text()=='':
                    var.ui.tbEstado.setText("NO HA INTRODUCIDO NINGÚN DNI")
                else:
                    var.ui.tbEstado.setText("CLIENTE DNI '" + dni + "' NO EXISTE EN LA BD")
        except Exception as error:
            print('Error baja clientes: %s' % str(error))

    def modificarCliente(self):
        '''módulos para modificar datos de un cliente
        :return:
        '''
        try:
            newdata=[]
            cliente=[var.ui.leDNI, var.ui.leApellidos,var.ui.leNombre, var.ui.leDireccion]
            if (conexion.Conexion.existeCliente(cliente[0].text())):
                for i in cliente:
                    newdata.append(i.text())
                newdata.append(var.formaEnvio)
                newdata.append(var.ui.comBoxProvincia.currentText())
                newdata.append(sex)
                var.pay=Clientes.selPago()
                newdata.append(var.pay)
                newdata.append(var.ui.leFecha.text())

                conexion.Conexion.modificarCliente(newdata)
                conexion.Conexion.mostrarClientes(self)
            else:
                print('NO EXISTE EL CLIENTE')
                if var.ui.leDNI.text() == '':
                    var.ui.tbEstado.setText("NO HA INTRODUCIDO NINGÚN DNI")
                else:
                    var.ui.tbEstado.setText("CLIENTE DNI '" + cliente[0].text()+ "' NO EXISTE EN LA BD")
        except Exception as error:
            var.ui.tbEstado.setText("DEBE CUBRIR LOS CAMPOS OBLIGATORIOS")
            print('Error modificando cliente: %s' % str(error))




