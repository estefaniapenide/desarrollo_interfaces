import libros
import var
import conexion


class Libros:

    def cargarGenero(self):
        try:
            genero=['','Narrativa','Teatro','Poesía','Ensayo']
            for i in genero:
                var.ui.comboBoxGenero.addItem(i)
        except Exception as error:
            print('Error al cargar género: %s'% str(error))

    def seleccionarGenero(genero):
        try:
            var.generoLibro=genero
        except Exception as error:
            print('Error: %s' % str(error))

    def seleccionarEstado(self):
        try:
            index = var.ui.spinBoxEstado.value()
            estado = ['DISPONIBLE', 'PRESTADO']
            var.estadoLibro = estado[index]
            var.ui.indicadorEstado.setText(var.estadoLibro)
            var.ui.indicadorEstado.setText(var.estadoLibro)
        except Exception as error:
            print('Error seleccionar envío: %s' % str(error))


    def seleccionarEtiquetas(self):
        try:
            var.etiquetas = [] #Se guardará en la base de datos
            if var.ui.checkBoxAventuras.isChecked():
                var.etiquetas.append('Aventuras')
            if var.ui.checkBoxFantasia.isChecked():
                var.etiquetas.append('Fantasía')
            if var.ui.checkBoxFilosofia.isChecked():
                var.etiquetas.append('Filosofía')
            if var.ui.checkBoxIntriga.isChecked():
                var.etiquetas.append('Intriga')
            if var.ui.checkBoxHistorica.isChecked():
                var.etiquetas.append('Histórica')
            if var.ui.checkBoxRomantica.isChecked():
                var.etiquetas.append('Romántica')


        except Exception as error:
            print('Error selccionar etiquetas: %s' % str(error))

    def marcarEtiquetas(self):
        var.checkBoxEtiquetas = (var.ui.checkBoxAventuras, var.ui.checkBoxFantasia, var.ui.checkBoxFilosofia, var.ui.checkBoxIntriga, var.ui.checkBoxHistorica, var.ui.checkBoxRomantica)
        for i in var.checkBoxEtiquetas:
            i.stateChanged.connect(Libros.seleccionarEtiquetas)

    def guardarLibro(self):
        try:
            libro = [var.estadoLibro, var.ui.lineEditTitulo.text(), var.ui.lineEditAutor.text(), var.generoLibro, var.etiquetas]

            conexion.Libros.guardarLibro(libro)
            Libros.buscarLibroCodigo(self)
            conexion.Libros.mostrarLibros(self)

        except Exception as error:
            #var.ui.tbEstado.setText("DEBE CUBRIR LOS CAMPOS OBLIGATORIOS")
            print('Error guardar libro (libros): %s ' % str(error))

    def eliminarLibro(self):
        try:
            codigo = var.ui.lineEditCodigo.text()
            if (conexion.Libros.existeLibro(codigo)):
                conexion.Libros.bajaLibro(codigo)
                conexion.Libros.mostrarLibros(self)
                Libros.limpiarLibro(self)
                #var.ui.tbEstado.setText("CLIENTE DNI '" + dni + "' HA SIDO DADO DE BAJA")
            else:
                print('NO EXISTE EL CLIENTE')
                if var.ui.lineEditCodigo.text()=='':
                    print("NO HA INTRODUCIDO NINGÚN CÓDIGO")
                    #var.ui.tbEstado.setText("NO HA INTRODUCIDO NINGÚN CÓDIGO")
                else:
                    print("LIBRO CON CÓDIGO '" + codigo + "' NO EXISTE EN LA BD")
                    #var.ui.tbEstado.setText("LIBRO CON CÓDIGO '" + codigo + "' NO EXISTE EN LA BD")
        except Exception as error:
            print('Error eliminar libro: %s' % str(error))


    def modificarLibro(self):
        try:
            libro = [var.ui.lineEditCodigo.text(), var.estadoLibro, var.ui.lineEditTitulo.text(), var.ui.lineEditAutor.text(), var.generoLibro, var.etiquetas]
            if (conexion.Libros.existeLibro(libro[0])):
                conexion.Libros.modificarLibro(libro)
                conexion.Libros.mostrarLibros(self)
            else:
                print('NO EXISTE EL CLIENTE')
                if var.ui.leDNI.text() == '':
                    print("NO HA INTRODUCIDO NINGÚN CÓDIGO")
                    #var.ui.tbEstado.setText("NO HA INTRODUCIDO NINGÚN CÓDIGO")
                else:
                    print("LIBRO CON CÓDIGO '" + libro[0].text()+ "' NO EXISTE EN LA BD")
                    #var.ui.tbEstado.setText("LIBRO CON CÓDIGO '" + libro[0].text()+ "' NO EXISTE EN LA BD")
        except Exception as error:
            #var.ui.tbEstado.setText("DEBE CUBRIR LOS CAMPOS OBLIGATORIOS")
            print('Error modificando libro: %s' % str(error))


    def limpiarLibro(self):

        var.ui.lineEditCodigo.setText("")
        var.ui.lineEditTitulo.setText("")
        var.ui.lineEditAutor.setText("")
        var.ui.comboBoxGenero.setCurrentIndex(0)
        var.ui.labelCodigoGenerado.setText("")
        var.ui.spinBoxEstado.setValue(0)
        var.ui.checkBoxAventuras.setChecked(False)
        var.ui.checkBoxFantasia.setChecked(False)
        var.ui.checkBoxFilosofia.setChecked(False)
        var.ui.checkBoxIntriga.setChecked(False)
        var.ui.checkBoxHistorica.setChecked(False)
        var.ui.checkBoxRomantica.setChecked(False)



    def buscarLibroCodigo(self):
        id = var.ui.lineEditCodigo.text()
        if conexion.Libros.existeLibro(id):
            conexion.Libros.buscarLibroCodigo(id)

            Libros.limpiarLibro(self)

            var.ui.lineEditCodigo.setText(str(var.codigo))
            var.ui.labelCodigoGenerado.setText(str(var.codigo))
            var.ui.lineEditTitulo.setText(var.titulo)
            var.ui.lineEditAutor.setText(var.autor)

            if (var.estado == 'DISPONIBLE'):
                var.ui.spinBoxEstado.setValue(0)
            elif (var.estado == 'PRESTADO'):
                var.ui.spinBoxEstado.setValue(1)

            if (var.genero == ""):
                var.ui.comboBoxGenero.setCurrentIndex(0)
            elif (var.genero == "Narrativa"):
                var.ui.comboBoxGenero.setCurrentIndex(1)
            elif (var.genero == "Teatro"):
                var.ui.comboBoxGenero.setCurrentIndex(2)
            elif (var.genero == "Poesía"):
                var.ui.comboBoxGenero.setCurrentIndex(3)
            elif (var.genero == "Ensayo"):
                var.ui.comboBoxGenero.setCurrentIndex(4)

            if 'Aventuras' in var.etiqueta:
                var.ui.checkBoxAventuras.setChecked(True)
            if 'Romántica' in var.etiqueta:
                var.ui.checkBoxRomantica.setChecked(True)
            if 'Histórica' in var.etiqueta:
                var.ui.checkBoxHistorica.setChecked(True)
            if 'Intriga' in var.etiqueta:
                var.ui.checkBoxIntriga.setChecked(True)
            if 'Fantasía' in var.etiqueta:
                var.ui.checkBoxFantasia.setChecked(True)
            if 'Filosofía' in var.etiqueta:
                var.ui.checkBoxFilosofia.setChecked(True)

            #var.ui.tbEstado.setText('CLIENTE DNI %s ENCONTRADO' % id)

        else:
            Libros.limpiarLibro(self)
            var.ui.lineEditCodigo.setText(id)
            conexion.Libros.mostrarLibros(self)
            #var.ui.tbEstado.setText('CLIENTE DNI %s NO ENCONTRADO' % id)
            #var.ui.lineEditCodigo.setText(id)

    def buscarLibroTitulo(self):
        titulo = var.ui.lineEditTitulo.text()
        if conexion.Libros.existeLibroTitulo(titulo):
            conexion.Libros.buscarLibroTitulo(titulo)

            Libros.limpiarLibro(self)

            var.ui.lineEditTitulo.setText(titulo)
        else:
            Libros.limpiarLibro(self)
            var.ui.lineEditTitulo.setText(titulo)
            conexion.Libros.mostrarLibros(self)
            print('NO EXISTE EL LIBRO EN LA DB ')

    def buscarLibroAutor(self):
        autor = var.ui.lineEditAutor.text()
        if conexion.Libros.existeLibroAutor(autor):
            conexion.Libros.buscarLibroAutor(autor)

            Libros.limpiarLibro(self)

            var.ui.lineEditAutor.setText(autor)
        else:
            Libros.limpiarLibro(self)
            var.ui.lineEditAutor.setText(autor)
            conexion.Libros.mostrarLibros(self)
            print('NO EXISTE EL LIBRO EN LA DB ')


    def buscarLibroGenero(self):
        genero = var.generoLibro
        if conexion.Libros.existeLibroGenero(genero):
            conexion.Libros.buscarLibroGenero(genero)

            Libros.limpiarLibro(self)

            if (var.genero == ""):
                var.ui.comboBoxGenero.setCurrentIndex(0)
            elif (var.genero == "Narrativa"):
                var.ui.comboBoxGenero.setCurrentIndex(1)
            elif (var.genero == "Teatro"):
                var.ui.comboBoxGenero.setCurrentIndex(2)
            elif (var.genero == "Poesía"):
                var.ui.comboBoxGenero.setCurrentIndex(3)
            elif (var.genero == "Ensayo"):
                var.ui.comboBoxGenero.setCurrentIndex(4)
        else:
            Libros.limpiarLibro(self)
            if (var.generoLibro == ""):
                var.ui.comboBoxGenero.setCurrentIndex(0)
            elif (var.generoLibro == "Narrativa"):
                var.ui.comboBoxGenero.setCurrentIndex(1)
            elif (var.generoLibro == "Teatro"):
                var.ui.comboBoxGenero.setCurrentIndex(2)
            elif (var.generoLibro == "Poesía"):
                var.ui.comboBoxGenero.setCurrentIndex(3)
            elif (var.generoLibro == "Ensayo"):
                var.ui.comboBoxGenero.setCurrentIndex(4)
            conexion.Libros.mostrarLibros(self)
            print('NO EXISTE EL LIBRO EN LA DB ')

    def buscarLibroEstado(self):
        estado = var.estadoLibro
        if conexion.Libros.existeLibroEstado(estado):
            conexion.Libros.buscarLibroEstado(estado)

            Libros.limpiarLibro(self)

            if (var.estado == 'DISPONIBLE'):
                var.ui.spinBoxEstado.setValue(0)
            elif (var.estado == 'PRESTADO'):
                var.ui.spinBoxEstado.setValue(1)
        else:
            Libros.limpiarLibro(self)
            if (var.estadoLibro == 'DISPONIBLE'):
                var.ui.spinBoxEstado.setValue(0)
            elif (var.estadoLibro == 'PRESTADO'):
                var.ui.spinBoxEstado.setValue(1)
            conexion.Libros.mostrarLibros(self)
            print('NO EXISTE EL LIBRO EN LA DB ')