from reportlab.pdfgen import canvas
import os
import var
from PyQt5 import QtWidgets, QtSql
from datetime import datetime

class Printer():


    def cabecera(self):
        try:
            logo='.\\img\logo.png'
            var.rep.setTitle('INFORMES')
            var.rep.setAuthor('Adminsitración')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45,820,525,820)
            var.rep.line(45,745,525,745)
            textcif='A0000000H'
            textnom='IMPORTACIÓN Y EXPORTACIÓN TEIS, S.L.'
            textdir='Avenida Galicia, 101 - Vigo'
            texttlfo='886 12 04 04'
            var.rep.drawString(50,805,textcif)
            var.rep.drawString(50,790, textnom)
            var.rep.drawString(50,775, textdir)
            var.rep.drawString(50,760, texttlfo)
            #var.rep.drawImage(logo,450,752)
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE CLIENTES'
            var.rep.drawString(240, 695, textlistado)
        except Exception as error:
            print('Error cabecera informe: %s' % str(error))

    def cuerpo(self):
        try:
            itemCli=['DNI', 'APELLIDOS', 'NOMBRE','FECHA ALTA']
            var.rep.setFont('Helvetica-Bold', size=9)
            var.rep.line(45, 680, 525, 680)
            var.rep.drawString(65,667,itemCli[0])
            var.rep.drawString(190, 667, itemCli[1])
            var.rep.drawString(330, 667, itemCli[2])
            var.rep.drawString(445, 667, itemCli[3])
            var.rep.line(45,660,525,660)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, fechaAlta from clientes order by apellidos, nombre')
            if query.exec_():
                i=50
                j=645
                cont=0
                while query.next():
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i,j, str(query.value(0)))
                    var.rep.drawString(i+130, j, str(query.value(1)))
                    var.rep.drawString(i+280, j, str(query.value(2)))
                    var.rep.drawString(i+400, j, str(query.value(3)))
                    j=j-30
                    cont=cont+1
                    if (cont == 20):
                        Printer.pie(self)
                        var.rep.showPage()
                        i=50
                        j=745
                        var.rep.setFont('Helvetica-Bold', size=9)
                        var.rep.line(45, 790, 525, 790)
                        var.rep.drawString(65, 777, itemCli[0])
                        var.rep.drawString(190, 777, itemCli[1])
                        var.rep.drawString(330, 777, itemCli[2])
                        var.rep.drawString(445, 777, itemCli[3])
                        var.rep.line(45, 770, 525, 770)
                        cont = 0
                Printer.pie(self)
        except Exception as error:
            print('Error cuerpo informe: %s' % str(error))

    def pie(self):
        try:
            var.rep.line(45,45,525,45)
            fecha= datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique',size=7)
            var.rep.drawString(460,35,str(fecha))
            var.rep.drawString(275, 35, str('Página %s' % var.rep.getPageNumber()))
            #var.rep.drawString(45, 35, str(textlistado))
        except Exception as error:
            print('Error pie informe: %s' % str(error))


    def reportCli(self):
        try:
            var.rep =  canvas.Canvas('informes/listadoclientes.pdf')
            Printer.cabecera(self)
            Printer.cuerpo(self)
            var.rep.save()
            rootPath=".\\informes"
            cont =0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error reportCli %s' % str(error))