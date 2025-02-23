# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(995, 492)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vCLblTitulo = QLabel(Dialog)
        self.vCLblTitulo.setObjectName(u"vCLblTitulo")
        self.vCLblTitulo.setMinimumSize(QSize(0, 0))
        self.vCLblTitulo.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.vCLblTitulo.setFont(font)
        self.vCLblTitulo.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.vCLblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vCLblTitulo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vcListWidSalones = QListWidget(Dialog)
        self.vcListWidSalones.setObjectName(u"vcListWidSalones")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcListWidSalones.sizePolicy().hasHeightForWidth())
        self.vcListWidSalones.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.vcListWidSalones.setFont(font1)

        self.horizontalLayout_2.addWidget(self.vcListWidSalones)

        self.vcGridReservas = QTableView(Dialog)
        self.vcGridReservas.setObjectName(u"vcGridReservas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vcGridReservas.sizePolicy().hasHeightForWidth())
        self.vcGridReservas.setSizePolicy(sizePolicy1)
        self.vcGridReservas.setFont(font1)

        self.horizontalLayout_2.addWidget(self.vcGridReservas)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.vcbtnReservar = QPushButton(Dialog)
        self.vcbtnReservar.setObjectName(u"vcbtnReservar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.vcbtnReservar.sizePolicy().hasHeightForWidth())
        self.vcbtnReservar.setSizePolicy(sizePolicy2)
        self.vcbtnReservar.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.vcbtnReservar.setFont(font2)

        self.horizontalLayout.addWidget(self.vcbtnReservar)

        self.vcbtnVerDetalle = QPushButton(Dialog)
        self.vcbtnVerDetalle.setObjectName(u"vcbtnVerDetalle")
        sizePolicy2.setHeightForWidth(self.vcbtnVerDetalle.sizePolicy().hasHeightForWidth())
        self.vcbtnVerDetalle.setSizePolicy(sizePolicy2)
        self.vcbtnVerDetalle.setMinimumSize(QSize(100, 40))
        self.vcbtnVerDetalle.setFont(font2)

        self.horizontalLayout.addWidget(self.vcbtnVerDetalle)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Reservas", None))
#if QT_CONFIG(tooltip)
        self.vCLblTitulo.setToolTip(QCoreApplication.translate("Dialog", u"Reservas", None))
#endif // QT_CONFIG(tooltip)
        self.vCLblTitulo.setText(QCoreApplication.translate("Dialog", u"RESERVAS", None))
#if QT_CONFIG(tooltip)
        self.vcListWidSalones.setToolTip(QCoreApplication.translate("Dialog", u"Salones disponibles", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcGridReservas.setToolTip(QCoreApplication.translate("Dialog", u"Listado de reservas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcbtnReservar.setToolTip(QCoreApplication.translate("Dialog", u"Crear nueva reserva", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnReservar.setText(QCoreApplication.translate("Dialog", u"Reservar", None))
#if QT_CONFIG(tooltip)
        self.vcbtnVerDetalle.setToolTip(QCoreApplication.translate("Dialog", u"Modificar reserva seleccionada", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnVerDetalle.setText(QCoreApplication.translate("Dialog", u"Ver Detalle", None))
    # retranslateUi

