import var
from dni import Dni

class Eventos():

    def AceptarDatos(self):
        try:
            datosCompletos =False
            dni = var.ui.leDNI.text()
            nombre = var.ui.leNombre.text()
            apellidos = var.ui.leApellidos.text()

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
                    var.ui.lblDNI.setText('<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">DNI</span></p></body></html>')
                    datosCompletos=True
                else:
                    print("DNI INCORRECTO")
                    var.ui.lblDNI.setText('<html><head/><body><p><span style=\" font-size:8pt; color:#b1193d;\">DNI</span></p></body></html>')
                    datosCompletos = False
            else:
                print("DNI INCORRECTO")
                var.ui.lblDNI.setText('<html><head/><body><p><span style=\" font-size:8pt; color:#b1193d;\">DNI</span></p></body></html>')
                datosCompletos = False
            if nombre=='':
                print("FALTA EL NOMBRE")
                var.ui.lblNombre.setText('<html><head/><body><p><span style=\" font-size:8pt; color:#b1193d;\">Nombre</span></p></body></html>')
                datosCompletos = False
            else:
                print("NOMBRE AÑADIDO")
                var.ui.lblNombre.setText('<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">Nombre</span></p></body></html>')
                datosCompletos = True
            if apellidos=='':
                print("FALTA EL NOMBRE")
                var.ui.lblApellidos.setText('<html><head/><body><p><span style=\" font-size:8pt; color:#b1193d;\">Apellidos</span></p></body></html>')
                datosCompletos = False
            else:
                print("APELLIDOS AÑADIDO")
                var.ui.lblApellidos.setText('<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">Apellidos</span></p></body></html>')
                datosCompletos = True

            if datosCompletos:
                exit()

        except Exception as error:
            print('Error: %s ' % str(error))

    def Salir(self):
        try:
            exit()
        except Exception as error:
            print('Error: %s ' % str(error))
