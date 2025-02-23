# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acerca_de.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_Acerca(object):
    def setupUi(self, Acerca):
        if not Acerca.objectName():
            Acerca.setObjectName(u"Acerca")
        Acerca.setWindowModality(Qt.WindowModality.WindowModal)
        Acerca.resize(538, 364)
        self.textBrowser = QTextBrowser(Acerca)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 30, 481, 291))
        self.textBrowser.setMinimumSize(QSize(391, 231))
        self.textBrowser.setMaximumSize(QSize(9999, 9999))
        font = QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)

        self.retranslateUi(Acerca)

        QMetaObject.connectSlotsByName(Acerca)
    # setupUi

    def retranslateUi(self, Acerca):
        Acerca.setWindowTitle(QCoreApplication.translate("Acerca", u"Acerca de", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Acerca", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">Acerca de</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Esta aplicaci\u00f3n permite "
                        "gestionar la reserva de salones para eventos, facilitando la consulta de disponibilidad, creaci\u00f3n y modificaci\u00f3n de reservas. Tambi\u00e9n integra la gesti\u00f3n de clientes para un manejo eficiente de la informaci\u00f3n.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Desarrollado por Valen.</p></body></html>", None))
    # retranslateUi

