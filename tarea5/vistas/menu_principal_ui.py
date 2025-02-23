# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QWidget)

class Ui_MenuPrincipal(object):
    def setupUi(self, MenuPrincipal):
        if not MenuPrincipal.objectName():
            MenuPrincipal.setObjectName(u"MenuPrincipal")
        MenuPrincipal.resize(513, 247)
        MenuPrincipal.setMinimumSize(QSize(513, 247))
        MenuPrincipal.setMaximumSize(QSize(513, 247))
        self.actionReservar = QAction(MenuPrincipal)
        self.actionReservar.setObjectName(u"actionReservar")
        font = QFont()
        font.setPointSize(12)
        self.actionReservar.setFont(font)
        self.actionClientes = QAction(MenuPrincipal)
        self.actionClientes.setObjectName(u"actionClientes")
        self.actionClientes.setFont(font)
        self.actionAcerca = QAction(MenuPrincipal)
        self.actionAcerca.setObjectName(u"actionAcerca")
        self.actionAcerca.setFont(font)
        self.actionDocumentaci_n = QAction(MenuPrincipal)
        self.actionDocumentaci_n.setObjectName(u"actionDocumentaci_n")
        self.actionDocumentaci_n.setFont(font)
        self.centralwidget = QWidget(MenuPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 521, 101))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 90, 391, 31))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MenuPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MenuPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 513, 33))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.menubar.setFont(font3)
        self.menuAplicaciones = QMenu(self.menubar)
        self.menuAplicaciones.setObjectName(u"menuAplicaciones")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.menuAplicaciones.setFont(font4)
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuAyuda.setFont(font4)
        MenuPrincipal.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuAplicaciones.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuAplicaciones.addAction(self.actionReservar)
        self.menuAplicaciones.addAction(self.actionClientes)
        self.menuAyuda.addAction(self.actionAcerca)
        self.menuAyuda.addAction(self.actionDocumentaci_n)

        self.retranslateUi(MenuPrincipal)

        QMetaObject.connectSlotsByName(MenuPrincipal)
    # setupUi

    def retranslateUi(self, MenuPrincipal):
        MenuPrincipal.setWindowTitle(QCoreApplication.translate("MenuPrincipal", u"Men\u00fa principal", None))
        self.actionReservar.setText(QCoreApplication.translate("MenuPrincipal", u"Reservar", None))
        self.actionClientes.setText(QCoreApplication.translate("MenuPrincipal", u"Clientes", None))
        self.actionAcerca.setText(QCoreApplication.translate("MenuPrincipal", u"Acerca", None))
        self.actionDocumentaci_n.setText(QCoreApplication.translate("MenuPrincipal", u"Documentaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MenuPrincipal", u"BIENVENIDO/A A TU GESTI\u00d3N", None))
        self.label_2.setText(QCoreApplication.translate("MenuPrincipal", u"Elige arriba la opci\u00f3n que necesites", None))
        self.menuAplicaciones.setTitle(QCoreApplication.translate("MenuPrincipal", u"Aplicaciones", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MenuPrincipal", u"Ayuda", None))
    # retranslateUi

