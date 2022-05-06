import os.path
import shutil
import sys
import zipfile
import shutil

#import xlrd

import clientes
import var
from datetime import datetime
import conexion
from PyQt5 import QtCore, QtGui, QtWidgets


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

    def AbrirDir(self):
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print('Error abrir explorador: %s ' % str(error))

    def Backup():
        try:
            fecha=datetime.today()
            fecha=fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia=(str(fecha)+'backup.zip')
            option=QtWidgets.QFileDialog.Options()
            directorio, filename= var.filedlgabrir.getSaveFileName(None,'Guardar Copia',var.copia,'.zip',options=option)
            if var.filedlgabrir.Accepted and filename !='':
                ficheroZip=zipfile.ZipFile(var.copia,'w')
                ficheroZip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                ficheroZip.close()
                var.ui.tbEstado.setText('BASE DE DATOS COPIADA A ARCHIVO ZIP')
                shutil.move(str(var.copia),str(directorio))
        except Exception as error:
            print('Error al comprimir: %s' % str(error))

    def importarBaseDatos(self):
        try:
            option=QtWidgets.QFileDialog.Options()
            filename=var.filedlgabrir.getOpenFileName(None,'Restaurar copia','','*.db',options=option)
            db=str(filename[0])
            if var.filedlgabrir.Accepted and filename != '' and db.endswith('.db'):
                var.filedb=db
                conexion.Conexion.db_connect(var.filedb)
                var.ui.tbEstado.setText('BASE DE DATOS %s RECUPERADA' % db)
                conexion.Conexion.mostrarClientes(self)
            else:
                conexion.Conexion.mostrarClientes(self)
                var.ui.tbEstado.setText('NO ES UNA BASE DE DATOS')
                print('NO ES UNA BASE DE DATOS')
        except Exception as error:
            print('Error importar base de datos: %s' % str(error))


    def recuperarBackup(self):
        try:
            option=QtWidgets.QFileDialog.Options()
            filename=var.filedlgabrir.getOpenFileName(None,'Restaurar copia','','*.zip',options=option)
            db=str(filename[0])
            if var.filedlgabrir.Accepted and filename != '' and db.endswith('.zip'):
                nuevaCarpeta=db.__add__('s')
                shutil.unpack_archive(db, nuevaCarpeta, 'zip')
                directorio=os.path.basename(nuevaCarpeta)
                archivo = os.listdir(directorio)
                var.filedb=archivo[0]
                conexion.Conexion.db_connect(var.filedb)
                var.ui.tbEstado.setText('BASE DE DATOS %s RECUPERADA' % db)
                conexion.Conexion.mostrarClientes(self)
            else:
                conexion.Conexion.mostrarClientes(self)
                var.ui.tbEstado.setText('EL BACKUP DEBE SER UN ARCHIVO ZIP')
                print('EL BACKUP DEBE SER UN ARCHIVO ZIP')
        except Exception as error:
            print('Error recuperar zip base de datos: %s' % str(error))


    '''def mostarDatosXLS(self):

        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.filedlgabrir.getOpenFileName(None, 'Restaurar copia', '', '*.xls', options=option)
            archivo = str(filename[0])
            if var.filedlgabrir.Accepted and filename != '' and archivo.endswith('.xls'):
                documento = xlrd.open_workbook(archivo)
                hojaClientes = documento.sheet_by_index(0)
                filas_clientes = hojaClientes.nrows
                columnas_clientes = hojaClientes.ncols

                if columnas_clientes >= 3:
                    i=0
                    j=0
                    while i < filas_clientes:
                        while j < 3:
                            campo=hojaClientes.cell_value(i,j)
                            var.ui.cliTabla.setRowCount(i+1)  # Crea la fila y a continuación mete los datos
                            var.ui.cliTabla.setItem(i,j, QtWidgets.QTableWidgetItem(campo))
                            j=j+1
                        j=0
                        i=i+1
                    var.ui.tbEstado.setText('DATOS DEL ARCHIVO %s MOSTRADOS' % archivo)
                    print('DATOS .XLS MOSTRADOS')
                    conexion.Conexion.db_desconectar(self)
                else:
                    var.ui.tbEstado.setText('EL NÚMERO DE FILAS DEL ARCHIVO .XLS NO ES COMPATIBLE')
                    print('EL NÚMERO DE FILAS DEL ARCHIVO .XLS NO ES COMPATIBLE')
            else:
                conexion.Conexion.mostrarClientes(self)
                var.ui.tbEstado.setText('LOS DATOS A MOSTRAR DEBEN SER DE UN ARCHIVO .XLS')
                print('LOS DATOS IMPORTADOS DEBEN SER DE UN ARCHIVO .XLS')
        except Exception as error:
            print('Error al mostrar datos xls: %s' % str(error))

    def importarDatosXLS(self):

        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.filedlgabrir.getOpenFileName(None, 'Restaurar copia', '', '*.xls', options=option)
            archivo = str(filename[0])
            if var.filedlgabrir.Accepted and filename != '' and archivo.endswith('.xls'):
                documento = xlrd.open_workbook(archivo)
                hojaClientes = documento.sheet_by_index(0)
                filas_clientes = hojaClientes.nrows
                columnas_clientes = hojaClientes.ncols

                i=0
                j=0
                while i < filas_clientes:
                    cliente=[]
                    while j < columnas_clientes:
                        campo=hojaClientes.cell_value(i,j)
                        cliente.append(campo)
                        j=j+1
                    conexion.Conexion.cargarCliente(cliente)
                    j=0
                    i=i+1
                var.ui.tbEstado.setText('DATOS DEL ARCHIVO %s  HAN SIDO IMPORTADOS' % archivo)
                print('DATOS .XLS IMPORTADOS')

            else:
                conexion.Conexion.mostrarClientes(self)
                var.ui.tbEstado.setText('LOS DATOS IMPORTADOS DEBEN SER DE UN ARCHIVO .XLS')
                print('LOS DATOS IMPORTADOS DEBEN SER DE UN ARCHIVO .XLS')
        except Exception as error:
            var.ui.tbEstado.setText('EL NÚMERO DE FILAS DEL ARCHIVO .XLS NO ES COMPATIBLE CON LA BASE DE DATOS ACTUAL')
            print('EL NÚMERO DE FILAS DEL ARCHIVO .XLS NO ES COMPATIBLE')
            print('Error importando datos xls: %s' % str(error))'''

