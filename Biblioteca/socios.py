import var
from dni import Dni
from PyQt5.QtGui import QFont
import conexion

class Socios:

    def visibilidadFechaSancion(self):
        if var.multaSocio==True:
            Socios.mostrarFechaSancion(self)
        if var.multaSocio==False:
            Socios.esconderFechaSancion(self)

    def esconderFechaSancion(self):
        var.ui.lineEditSancionHasta.setText('')
        var.ui.labelSancionHasta.setHidden(True)
        var.ui.lineEditSancionHasta.setHidden(True)
        var.ui.pushButtonSancionHasta.setHidden(True)

    def mostrarFechaSancion(self):
        var.ui.labelSancionHasta.setHidden(False)
        var.ui.lineEditSancionHasta.setHidden(False)
        var.ui.pushButtonSancionHasta.setHidden(False)

    def seleccionarMulta(self):
        try:
            if var.ui.radioButtonMultaSi.isChecked():
                #print('marcado si')
                var.multaSocio=True
            if var.ui.radioButtonMultaNo.isChecked():
                #print('marcado no')
                var.multaSocio=False
        except Exception as error:
            print('Error en módulo seleccionar multa:',error)

    def seleccionarSexo(self):
        try:
            if var.ui.radioButtonMujer.isChecked():
                #print('marcado mujer')
                var.sexoSocio='Mujer'
            if var.ui.radioButtonHombre.isChecked():
                #print('marcado hombre')
                var.sexoSocio='Hombre'
        except Exception as error:
            print('Error en módulo seleccionar sexo:',error)

    def seleccionarNumLibros(self):
        try:
            var.numLibrosSocio = var.ui.spinBoxNumLibros.value()
        except Exception as error:
            print('Error seleccionar numero de libros prestados: %s' % str(error))

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
                    #var.ui.tbEstado.setText("DNI CORRECTO")
                    var.ui.labelValidarDni.setStyleSheet('QLabel {color:green;font-size:14pt;font-weight:bold}')
                    var.ui.labelValidarDni.setFont(QFont("Forte"))
                    var.ui.labelValidarDni.setText('V')
                    return True
                else:
                    print("DNI INCORRECTO")
                   # var.ui.tbEstado.setText("DNI INCORRECTO")
                    var.ui.labelValidarDni.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                    var.ui.labelValidarDni.setFont(QFont("Forte"))
                    var.ui.labelValidarDni.setText('X')
                    return False
            else:
                print("DNI INCORRECTO")
                #var.ui.tbEstado.setText("DNI INCORRECTO")
                var.ui.labelValidarDni.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold}')
                var.ui.labelValidarDni.setFont(QFont("Forte"))
                var.ui.labelValidarDni.setText('X')
                return False
        except Exception as error:
            print("Error validar dni: %s " % str(error))

    def guardarSocio(self):
        if Socios.validarDNI():
            try:
                socio = [var.ui.lineEditDni.text(), var.ui.lineEditNombre.text(), var.ui.lineEditApellidos.text(), var.ui.lineEditDireccion.text(), var.sexoSocio, str(var.multaSocio),var.ui.lineEditSancionHasta.text(),str(var.numLibrosSocio)]

                conexion.Socios.guardarSocio(socio)
                Socios.buscarSocioDni(self)
                conexion.Socios.mostrarSocios(self)

            except Exception as error:
                #var.ui.tbEstado.setText("DEBE CUBRIR LOS CAMPOS OBLIGATORIOS")
                print('Error guardar socio (socios): %s ' % str(error))

    def buscarSocioDni(self):
        if Socios.validarDNI():
            dni = var.ui.lineEditDni.text()
            if conexion.Socios.existeSocioDni(dni):
                conexion.Socios.buscarSocioDni(dni)

                Socios.limpiarSocio(self)

                var.ui.lineEditDni.setText(var.dni)
                #var.ui.lineEditNumeroSocio.setText(str(var.numSocio))
                var.ui.labelNumSocioGenerado.setText(str(var.numSocio))
                var.ui.lineEditNombre.setText(var.nombre)
                var.ui.lineEditApellidos.setText(var.apellidos)
                var.ui.lineEditDireccion.setText(var.direccion)
                var.ui.spinBoxNumLibros.setValue(var.numLibros)

                if (var.sexo == 'Mujer'):
                    var.ui.radioButtonMujer.click()
                elif (var.sexo == 'Hombre'):
                    var.ui.radioButtonHombre.click()

                #var.ui.tbEstado.setText('CLIENTE DNI %s ENCONTRADO' % id)

            else:
                Socios.limpiarSocio(self)
                var.ui.lineEditNumeroSocio.setText(dni)
                conexion.Socios.mostrarSocios(self)
                #var.ui.tbEstado.setText('CLIENTE DNI %s NO ENCONTRADO' % id)
                #var.ui.lineEditCodigo.setText(id)

    def limpiarSocio(self):

        var.ui.lineEditNumeroSocio.setText("")
        var.ui.labelNumSocioGenerado.setText("")
        var.ui.lineEditDni.setText("")
        var.ui.labelValidarDni.setText("")
        var.ui.lineEditNombre.setText("")
        var.ui.lineEditDireccion.setText("")
        Socios.esconderFechaSancion(self)

        var.ui.buttonGroupMulta.setExclusive(False)
        var.ui.radioButtonMultaNo.setChecked(True)
        var.ui.radioButtonMultaSi.setChecked(False)
        var.ui.buttonGroupMulta.setExclusive(True)

        var.ui.buttonGroupSexo.setExclusive(False)
        var.ui.radioButtonHombre.setChecked(False)
        var.ui.radioButtonMujer.setChecked(False)
        var.ui.buttonGroupSexo.setExclusive(True)

        var.ui.spinBoxNumLibros.setValue(0)
