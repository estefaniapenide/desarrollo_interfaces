import eventos
import libros
import var
import conexion
import prestamos
import socios
from ventanaBiblioteca import *
import ventanaCalendarioPrestamo
import ventanaCalendarioDevolucion
import ventanaCalendarioSancion
import sys
from datetime import datetime

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)


        #************************************+CONEXIÓN BD***********************************************
        var.filedb = 'biblioteca.db'
        conexion.Conexion.db_connect(var.filedb)
        conexion.Libros.mostrarLibros(self)
        conexion.Prestamos.mostrarPrestamos(self)
        conexion.Socios.mostrarSocios(self)
        #**************************************************************************************************+



        #***************************************PRÉSTAMOS******************************************
        #Seleccionar fechas préstamo y devolución
        var.ui.pushButtonCalendario.clicked.connect(eventos.Calendario.abrirCalendarioPrestamo)
        var.ui.pushButtonCalendarioDevolucion.clicked.connect(eventos.Calendario.abrirCalendarioDevolucion)
        #Seleccionar Devuelto y visibilidad Fecha Devolucion
        prestamos.Prestamos.seleccionarDevuelto(self)
        prestamos.Prestamos.visibilidadFechaDevolucion(self)
        var.ui.buttonGroupDevuelto.buttonToggled.connect(prestamos.Prestamos.seleccionarDevuelto)
        var.ui.buttonGroupDevuelto.buttonToggled.connect(prestamos.Prestamos.visibilidadFechaDevolucion)
        # Botones guardar, elimninar, modificar, limpiar
        var.ui.pushButtonGuardarPrestamo.clicked.connect(prestamos.Prestamos.guardarPrestamo)
        #****************************************************************************************************



        #*****************************************LIBROS****************************************
        #Seleccionar género
        var.generoLibro='' #Género predeterminado
        libros.Libros.cargarGenero(self)
        var.ui.comboBoxGenero.currentIndexChanged[str].connect(libros.Libros.seleccionarGenero)
        # Seleccionar estado
        var.estadoLibro = 'DISPONIBLE'  # Estado predeterminado
        var.ui.spinBoxEstado.valueChanged.connect(libros.Libros.seleccionarEstado)
        #Seleccionar etiquetas
        libros.Libros.marcarEtiquetas(self)
        #Botones guardar, elimninar, modificar, limpiar
        var.ui.pushButtonGuardarLibro.clicked.connect(libros.Libros.guardarLibro)
        var.ui.pushButtonLimpiarLibros.clicked.connect(libros.Libros.limpiarLibro)
        var.ui.pushButtonLimpiarLibros.clicked.connect(conexion.Libros.mostrarLibros)
        var.ui.pushButtonEliminarLibro.clicked.connect(libros.Libros.eliminarLibro)
        var.ui.pushButtonModificarLibro.clicked.connect(libros.Libros.modificarLibro)
        #Búsquedas
        var.ui.pushButtonBuscarCodigo.clicked.connect(libros.Libros.buscarLibroCodigo)
        var.ui.pushButtonBuscarTitulo.clicked.connect(libros.Libros.buscarLibroTitulo)
        var.ui.pushButtonBuscarAutor.clicked.connect(libros.Libros.buscarLibroAutor)
        var.ui.pushButtonBuscarGenero.clicked.connect(libros.Libros.buscarLibroGenero)
        var.ui.pushButtonBuscarEstado.clicked.connect(libros.Libros.buscarLibroEstado)
        # ****************************************************************************************************



        # ***************************************SOCIOS******************************************
        # Seleccionar fecha sanción
        var.ui.pushButtonSancionHasta.clicked.connect(eventos.Calendario.abrirCalendarioSancion)
        # Seleccionar Multa y visibilidad Sanción Hasta
        socios.Socios.seleccionarMulta(self)
        socios.Socios.visibilidadFechaSancion(self)
        var.ui.buttonGroupMulta.buttonToggled.connect(socios.Socios.seleccionarMulta)
        var.ui.buttonGroupMulta.buttonToggled.connect(socios.Socios.visibilidadFechaSancion)
        #Seleccionar sexo
        var.ui.buttonGroupSexo.buttonClicked.connect(socios.Socios.seleccionarSexo)
        #Seleccionar numero libros prestados
        var.numLibrosSocio=0 #Valor por defecto
        var.ui.spinBoxNumLibros.valueChanged.connect(socios.Socios.seleccionarNumLibros)
        #Validar DNI
        var.ui.lineEditDni.editingFinished.connect(socios.Socios.validarDNI)
        # Botones guardar, elimninar, modificar, limpiar
        var.ui.pushButtonGuardarSocio.clicked.connect(socios.Socios.guardarSocio)
        # Búsquedas
        var.ui.pushButtonBuscarDni.clicked.connect(socios.Socios.buscarSocioDni)
        # ****************************************************************************************************

class CalendarioPrestamo(QtWidgets.QDialog):

    def __init__(self):
        super(CalendarioPrestamo,self).__init__()
        var.uiCalendarioPrestamo = ventanaCalendarioPrestamo.Ui_Dialog()
        var.uiCalendarioPrestamo.setupUi(self)
        diaActual=datetime.now().day
        mesActual=datetime.now().month
        anoActual=datetime.now().year

        #PRÉSTAMOS
        var.uiCalendarioPrestamo.calendarioPrestamo.setSelectedDate(QtCore.QDate(anoActual,mesActual,diaActual))
        var.uiCalendarioPrestamo.calendarioPrestamo.clicked.connect(eventos.Calendario.cargarFechaDesde)
        var.uiCalendarioPrestamo.calendarioPrestamo.clicked.connect(eventos.Calendario.cargarFechaHasta)

class CalendarioDevolucion(QtWidgets.QDialog):

    def __init__(self):
        super(CalendarioDevolucion,self).__init__()
        var.uiCalendarioDevolucion = ventanaCalendarioDevolucion.Ui_Dialog()
        var.uiCalendarioDevolucion.setupUi(self)
        diaActual=datetime.now().day
        mesActual=datetime.now().month
        anoActual=datetime.now().year

        #DEVOLUCIÓN
        var.uiCalendarioDevolucion.calendarioDevolucion.setSelectedDate(QtCore.QDate(anoActual,mesActual,diaActual))
        var.uiCalendarioDevolucion.calendarioDevolucion.clicked.connect(eventos.Calendario.cargarFechaDevolucion)

class CalendarioSancion(QtWidgets.QDialog):

    def __init__(self):
        super(CalendarioSancion,self).__init__()
        var.uiCalendarioSancion = ventanaCalendarioSancion.Ui_Dialog()
        var.uiCalendarioSancion.setupUi(self)
        diaActual=datetime.now().day
        mesActual=datetime.now().month
        anoActual=datetime.now().year

        #SANCIÓN
        var.uiCalendarioSancion.calendarioSancion.setSelectedDate(QtCore.QDate(anoActual,mesActual,diaActual))
        var.uiCalendarioSancion.calendarioSancion.clicked.connect(eventos.Calendario.cargarFechaSancion)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.uiCalendarioPrestamo = CalendarioPrestamo()
    var.uiCalendarioDevolucion = CalendarioDevolucion()
    var.uiCalendarioSancion = CalendarioSancion()
    window.show()
    sys.exit(app.exec())
