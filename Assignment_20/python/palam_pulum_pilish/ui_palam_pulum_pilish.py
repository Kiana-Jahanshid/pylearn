# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'palam_pulum_pilishPApuAn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(504, 627)
        font = QFont()
        font.setPointSize(5)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"border-color: rgb(170, 0, 0);\n"
"background-color: rgb(170, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.win_btn = QPushButton(self.centralwidget)
        self.win_btn.setObjectName(u"win_btn")
        self.win_btn.setGeometry(QRect(-9, 230, 531, 51))
        font1 = QFont()
        font1.setPointSize(13)
        self.win_btn.setFont(font1)
        self.win_btn.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgb(197, 158, 229);")
        self.back_btn = QPushButton(self.centralwidget)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(50, 490, 191, 81))
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.back_btn.setFont(font2)
        self.back_btn.setStyleSheet(u"border-radius: 39px;\n"
"color: rgb(0, 145, 0);\n"
"background-color: rgb(170, 85, 255);")
        self.front_btn = QPushButton(self.centralwidget)
        self.front_btn.setObjectName(u"front_btn")
        self.front_btn.setGeometry(QRect(270, 490, 191, 81))
        font3 = QFont()
        font3.setPointSize(30)
        self.front_btn.setFont(font3)
        self.front_btn.setStyleSheet(u"border-radius: 39px;\n"
"color: rgb(0, 145, 0);\n"
"background-color: rgb(170, 85, 255);")
        self.player_score_btn = QPushButton(self.centralwidget)
        self.player_score_btn.setObjectName(u"player_score_btn")
        self.player_score_btn.setGeometry(QRect(141, 431, 211, 51))
        font4 = QFont()
        font4.setPointSize(14)
        self.player_score_btn.setFont(font4)
        self.player_score_btn.setStyleSheet(u"border-radius: 15px;")
        self.com1_score = QPushButton(self.centralwidget)
        self.com1_score.setObjectName(u"com1_score")
        self.com1_score.setGeometry(QRect(10, 20, 211, 51))
        font5 = QFont()
        font5.setPointSize(12)
        self.com1_score.setFont(font5)
        self.com1_score.setStyleSheet(u"border-radius: 15px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 301, 171, 131))
        self.frame.setStyleSheet(u"border :2px ;\n"
"border-color: rgb(170, 0, 127);\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.player_choice = QPushButton(self.frame)
        self.player_choice.setObjectName(u"player_choice")
        self.player_choice.setGeometry(QRect(0, 0, 171, 131))
        font6 = QFont()
        font6.setPointSize(43)
        self.player_choice.setFont(font6)
        self.player_choice.setStyleSheet(u"border :2px solid purple;\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(39, 79, 171, 131))
        self.frame_2.setStyleSheet(u"border :2px ;\n"
"border-color: rgb(170, 0, 127);\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.comp1_choice = QPushButton(self.frame_2)
        self.comp1_choice.setObjectName(u"comp1_choice")
        self.comp1_choice.setGeometry(QRect(0, 0, 171, 131))
        self.comp1_choice.setFont(font6)
        self.comp1_choice.setStyleSheet(u"border :2px solid purple;\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(300, 79, 171, 131))
        self.frame_3.setStyleSheet(u"border :2px ;\n"
"border-color: rgb(170, 0, 127);\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.comp2_choice = QPushButton(self.frame_3)
        self.comp2_choice.setObjectName(u"comp2_choice")
        self.comp2_choice.setGeometry(QRect(0, 0, 171, 131))
        self.comp2_choice.setFont(font6)
        self.comp2_choice.setStyleSheet(u"border :2px solid purple;\n"
"border-style : dashed;\n"
"border-radius: 38px;\n"
"")
        self.comp2_score = QPushButton(self.centralwidget)
        self.comp2_score.setObjectName(u"comp2_score")
        self.comp2_score.setGeometry(QRect(270, 20, 211, 51))
        self.comp2_score.setFont(font5)
        self.comp2_score.setStyleSheet(u"border-radius: 15px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 504, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.win_btn.setText("")
        self.back_btn.setText(QCoreApplication.translate("MainWindow", u"🤚🏻", None))
        self.front_btn.setText(QCoreApplication.translate("MainWindow", u"🖐🏻", None))
        self.player_score_btn.setText(QCoreApplication.translate("MainWindow", u"Your Score : ", None))
        self.com1_score.setText(QCoreApplication.translate("MainWindow", u"Computer1 Score : ", None))
        self.player_choice.setText("")
        self.comp1_choice.setText("")
        self.comp2_choice.setText("")
        self.comp2_score.setText(QCoreApplication.translate("MainWindow", u"Computer2 Score : ", None))
    # retranslateUi

