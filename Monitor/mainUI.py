# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 768)
        Form.setStyleSheet(u"background-color: rgb(246, 247, 248);")
        self.logo = QLabel(Form)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(609, 100, 148, 50))
        self.logo.setStyleSheet(u"border-image: url(:/logo/img/logo_little.png);")
        self.label_goBms = QLabel(Form)
        self.label_goBms.setObjectName(u"label_goBms")
        self.label_goBms.setGeometry(QRect(411, 540, 542, 82))
        self.label_goBms.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 10px;\n"
"shadow: 0px 4px 10px rgba(184, 184, 184, 0.2);")
        self.label_goBms.setFrameShape(QFrame.StyledPanel)
        self.label_goBms.setFrameShadow(QFrame.Raised)
        self.label_goBms.setLineWidth(10)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(410, 540, 541, 81))
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.goBms)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText("")
        self.label_goBms.setText("")
        self.pushButton.setText("")
    # retranslateUi

