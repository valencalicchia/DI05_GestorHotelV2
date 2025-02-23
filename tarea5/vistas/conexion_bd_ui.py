# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conexion_bd.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ConexionBD(object):
    def setupUi(self, ConexionBD):
        if not ConexionBD.objectName():
            ConexionBD.setObjectName(u"ConexionBD")
        ConexionBD.resize(509, 329)
        ConexionBD.setMinimumSize(QSize(477, 286))
        ConexionBD.setMaximumSize(QSize(999, 999))
        self.verticalLayout = QVBoxLayout(ConexionBD)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vCLblTitulo = QLabel(ConexionBD)
        self.vCLblTitulo.setObjectName(u"vCLblTitulo")
        self.vCLblTitulo.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.vCLblTitulo.setFont(font)
        self.vCLblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vCLblTitulo)

        self.vCLblTitulo_2 = QLabel(ConexionBD)
        self.vCLblTitulo_2.setObjectName(u"vCLblTitulo_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.vCLblTitulo_2.setFont(font1)
        self.vCLblTitulo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vCLblTitulo_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.vcLblNombre = QLabel(ConexionBD)
        self.vcLblNombre.setObjectName(u"vcLblNombre")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.vcLblNombre.setFont(font2)
        self.vcLblNombre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.vcLblNombre)

        self.vcTxtBD = QLineEdit(ConexionBD)
        self.vcTxtBD.setObjectName(u"vcTxtBD")
        self.vcTxtBD.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.vcTxtBD.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.vcTxtBD)

        self.vcLblNombre_2 = QLabel(ConexionBD)
        self.vcLblNombre_2.setObjectName(u"vcLblNombre_2")
        self.vcLblNombre_2.setFont(font2)
        self.vcLblNombre_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.vcLblNombre_2)

        self.vcTxtUsuario = QLineEdit(ConexionBD)
        self.vcTxtUsuario.setObjectName(u"vcTxtUsuario")
        self.vcTxtUsuario.setEnabled(True)
        font4 = QFont()
        font4.setPointSize(14)
        self.vcTxtUsuario.setFont(font4)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.vcTxtUsuario)

        self.vcLblNombre_3 = QLabel(ConexionBD)
        self.vcLblNombre_3.setObjectName(u"vcLblNombre_3")
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        self.vcLblNombre_3.setFont(font5)
        self.vcLblNombre_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.vcLblNombre_3)

        self.vcTxtContrasenia = QLineEdit(ConexionBD)
        self.vcTxtContrasenia.setObjectName(u"vcTxtContrasenia")
        self.vcTxtContrasenia.setEnabled(True)
        self.vcTxtContrasenia.setFont(font4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.vcTxtContrasenia)

        self.vcLblNombre_4 = QLabel(ConexionBD)
        self.vcLblNombre_4.setObjectName(u"vcLblNombre_4")
        self.vcLblNombre_4.setFont(font2)
        self.vcLblNombre_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.vcLblNombre_4)

        self.vcTxtHost = QLineEdit(ConexionBD)
        self.vcTxtHost.setObjectName(u"vcTxtHost")
        self.vcTxtHost.setEnabled(True)
        self.vcTxtHost.setFont(font4)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.vcTxtHost)

        self.vcLblNombre_5 = QLabel(ConexionBD)
        self.vcLblNombre_5.setObjectName(u"vcLblNombre_5")
        self.vcLblNombre_5.setFont(font2)
        self.vcLblNombre_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.vcLblNombre_5)

        self.vcTxtPuerto = QLineEdit(ConexionBD)
        self.vcTxtPuerto.setObjectName(u"vcTxtPuerto")
        self.vcTxtPuerto.setEnabled(True)
        self.vcTxtPuerto.setFont(font4)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.vcTxtPuerto)


        self.verticalLayout.addLayout(self.formLayout)

        self.vcbtnConfirmar = QPushButton(ConexionBD)
        self.vcbtnConfirmar.setObjectName(u"vcbtnConfirmar")
        self.vcbtnConfirmar.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcbtnConfirmar.sizePolicy().hasHeightForWidth())
        self.vcbtnConfirmar.setSizePolicy(sizePolicy)
        self.vcbtnConfirmar.setFont(font2)
        self.vcbtnConfirmar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.vcbtnConfirmar)


        self.retranslateUi(ConexionBD)

        QMetaObject.connectSlotsByName(ConexionBD)
    # setupUi

    def retranslateUi(self, ConexionBD):
        ConexionBD.setWindowTitle(QCoreApplication.translate("ConexionBD", u"Conexi\u00f3nBD", None))
#if QT_CONFIG(tooltip)
        ConexionBD.setToolTip(QCoreApplication.translate("ConexionBD", u"Conexi\u00f3n a BD", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vCLblTitulo.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.vCLblTitulo.setText(QCoreApplication.translate("ConexionBD", u"CONEXI\u00d3N A BASE DE DATOS", None))
#if QT_CONFIG(tooltip)
        self.vCLblTitulo_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.vCLblTitulo_2.setText(QCoreApplication.translate("ConexionBD", u"Ingrese los datos de su conexi\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.vcLblNombre.setToolTip(QCoreApplication.translate("ConexionBD", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblNombre.setText(QCoreApplication.translate("ConexionBD", u"Base de datos", None))
#if QT_CONFIG(tooltip)
        self.vcTxtBD.setToolTip(QCoreApplication.translate("ConexionBD", u"Nombre de la base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcLblNombre_2.setToolTip(QCoreApplication.translate("ConexionBD", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblNombre_2.setText(QCoreApplication.translate("ConexionBD", u"Usuario", None))
#if QT_CONFIG(tooltip)
        self.vcTxtUsuario.setToolTip(QCoreApplication.translate("ConexionBD", u"Usuario de la Base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcLblNombre_3.setToolTip(QCoreApplication.translate("ConexionBD", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblNombre_3.setText(QCoreApplication.translate("ConexionBD", u"Contrase\u00f1a", None))
#if QT_CONFIG(tooltip)
        self.vcTxtContrasenia.setToolTip(QCoreApplication.translate("ConexionBD", u"Contrase\u00f1a de la base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcLblNombre_4.setToolTip(QCoreApplication.translate("ConexionBD", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblNombre_4.setText(QCoreApplication.translate("ConexionBD", u"Host", None))
#if QT_CONFIG(tooltip)
        self.vcTxtHost.setToolTip(QCoreApplication.translate("ConexionBD", u"Contrase\u00f1a de la base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcLblNombre_5.setToolTip(QCoreApplication.translate("ConexionBD", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblNombre_5.setText(QCoreApplication.translate("ConexionBD", u"Puerto", None))
#if QT_CONFIG(tooltip)
        self.vcTxtPuerto.setToolTip(QCoreApplication.translate("ConexionBD", u"Contrase\u00f1a de la base de datos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcbtnConfirmar.setToolTip(QCoreApplication.translate("ConexionBD", u"Confirmar cambios", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnConfirmar.setText(QCoreApplication.translate("ConexionBD", u"Confirmar", None))
    # retranslateUi

