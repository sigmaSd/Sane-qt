# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(400, 300)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(210, 40, 291, 231))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 131, 37))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 170, 107, 37))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 221, 231))
        self.label_2.setObjectName("label_2")
        StackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(200, 40, 171, 231))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 100, 107, 37))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 200, 107, 37))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 60, 131, 37))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 20, 107, 37))
        self.pushButton_6.setObjectName("pushButton_6")
        StackedWidget.addWidget(self.page_2)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("sane-qt", "sane-qt"))
        self.pushButton.setText(_translate("StackedWidget", "confirm selected"))
        self.pushButton_2.setText(_translate("StackedWidget", "check again"))
        self.pushButton_3.setText(_translate("StackedWidget", "scan"))
        self.pushButton_4.setText(_translate("StackedWidget", "Devices List"))
        self.pushButton_5.setText(_translate("StackedWidget", "choose directory"))
        self.pushButton_6.setText(_translate("StackedWidget", "choose name"))
        self.label_2.setText(_translate("StackedWidget",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ff0000;\">No devices found.</span></p><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ff0000;\">Press check again to rescan .</span></p></body></html>"))



