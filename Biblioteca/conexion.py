from PyQt5 import QtWidgets, QtSql
import var

class Conexion:

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


#CONEXION DE LOS LIBROS
class Libros:

    def libroDisponible(codigoLibro):
        try:
            disponible=False
            query = QtSql.QSqlQuery()
            query.prepare('select estado from libros where codigo=:codigo')
            query.bindValue(':codigo', codigoLibro)
            if query.exec_():
                while query.next():
                    estado = str(query.value(0))
                    if(estado=='DISPONIBLE'):
                        disponible=True
            return disponible
        except Exception as error:
            print('Error disponibilidad libro: %s' % str(error))

    def modificarDisponibilidadLibro(codigoLibro, devuelto):#'comprobar que esto funciona bien'
        print('comprobar que esto funciona bien')
        if devuelto == 'False':
            estadoLibro='PRESTADO'
        elif devuelto == 'True':
            estadoLibro='DISPONIBLE'

        query = QtSql.QSqlQuery()
        query.prepare(
            'update libros set estado=:estado where codigo=:codigo')
        query.bindValue(':codigo', codigoLibro)
        query.bindValue(':estado', estadoLibro)
        if query.exec_():
            print('LIBRO MODIFICADO')
            # var.ui.tbEstado.setText('LIBRO CON CODIGO %s HA SIDO MODIFICADO' % codigo)
        else:
            print('Error modificar libro: ', query.lastError().text())

    def guardarLibro(libro):
        query=QtSql.QSqlQuery()
        query.prepare('insert into libros (estado, titulo, autor, genero, etiquetas)'
                      'VALUES (:estado, :titulo, :autor, :genero,:etiquetas)')
        query.bindValue(':estado', str(libro[0]))
        query.bindValue(':titulo', str(libro[1]))
        query.bindValue(':autor', str(libro[2]))
        query.bindValue(':genero', str(libro[3]))
        query.bindValue(':etiquetas', str(libro[4]))

        if query.exec_():
            #var.ui.tbEstado.setText("CLIENTE DNI '" +cliente[0] + "' HA SIDO DADO DE ALTA")
            print('Insercción de libro correcta')
            Libros.mostrarLibros(libro)
        else:
            #var.ui.tbEstado.setText("CLIENTE DNI '" + cliente[0] + "' YA EXISTE EN LA BD")
            print('Error guardar libro: ', query.lastError().text())

    def bajaLibro(codigo):
        query = QtSql.QSqlQuery()
        query.prepare('delete from libros where codigo = :codigo')
        query.bindValue(':codigo', codigo)
        if query.exec_():
            print('Libro eliminado')
        else:
            print('Error baja libro: ', query.lastError().text())

    def modificarLibro(modificacion):
        codigo = modificacion[0]
        query=QtSql.QSqlQuery()
        query.prepare('update libros set estado=:estado, titulo=:titulo, autor=:autor,genero=:genero, etiquetas=:etiquetas where codigo=:codigo')
        query.bindValue(':codigo', str(codigo))
        query.bindValue(':estado', str(modificacion[1]))
        query.bindValue(':titulo', str(modificacion[2]))
        query.bindValue(':autor', str(modificacion[3]))
        query.bindValue(':genero', str(modificacion[4]))
        query.bindValue(':etiquetas', str(modificacion[5]))
        if query.exec_():
            print('LIBRO MODIFICADO')
            #var.ui.tbEstado.setText('LIBRO CON CODIGO %s HA SIDO MODIFICADO' % codigo)
        else:
            print('Error modificar libro: ',query.lastError().text())


    def mostrarLibros(self):
        index = 0
        query =QtSql.QSqlQuery()
        query.prepare('select codigo, estado, titulo, autor, genero from libros')
        if query.exec_():
            while query.next():
                codigo =str(query.value(0))
                estado = query.value(1)
                titulo = query.value(2)
                autor = query.value(3)
                genero = query.value(4)
                var.ui.tablaLibros.setRowCount(index+1)#Crea la fila y a continuación mete los datos
                var.ui.tablaLibros.setItem(index,0, QtWidgets.QTableWidgetItem(codigo))
                var.ui.tablaLibros.setItem(index,1, QtWidgets.QTableWidgetItem(estado))
                var.ui.tablaLibros.setItem(index,2, QtWidgets.QTableWidgetItem(titulo))
                var.ui.tablaLibros.setItem(index,3, QtWidgets.QTableWidgetItem(autor))
                var.ui.tablaLibros.setItem(index,4, QtWidgets.QTableWidgetItem(genero))
                index +=1
        else:
            #var.ui.tbEstado.setText("BASE DE DATOS NO COMPATIBLE")
            var.ui.tablaLibros.setRowCount(1)  # Crea la fila y a continuación mete los datos
            var.ui.tablaLibros.setItem(index, 0, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaLibros.setItem(index, 1, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaLibros.setItem(index, 2, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaLibros.setItem(index, 3, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaLibros.setItem(index, 4, QtWidgets.QTableWidgetItem(""))
            print('Error mostrar libros: ',query.lastError().text())

    def existeLibro(id):
        try:
            salida=False
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from libros')
            if query.exec_():
                while query.next():
                    codigo = str(query.value(0))
                    if(codigo==id):
                        salida=True
            return salida
        except Exception as error:
            print('Error existe libro: %s' % str(error))

    def existeLibroTitulo(id):
        try:
            salida=False
            query = QtSql.QSqlQuery()
            query.prepare('select titulo from libros')
            if query.exec_():
                while query.next():
                    titulo = query.value(0)
                    if(titulo==id):
                        salida=True
            return salida
        except Exception as error:
            print('Error existe libro titulo: %s' % str(error))

    def existeLibroAutor(id):
        try:
            salida=False
            query = QtSql.QSqlQuery()
            query.prepare('select autor from libros')
            if query.exec_():
                while query.next():
                    autor = query.value(0)
                    if(autor==id):
                        salida=True
            return salida
        except Exception as error:
            print('Error existe libro autor: %s' % str(error))

    def existeLibroGenero(id):
        try:
            salida=False
            query = QtSql.QSqlQuery()
            query.prepare('select genero from libros')
            if query.exec_():
                while query.next():
                    genero = query.value(0)
                    if(genero==id):
                        salida=True
            return salida
        except Exception as error:
            print('Error existe libro genero: %s' % str(error))

    def existeLibroEstado(id):
        try:
            salida=False
            query = QtSql.QSqlQuery()
            query.prepare('select estado from libros')
            if query.exec_():
                while query.next():
                    estado = query.value(0)
                    if(estado==id):
                        salida=True
            return salida
        except Exception as error:
            print('Error existe libro genero: %s' % str(error))

    def resultadosBusqueda(query):
        index = 0
        if query.exec_():
            while query.next():
                var.codigo = query.value(0)
                var.estado = query.value(1)
                var.titulo = query.value(2)
                var.autor = query.value(3)
                var.genero = query.value(4)
                var.etiqueta = query.value(5)

                var.ui.tablaLibros.setRowCount(index + 1)  # Crea la fila y a continuación mete los datos
                var.ui.tablaLibros.setItem(index, 0, QtWidgets.QTableWidgetItem(str(var.codigo)))
                var.ui.tablaLibros.setItem(index, 1, QtWidgets.QTableWidgetItem(var.estado))
                var.ui.tablaLibros.setItem(index, 2, QtWidgets.QTableWidgetItem(var.titulo))
                var.ui.tablaLibros.setItem(index, 3, QtWidgets.QTableWidgetItem(var.autor))
                var.ui.tablaLibros.setItem(index, 4, QtWidgets.QTableWidgetItem(var.genero))
                index += 1
        else:
            print('Error buscar libro: ', query.lastError().text())

    def buscarLibroCodigo(id):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'select codigo, estado, titulo, autor, genero, etiquetas from libros where codigo=:codigo')
            query.bindValue(':codigo', id)
            Libros.resultadosBusqueda(query)
        except Exception as error:
            print('Error buscar libro: %s' % str(error))

    def buscarLibroTitulo(titulo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'select codigo, estado, titulo, autor, genero, etiquetas from libros where titulo=:titulo')
            query.bindValue(':titulo', titulo)
            Libros.resultadosBusqueda(query)
        except Exception as error:
            print('Error buscar libro titulo: %s' % str(error))

    def buscarLibroAutor(autor):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'select codigo, estado, titulo, autor, genero, etiquetas from libros where autor=:autor')
            query.bindValue(':autor', autor)
            Libros.resultadosBusqueda(query)
        except Exception as error:
            print('Error buscar libro autor: %s' % str(error))


    def buscarLibroGenero(genero):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'select codigo, estado, titulo, autor, genero, etiquetas from libros where genero=:genero')
            query.bindValue(':genero', genero)
            Libros.resultadosBusqueda(query)
        except Exception as error:
            print('Error buscar libro genero: %s' % str(error))

    def buscarLibroEstado(estado):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'select codigo, estado, titulo, autor, genero, etiquetas from libros where estado=:estado')
            query.bindValue(':estado', estado)
            Libros.resultadosBusqueda(query)
        except Exception as error:
            print('Error buscar libro estado: %s' % str(error))


#CONEXIÓN DE LOS SOCIOS
class Socios:

    def actualizarSocios(self):
        print('Pendiente')

    #No dejar que los socios cojan más de 3 libros #Creo que ya lo controlé en gyuardarPrestamo

    def modificarNumeroLibrosSocio(numSocio):
        query1 = QtSql.QSqlQuery()
        query1.prepare('select numLibros from socios where numSocio=:numSocio')
        query1.bindValue(':numSocio', numSocio)
        if query1.exec_():
            while query1.next():
                numLibros = query1.value(0)
        numLibros=numLibros+1

        query = QtSql.QSqlQuery()
        query.prepare(
            'update socios set numLibros=:numLibros where numSocio=:numSocio')
        query.bindValue(':numSocio', str(numSocio))
        query.bindValue(':numLibros', str(numLibros))
        if query.exec_():
            print('SOCIO MODIFICADO')
            # var.ui.tbEstado.setText('LIBRO CON CODIGO %s HA SIDO MODIFICADO' % codigo)
        else:
            print('Error modificar socio: ', query.lastError().text())

    def socioAptoPrestamo(numSocio):
        try:
            disponible=False
            query = QtSql.QSqlQuery()
            query.prepare('select multa, numLibros from socios where numSocio=:numSocio')
            query.bindValue(':numSocio', numSocio)
            if query.exec_():
                while query.next():
                    multa = str(query.value(0))
                    numLibros = query.value(1)
                    if(multa=='False' and numLibros<3):
                        disponible=True
            return disponible
        except Exception as error:
            print('Error disponibilidad socio: %s' % str(error))

    def guardarSocio(socio):
        query=QtSql.QSqlQuery()
        query.prepare('insert into socios (dni, nombre, apellidos, direccion, sexo, multa, fmulta, numLibros)'
                      'VALUES (:dni, :nombre, :apellidos, :direccion, :sexo, :multa, :fmulta, :numLibros)')
        query.bindValue(':dni', str(socio[0]))
        query.bindValue(':nombre', str(socio[1]))
        query.bindValue(':apellidos', str(socio[2]))
        query.bindValue(':direccion', str(socio[3]))
        query.bindValue(':sexo', str(socio[4]))
        query.bindValue(':multa', str(socio[5]))
        query.bindValue(':fmulta', str(socio[6]))
        query.bindValue(':numLibros', str(socio[7]))

        if query.exec_():
            #var.ui.tbEstado.setText("CLIENTE DNI '" +cliente[0] + "' HA SIDO DADO DE ALTA")
            print('Insercción de socio correcta')
            Socios.mostrarSocios(socio)
        else:
            #var.ui.tbEstado.setText("CLIENTE DNI '" + cliente[0] + "' YA EXISTE EN LA BD")
            print('Error guardar socio: ', query.lastError().text())

    def mostrarSocios(self):
        index = 0
        query =QtSql.QSqlQuery()
        query.prepare('select numSocio, dni, nombre, apellidos, direccion, sexo, multa, fmulta, numLibros from socios')
        if query.exec_():
            while query.next():
                numSocio =str(query.value(0))
                dni = query.value(1)
                nombre = query.value(2)
                apellidos = query.value(3)
                direccion = query.value(4)
                sexo = query.value(5)
                multa = query.value(6)
                fmulta = query.value(7)
                numLibros = str(query.value(8))

                var.ui.tablaSocios.setRowCount(index+1)#Crea la fila y a continuación mete los datos
                var.ui.tablaSocios.setItem(index,0, QtWidgets.QTableWidgetItem(numSocio))
                var.ui.tablaSocios.setItem(index,1, QtWidgets.QTableWidgetItem(dni))
                var.ui.tablaSocios.setItem(index,2, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tablaSocios.setItem(index,3, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaSocios.setItem(index,4, QtWidgets.QTableWidgetItem(direccion))
                var.ui.tablaSocios.setItem(index, 5, QtWidgets.QTableWidgetItem(sexo))
                var.ui.tablaSocios.setItem(index, 6, QtWidgets.QTableWidgetItem(multa))
                var.ui.tablaSocios.setItem(index, 7, QtWidgets.QTableWidgetItem(fmulta))
                var.ui.tablaSocios.setItem(index, 8, QtWidgets.QTableWidgetItem(numLibros))
                index +=1
        else:
            #var.ui.tbEstado.setText("BASE DE DATOS NO COMPATIBLE")
            var.ui.tablaSocios.setRowCount(1)  # Crea la fila y a continuación mete los datos
            var.ui.tablaSocios.setItem(index, 0, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaSocios.setItem(index, 1, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaSocios.setItem(index, 2, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaSocios.setItem(index, 3, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaSocios.setItem(index, 4, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaSocios.setItem(index, 5, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaSocios.setItem(index, 6, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaSocios.setItem(index, 7, QtWidgets.QTableWidgetItem(""))
            var.ui.tablaSocios.setItem(index, 8, QtWidgets.QTableWidgetItem(""))

            print('Error mostrar libros: ',query.lastError().text())


    def existeSocioDni(id):
        try:
            salida = False
            query = QtSql.QSqlQuery()
            query.prepare('select dni from socios')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    if (dni == id):
                        salida = True
            return salida
        except Exception as error:
            print('Error existe socio dni: %s' % str(error))

    def buscarSocioDni(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'select numSocio, dni, nombre, apellidos, direccion, sexo, multa, fmulta ,numLibros from socios where dni=:dni')
            query.bindValue(':dni', dni)
            Socios.resultadosBusqueda(query)
        except Exception as error:
            print('Error buscar libro estado: %s' % str(error))

    def resultadosBusqueda(query):
        index = 0
        if query.exec_():
            while query.next():
                var.numSocio = query.value(0)
                var.dni = query.value(1)
                var.nombre = query.value(2)
                var.apellidos = query.value(3)
                var.direccion = query.value(4)
                var.sexo = query.value(5)
                var.multa = query.value(6)
                var.fmulta = query.value(7)
                var.numLibros=query.value(8)

                var.ui.tablaSocios.setRowCount(index + 1)  # Crea la fila y a continuación mete los datos
                var.ui.tablaSocios.setItem(index, 0, QtWidgets.QTableWidgetItem(str(var.numSocio)))
                var.ui.tablaSocios.setItem(index, 1, QtWidgets.QTableWidgetItem(var.dni))
                var.ui.tablaSocios.setItem(index, 2, QtWidgets.QTableWidgetItem(var.nombre))
                var.ui.tablaSocios.setItem(index, 3, QtWidgets.QTableWidgetItem(var.apellidos))
                var.ui.tablaSocios.setItem(index, 4, QtWidgets.QTableWidgetItem(var.direccion))
                var.ui.tablaSocios.setItem(index, 5, QtWidgets.QTableWidgetItem(var.sexo))
                var.ui.tablaSocios.setItem(index, 6, QtWidgets.QTableWidgetItem(var.multa))
                var.ui.tablaSocios.setItem(index, 7, QtWidgets.QTableWidgetItem(var.fmulta))
                var.ui.tablaSocios.setItem(index, 8, QtWidgets.QTableWidgetItem(str(var.numLibros)))
                index += 1
        else:
            print('Error buscar socio: ', query.lastError().text())


#CONEXION DE LOS PRÉSTAMOS
class Prestamos:

    def guardarPrestamo(prestamo):
        query=QtSql.QSqlQuery()
        query.prepare('insert into prestamos (numSocio, codLibro, desde, hasta, devuelto, fdevolucion)'
                      'VALUES (:numSocio, :codLibro, :desde, :hasta, :devuelto,:fdevolucion)')
        query.bindValue(':numSocio', str(prestamo[0]))
        query.bindValue(':codLibro', str(prestamo[1]))
        query.bindValue(':desde', str(prestamo[2]))
        query.bindValue(':hasta', str(prestamo[3]))
        query.bindValue(':devuelto', str(prestamo[4]))
        query.bindValue(':fdevolucion', str(prestamo[5]))

        if query.exec_():
            #var.ui.tbEstado.setText("CLIENTE DNI '" +cliente[0] + "' HA SIDO DADO DE ALTA")
            print('Insercción de prestamo correcta')
            Prestamos.mostrarPrestamos(prestamo)
        else:
            #var.ui.tbEstado.setText("CLIENTE DNI '" + cliente[0] + "' YA EXISTE EN LA BD")
            print('Error guardar prestamo: ', query.lastError().text())

    def mostrarPrestamos(self):
        try:
            index = 0
            query =QtSql.QSqlQuery()
            query.prepare('select numSocio, codLibro, desde, hasta, devuelto, fdevolucion from prestamos order by devuelto')
            if query.exec_():
                while query.next():
                    numSocio =str(query.value(0))
                    codLibro = str(query.value(1))
                    desde = query.value(2)
                    hasta = query.value(3)
                    devuelto = str(query.value(4))
                    fedevolucion = query.value(5)
                    var.ui.tablaPrestamos.setRowCount(index+1)#Crea la fila y a continuación mete los datos
                    var.ui.tablaPrestamos.setItem(index,0, QtWidgets.QTableWidgetItem(numSocio))
                    var.ui.tablaPrestamos.setItem(index,1, QtWidgets.QTableWidgetItem(codLibro))
                    var.ui.tablaPrestamos.setItem(index,2, QtWidgets.QTableWidgetItem(desde))
                    var.ui.tablaPrestamos.setItem(index,3, QtWidgets.QTableWidgetItem(hasta))
                    var.ui.tablaPrestamos.setItem(index,4, QtWidgets.QTableWidgetItem(devuelto))
                    var.ui.tablaPrestamos.setItem(index, 5, QtWidgets.QTableWidgetItem(fedevolucion))
                    index +=1
            else:
                #var.ui.tbEstado.setText("BASE DE DATOS NO COMPATIBLE")
                var.ui.tablaLibros.setRowCount(1)  # Crea la fila y a continuación mete los datos
                var.ui.tablaLibros.setItem(index, 0, QtWidgets.QTableWidgetItem(""))
                var.ui.tablaLibros.setItem(index, 1, QtWidgets.QTableWidgetItem(""))
                var.ui.tablaLibros.setItem(index, 2, QtWidgets.QTableWidgetItem(""))
                var.ui.tablaLibros.setItem(index, 3, QtWidgets.QTableWidgetItem(""))
                var.ui.tablaLibros.setItem(index, 4, QtWidgets.QTableWidgetItem(""))
                var.ui.tablaLibros.setItem(index, 5, QtWidgets.QTableWidgetItem(""))
                print('Error mostrar libros: ',query.lastError().text())
        except Exception as error:
            print('Excepcion aaaa: ', error)