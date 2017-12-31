from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName(_fromUtf8("StackedWidget"))
        StackedWidget.resize(400, 300)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.listWidget = QtGui.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(140, 20, 256, 271))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(6, 30, 111, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(0, 70, 131, 37))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        StackedWidget.addWidget(self.page)
        self.page1 = QtGui.QWidget()
        self.page1.setObjectName(_fromUtf8("page1"))
        self.graphicsView = QtGui.QLabel(self.page1)
        self.graphicsView.setGeometry(QtCore.QRect(140, 20, 256, 271))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.pushButton_2 = QtGui.QPushButton(self.page1)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 90, 107, 37))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.page1)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 40, 131, 37))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.page1)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 110, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setText("Choose name")
        self.pushButton_5 = QtGui.QPushButton(self.page1)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 230, 107, 37))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setText("Devices List")
        StackedWidget.addWidget(self.page1)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(_translate("Saneqt", "Saneqt", None))
        self.label.setText(_translate("StackedWidget", "Devices Found :", None))
        self.pushButton.setText(_translate("StackedWidget", "Confirm Selected", None))
        self.pushButton_2.setText(_translate("StackedWidget", "Scan", None))
        self.pushButton_3.setText(_translate("StackedWidget", "Choose dir", None))