# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asn8.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(500, 300)
        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblFrPerson = QGroupBox(self.centralwidget)
        self.lblFrPerson.setObjectName(u"lblFrPerson")
        self.lblFrPerson.setGeometry(QRect(10, 0, 121, 61))
        self.gridLayout = QGridLayout(self.lblFrPerson)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblFirst = QLabel(self.lblFrPerson)
        self.lblFirst.setObjectName(u"lblFirst")
        self.lblFirst.setStyleSheet(u"background-color: blue; color: white;")

        self.gridLayout.addWidget(self.lblFirst, 0, 0, 1, 1)

        self.entFirst = QLineEdit(self.centralwidget)
        self.entFirst.setObjectName(u"entFirst")
        self.entFirst.setGeometry(QRect(130, 20, 181, 31))
        self.lblLast = QLabel(self.centralwidget)
        self.lblLast.setObjectName(u"lblLast")
        self.lblLast.setGeometry(QRect(20, 60, 101, 20))
        self.lblLast.setStyleSheet(u"background-color: blue; color: white;")
        self.entLast = QLineEdit(self.centralwidget)
        self.entLast.setObjectName(u"entLast")
        self.entLast.setGeometry(QRect(130, 50, 181, 31))
        self.lblEmail = QLabel(self.centralwidget)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setGeometry(QRect(10, 100, 49, 16))
        self.entEmail = QLineEdit(self.centralwidget)
        self.entEmail.setObjectName(u"entEmail")
        self.entEmail.setGeometry(QRect(130, 90, 221, 26))
        self.lblPhone = QLabel(self.centralwidget)
        self.lblPhone.setObjectName(u"lblPhone")
        self.lblPhone.setGeometry(QRect(10, 140, 49, 16))
        self.entPhone = QLineEdit(self.centralwidget)
        self.entPhone.setObjectName(u"entPhone")
        self.entPhone.setGeometry(QRect(130, 130, 221, 26))
        self.fraButtons = QFrame(self.centralwidget)
        self.fraButtons.setObjectName(u"fraButtons")
        self.fraButtons.setGeometry(QRect(70, 170, 351, 80))
        self.fraButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.fraButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.btnS = QPushButton(self.fraButtons)
        self.btnS.setObjectName(u"btnS")
        self.btnS.setGeometry(QRect(10, 30, 81, 26))
        self.btnR = QPushButton(self.fraButtons)
        self.btnR.setObjectName(u"btnR")
        self.btnR.setGeometry(QRect(130, 30, 81, 26))
        self.btnQ = QPushButton(self.fraButtons)
        self.btnQ.setObjectName(u"btnQ")
        self.btnQ.setGeometry(QRect(260, 30, 81, 26))
        root.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(root)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        root.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(root)
        self.statusbar.setObjectName(u"statusbar")
        root.setStatusBar(self.statusbar)

        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Form", None))
        self.lblFrPerson.setTitle(QCoreApplication.translate("root", u"Personal Information", None))
        self.lblFirst.setText(QCoreApplication.translate("root", u"*First Name:", None))
        self.lblLast.setText(QCoreApplication.translate("root", u"*Last Name:", None))
        self.lblEmail.setText(QCoreApplication.translate("root", u"Email:", None))
        self.lblPhone.setText(QCoreApplication.translate("root", u"Phone:", None))
        self.btnS.setText(QCoreApplication.translate("root", u"Submit", None))
        self.btnR.setText(QCoreApplication.translate("root", u"Reset", None))
        self.btnQ.setText(QCoreApplication.translate("root", u"Quit", None))
    # retranslateUi

