from PyQt5 import QtWidgets, QtSql

import clientes
import conexion
import var

class Conexion():

    def db_connect(filename):

        db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None,'No se puede abrir la base de datos',
                                           'No se puede establecer conexión.\n' 'Haz Click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión establecida')
            return True

    def db_desconectar(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        if db.open():
            db.close()


    def cargarCliente(cliente):
        query=QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apellidos, nombre, direccion, formaEnvio, provincia, sexo, formapago, fechaAlta)'
                      'VALUES (:dni, :apellidos, :nombre, :direccion, :formaEnvio, :provincia, :sexo, :formapago, :fechaAlta)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':direccion', str(cliente[3]))
        query.bindValue(':formaEnvio', str(cliente[4]))
        query.bindValue(':provincia', str(cliente[5]))
        query.bindValue(':sexo', str(cliente[6]))
        #pagos = ' '.join(cliente[7]) si queremos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formapago', str(cliente[7]))
        query.bindValue(':fechaAlta', str(cliente[8]))

        if query.exec_():
            var.ui.tbEstado.setText("CLIENTE DNI '" +cliente[0] + "' HA SIDO DADO DE ALTA")
            print('Insercción correcta')
            Conexion.mostrarClientes(cliente)
        else:
            var.ui.tbEstado.setText("CLIENTE DNI '" + cliente[0] + "' YA EXISTE EN LA BD")
            print('Error carga de cliente: ', query.lastError().text())


    def mostrarClientes(self):
        index = 0
        query =QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                var.ui.cliTabla.setRowCount(index+1)#Crea la fila y a continuación mete los datos
                var.ui.cliTabla.setItem(index,0, QtWidgets.QTableWidgetItem(dni))
                var.ui.cliTabla.setItem(index,1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.cliTabla.setItem(index,2, QtWidgets.QTableWidgetItem(nombre))
                index +=1
        else:
            var.ui.tbEstado.setText("BASE DE DATOS NO COMPATIBLE")
            var.ui.cliTabla.setRowCount(1)  # Crea la fila y a continuación mete los datos
            var.ui.cliTabla.setItem(index, 0, QtWidgets.QTableWidgetItem(""))
            var.ui.cliTabla.setItem(index, 1, QtWidgets.QTableWidgetItem(""))
            var.ui.cliTabla.setItem(index, 2, QtWidgets.QTableWidgetItem(""))
            print('Error mostrar clientes: ',query.lastError().text())

    def existeCliente(id):
        try:
            salida=False
            query = QtSql.QSqlQuery()
            query.prepare('select dni from clientes')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    if(dni==id):
                        salida=True
            return salida
        except Exception as error:
            print('Error existe cliente: %s' % str(error))


    def bajaCliente(dni):
        '''Módulo para eliminar cliente. Se llama desde fichero clientes.py
        :return None'''
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            print('Baja cliente')
        else:
            print('Error baja clientes: ', query.lastError().text())


    def buscarCliente(self):
        '''row = 0
        while row < var.ui.cliTabla.rowCount():
            var.ui.cliTabla.removeRow(row)
            row += 1'''
        global dni
        global apellidos
        global nombre
        global direccion
        global envio
        global provincia
        global sexo
        global formapago
        global fechaAlta

        id = var.ui.leDNI.text()
        if conexion.Conexion.existeCliente(id):
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, direccion, formaEnvio, provincia, sexo, formapago, fechaAlta from clientes where dni=:dni')
            query.bindValue(':dni', id)
            if query.exec_():
               while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    direccion=query.value(3)
                    envio= query.value(4)
                    provincia=query.value(5)
                    sexo=query.value(6)
                    formapago=query.value(7)
                    fechaAlta=query.value(8)
                    var.ui.cliTabla.setRowCount(index + 1)  # Crea la fila y a continuación mete los datos
                    var.ui.cliTabla.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.cliTabla.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.cliTabla.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    index += 1
            else:
                print('Error buscar cliente: ', query.lastError().text())

            clientes.Clientes.limpiarCliente(self)

            var.ui.leDNI.setText(dni)
            var.ui.leApellidos.setText(apellidos)
            var.ui.leNombre.setText(nombre)
            var.ui.lblValidarDNI.setText("")
            var.ui.leDireccion.setText(direccion)
            var.ui.leFecha.setText(fechaAlta)

            if(envio=='RECOGIDA POR CLIENTE'):
                var.ui.sbEnvio.setValue(0)
            elif(envio=='ENVÍO NACIONAL PAQUETERÍA URGENTE'):
                var.ui.sbEnvio.setValue(1)
            elif (envio == 'ENVÍO NACIONAL PAQUETERÍA NORMAL'):
                var.ui.sbEnvio.setValue(2)
            elif (envio == 'ENVÍO INTERNACIONAL'):
                var.ui.sbEnvio.setValue(3)

            if(provincia==""):
                var.ui.comBoxProvincia.setCurrentIndex(0)
            elif(provincia=="A Coruña"):
                var.ui.comBoxProvincia.setCurrentIndex(1)
            elif (provincia == "Lugo"):
                var.ui.comBoxProvincia.setCurrentIndex(2)
            elif (provincia == "Ourense"):
                var.ui.comBoxProvincia.setCurrentIndex(3)
            elif (provincia == "Pontevedra"):
                var.ui.comBoxProvincia.setCurrentIndex(4)

            if(sexo=="Mujer"):
                var.ui.rbMujer.click()
            elif(sexo=="Hombre"):
                var.ui.rbHombre.click()

            if formapago=="['Efectivo']":
                var.ui.cbEfectivo.setChecked(True)
            elif  formapago=="['Tarjeta']":
                var.ui.cbTarjeta.setChecked(True)
            elif  formapago=="['Transferencia']":
                var.ui.cbTransferencia.setChecked(True)
            else:
                print("No tiene forma de pago asignada")


            var.ui.tbEstado.setText('CLIENTE DNI %s ENCONTRADO' % id)
        else:
            clientes.Clientes.limpiarCliente(self)
            var.ui.leDNI.setText(id)
            var.ui.tbEstado.setText('CLIENTE DNI %s NO ENCONTRADO' % id)
            var.ui.leDNI.setText(id)


    def modificarCliente(modificacion):
        dni = modificacion[0]
        query=QtSql.QSqlQuery()
        query.prepare('update clientes set apellidos=:apellidos, nombre=:nombre, direccion=:direccion,formaEnvio=:formaEnvio, provincia=:provincia, sexo=:sexo, formapago=:formapago, fechaAlta=:fechaAlta where dni=:dni')
        query.bindValue(':dni', str(dni))
        query.bindValue(':apellidos', str(modificacion[1]))
        query.bindValue(':nombre', str(modificacion[2]))
        query.bindValue(':direccion', str(modificacion[3]))
        query.bindValue(':formaEnvio', str(modificacion[4]))
        query.bindValue(':provincia', str(modificacion[5]))
        query.bindValue(':sexo', str(modificacion[6]))
        query.bindValue(':formapago', str(modificacion[7]))
        query.bindValue(':fechaAlta', str(modificacion[8]))
        if query.exec_():
            print('CLIENTE MODIFICADO')
            var.ui.tbEstado.setText('CLIENTE DNI %s HA SIDO MODIFICADO' % dni)
        else:
            print('Error modificar cliente: ',query.lastError().text())





