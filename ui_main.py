# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 802)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 127, 164, 255), stop:0.427447 rgba(56, 91, 117,235), stop:1 rgba(36, 57, 73,255));\n"
"font-family: Noto Sans;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_upload_competitors = QPushButton(self.centralwidget)
        self.btn_upload_competitors.setObjectName(u"btn_upload_competitors")
        self.btn_upload_competitors.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-top-left-radius: 7px;\n"
"height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_upload_competitors)

        self.btn_upload_result = QPushButton(self.centralwidget)
        self.btn_upload_result.setObjectName(u"btn_upload_result")
        self.btn_upload_result.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-top-right-radius: 7px;\n"
"height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_upload_result)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_calculate = QPushButton(self.centralwidget)
        self.btn_calculate.setObjectName(u"btn_calculate")
        self.btn_calculate.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.verticalLayout.addWidget(self.btn_calculate)

        self.tableView_2 = QTableView(self.centralwidget)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"}\n"
"QHeaderView::section {\n"
"qproperty-defaultAlignment: AlignLeft;\n"
"background-color: rgba(255,255,255,30);\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,40);\n"
"height: 35px;\n"
"}\n"
"QTableView::item {\n"
"color: white;\n"
"border-style: none;\n"
"border-bottom: rgba(255,255,255,50);\n"
"}\n"
"QTableView::item:selected {\n"
"border: none;\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.tableView_2.setAlternatingRowColors(False)
        self.tableView_2.setShowGrid(True)

        self.verticalLayout.addWidget(self.tableView_2)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-left-radius: 7px;\n"
"border-bottom-right-radius: 7px;\n"
"height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.verticalLayout.addWidget(self.btn_save)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Result Calculator", None))
        self.btn_upload_competitors.setText(QCoreApplication.translate("MainWindow", u"Upload competitors file", None))
        self.btn_upload_result.setText(QCoreApplication.translate("MainWindow", u"Upload result file", None))
        self.btn_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

