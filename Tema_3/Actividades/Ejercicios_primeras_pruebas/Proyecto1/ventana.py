# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Proyecto1(object):
    def setupUi(self, Proyecto1):
        Proyecto1.setObjectName("Proyecto1")
        Proyecto1.resize(703, 632)
        self.centralwidget = QtWidgets.QWidget(Proyecto1)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(290, 140, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblPulsa = QtWidgets.QLabel(self.centralwidget)
        self.lblPulsa.setGeometry(QtCore.QRect(250, 90, 161, 41))
        self.lblPulsa.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblPulsa.setTextFormat(QtCore.Qt.AutoText)
        self.lblPulsa.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPulsa.setObjectName("lblPulsa")
        self.CALENDARIO = QtWidgets.QCalendarWidget(self.centralwidget)
        self.CALENDARIO.setGeometry(QtCore.QRect(170, 230, 312, 183))
        self.CALENDARIO.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.CALENDARIO.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.CALENDARIO.setObjectName("CALENDARIO")
        Proyecto1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Proyecto1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 21))
        self.menubar.setObjectName("menubar")
        Proyecto1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Proyecto1)
        self.statusbar.setObjectName("statusbar")
        Proyecto1.setStatusBar(self.statusbar)

        self.retranslateUi(Proyecto1)
        QtCore.QMetaObject.connectSlotsByName(Proyecto1)

    def retranslateUi(self, Proyecto1):
        _translate = QtCore.QCoreApplication.translate
        Proyecto1.setWindowTitle(_translate("Proyecto1", "Proyecto1"))
        self.btnAceptar.setText(_translate("Proyecto1", "Aceptar"))
        self.lblPulsa.setText(_translate("Proyecto1", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00ff00;\">PULSA EL BOTÓN</span></p></body></html>"))
