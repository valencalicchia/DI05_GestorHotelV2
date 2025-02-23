# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_edit_cliente.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QFormLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Cliente(object):
    def setupUi(self, Cliente):
        if not Cliente.objectName():
            Cliente.setObjectName(u"Cliente")
        Cliente.setWindowModality(Qt.WindowModality.WindowModal)
        Cliente.resize(652, 462)
        Cliente.setMinimumSize(QSize(651, 462))
        self.verticalLayout = QVBoxLayout(Cliente)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vCLblTitulo = QLabel(Cliente)
        self.vCLblTitulo.setObjectName(u"vCLblTitulo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vCLblTitulo.sizePolicy().hasHeightForWidth())
        self.vCLblTitulo.setSizePolicy(sizePolicy)
        self.vCLblTitulo.setMinimumSize(QSize(25, 0))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.vCLblTitulo.setFont(font)
        self.vCLblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vCLblTitulo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.vcLblNombre = QLabel(Cliente)
        self.vcLblNombre.setObjectName(u"vcLblNombre")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.vcLblNombre.setFont(font1)
        self.vcLblNombre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.vcLblNombre)

        self.vcTxtNombre = QLineEdit(Cliente)
        self.vcTxtNombre.setObjectName(u"vcTxtNombre")
        self.vcTxtNombre.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(14)
        self.vcTxtNombre.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.vcTxtNombre)

        self.vcLblApellidos = QLabel(Cliente)
        self.vcLblApellidos.setObjectName(u"vcLblApellidos")
        self.vcLblApellidos.setFont(font1)
        self.vcLblApellidos.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.vcLblApellidos)

        self.vcTxtApellidos = QLineEdit(Cliente)
        self.vcTxtApellidos.setObjectName(u"vcTxtApellidos")
        self.vcTxtApellidos.setEnabled(True)
        self.vcTxtApellidos.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.vcTxtApellidos)

        self.vclblDni = QLabel(Cliente)
        self.vclblDni.setObjectName(u"vclblDni")
        self.vclblDni.setFont(font1)
        self.vclblDni.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.vclblDni)

        self.vcTxtDni = QLineEdit(Cliente)
        self.vcTxtDni.setObjectName(u"vcTxtDni")
        self.vcTxtDni.setEnabled(True)
        self.vcTxtDni.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.vcTxtDni)

        self.vclblFechaNac = QLabel(Cliente)
        self.vclblFechaNac.setObjectName(u"vclblFechaNac")
        self.vclblFechaNac.setFont(font1)
        self.vclblFechaNac.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.vclblFechaNac)

        self.vcdateEdit = QDateEdit(Cliente)
        self.vcdateEdit.setObjectName(u"vcdateEdit")
        self.vcdateEdit.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.vcdateEdit)

        self.vclblPais = QLabel(Cliente)
        self.vclblPais.setObjectName(u"vclblPais")
        self.vclblPais.setFont(font1)
        self.vclblPais.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.vclblPais)

        self.vcTxtPais = QLineEdit(Cliente)
        self.vcTxtPais.setObjectName(u"vcTxtPais")
        self.vcTxtPais.setEnabled(True)
        self.vcTxtPais.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.vcTxtPais)

        self.vclblTelefono = QLabel(Cliente)
        self.vclblTelefono.setObjectName(u"vclblTelefono")
        self.vclblTelefono.setFont(font1)
        self.vclblTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.vclblTelefono)

        self.vcTxtTelefono = QLineEdit(Cliente)
        self.vcTxtTelefono.setObjectName(u"vcTxtTelefono")
        self.vcTxtTelefono.setEnabled(True)
        self.vcTxtTelefono.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.vcTxtTelefono)

        self.vclblEmail = QLabel(Cliente)
        self.vclblEmail.setObjectName(u"vclblEmail")
        self.vclblEmail.setFont(font1)
        self.vclblEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.vclblEmail)

        self.vcTxtEmail = QLineEdit(Cliente)
        self.vcTxtEmail.setObjectName(u"vcTxtEmail")
        self.vcTxtEmail.setEnabled(True)
        self.vcTxtEmail.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.vcTxtEmail)

        self.vcLayOutCongreso = QHBoxLayout()
        self.vcLayOutCongreso.setSpacing(6)
        self.vcLayOutCongreso.setObjectName(u"vcLayOutCongreso")
        self.vcLayOutCongreso.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.vcchkBoxMenores = QCheckBox(Cliente)
        self.vcchkBoxMenores.setObjectName(u"vcchkBoxMenores")
        self.vcchkBoxMenores.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vcchkBoxMenores.sizePolicy().hasHeightForWidth())
        self.vcchkBoxMenores.setSizePolicy(sizePolicy1)
        self.vcchkBoxMenores.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.vcchkBoxMenores.setFont(font3)

        self.vcLayOutCongreso.addWidget(self.vcchkBoxMenores)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.vcLblJornadas = QLabel(Cliente)
        self.vcLblJornadas.setObjectName(u"vcLblJornadas")
        self.vcLblJornadas.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.vcLblJornadas.sizePolicy().hasHeightForWidth())
        self.vcLblJornadas.setSizePolicy(sizePolicy2)
        self.vcLblJornadas.setMaximumSize(QSize(80, 30))
        self.vcLblJornadas.setFont(font3)
        self.vcLblJornadas.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.vcLblJornadas)

        self.vccboBoxSexo = QComboBox(Cliente)
        self.vccboBoxSexo.setObjectName(u"vccboBoxSexo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.vccboBoxSexo.sizePolicy().hasHeightForWidth())
        self.vccboBoxSexo.setSizePolicy(sizePolicy3)
        self.vccboBoxSexo.setFont(font2)

        self.horizontalLayout_8.addWidget(self.vccboBoxSexo)


        self.vcLayOutCongreso.addLayout(self.horizontalLayout_8)


        self.formLayout.setLayout(7, QFormLayout.FieldRole, self.vcLayOutCongreso)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Cliente)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout.addWidget(self.widget)

        self.vcbtnEliminar = QPushButton(Cliente)
        self.vcbtnEliminar.setObjectName(u"vcbtnEliminar")
        self.vcbtnEliminar.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.vcbtnEliminar.sizePolicy().hasHeightForWidth())
        self.vcbtnEliminar.setSizePolicy(sizePolicy3)
        self.vcbtnEliminar.setFont(font1)
        self.vcbtnEliminar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.horizontalLayout.addWidget(self.vcbtnEliminar)

        self.vcbtnConfirmar = QPushButton(Cliente)
        self.vcbtnConfirmar.setObjectName(u"vcbtnConfirmar")
        self.vcbtnConfirmar.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.vcbtnConfirmar.sizePolicy().hasHeightForWidth())
        self.vcbtnConfirmar.setSizePolicy(sizePolicy3)
        self.vcbtnConfirmar.setFont(font1)
        self.vcbtnConfirmar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.horizontalLayout.addWidget(self.vcbtnConfirmar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Cliente)

        QMetaObject.connectSlotsByName(Cliente)
    # setupUi

    def retranslateUi(self, Cliente):
        Cliente.setWindowTitle(QCoreApplication.translate("Cliente", u"GestionarReserva", None))
#if QT_CONFIG(tooltip)
        Cliente.setToolTip(QCoreApplication.translate("Cliente", u"Gesti\u00f3n de una reserva", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vCLblTitulo.setToolTip(QCoreApplication.translate("Cliente", u"Crear/Editar una reserva", None))
#endif // QT_CONFIG(tooltip)
        self.vCLblTitulo.setText(QCoreApplication.translate("Cliente", u"GESTIONAR CLIENTE", None))
#if QT_CONFIG(tooltip)
        self.vcLblNombre.setToolTip(QCoreApplication.translate("Cliente", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblNombre.setText(QCoreApplication.translate("Cliente", u"Nombre", None))
#if QT_CONFIG(tooltip)
        self.vcTxtNombre.setToolTip(QCoreApplication.translate("Cliente", u"Nombre del/la cliente/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcLblApellidos.setToolTip(QCoreApplication.translate("Cliente", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblApellidos.setText(QCoreApplication.translate("Cliente", u"Apellidos", None))
#if QT_CONFIG(tooltip)
        self.vcTxtApellidos.setToolTip(QCoreApplication.translate("Cliente", u"Apellidos del/la cliente/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vclblDni.setToolTip(QCoreApplication.translate("Cliente", u"Tel\u00e9fono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vclblDni.setText(QCoreApplication.translate("Cliente", u"DNI", None))
#if QT_CONFIG(tooltip)
        self.vcTxtDni.setToolTip(QCoreApplication.translate("Cliente", u"DNI del/la cliente/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vclblFechaNac.setToolTip(QCoreApplication.translate("Cliente", u"Fecha del evento", None))
#endif // QT_CONFIG(tooltip)
        self.vclblFechaNac.setText(QCoreApplication.translate("Cliente", u"Fecha Nacimiento", None))
#if QT_CONFIG(tooltip)
        self.vcdateEdit.setToolTip(QCoreApplication.translate("Cliente", u"Fecha de nacimiento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vclblPais.setToolTip(QCoreApplication.translate("Cliente", u"Tel\u00e9fono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vclblPais.setText(QCoreApplication.translate("Cliente", u"Pais", None))
#if QT_CONFIG(tooltip)
        self.vcTxtPais.setToolTip(QCoreApplication.translate("Cliente", u"Pa\u00eds de origen", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vclblTelefono.setToolTip(QCoreApplication.translate("Cliente", u"Tel\u00e9fono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vclblTelefono.setText(QCoreApplication.translate("Cliente", u"Telefono", None))
#if QT_CONFIG(tooltip)
        self.vcTxtTelefono.setToolTip(QCoreApplication.translate("Cliente", u"Telefono del/la cliente/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vclblEmail.setToolTip(QCoreApplication.translate("Cliente", u"Fecha del evento", None))
#endif // QT_CONFIG(tooltip)
        self.vclblEmail.setText(QCoreApplication.translate("Cliente", u"Email", None))
#if QT_CONFIG(tooltip)
        self.vcTxtEmail.setToolTip(QCoreApplication.translate("Cliente", u"Email del/la cliente/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcchkBoxMenores.setToolTip(QCoreApplication.translate("Cliente", u"\u00bfHijos menores?", None))
#endif // QT_CONFIG(tooltip)
        self.vcchkBoxMenores.setText(QCoreApplication.translate("Cliente", u"Hijos menores", None))
        self.vcLblJornadas.setText(QCoreApplication.translate("Cliente", u"Sexo:", None))
#if QT_CONFIG(tooltip)
        self.vccboBoxSexo.setToolTip(QCoreApplication.translate("Cliente", u"Sexo del cliente", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcbtnEliminar.setToolTip(QCoreApplication.translate("Cliente", u"Eliminar cliente ", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnEliminar.setText(QCoreApplication.translate("Cliente", u"Eliminar", None))
#if QT_CONFIG(tooltip)
        self.vcbtnConfirmar.setToolTip(QCoreApplication.translate("Cliente", u"Confirmar cambios", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnConfirmar.setText(QCoreApplication.translate("Cliente", u"Confirmar", None))
    # retranslateUi

