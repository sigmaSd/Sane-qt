import sys
from PyQt4 import QtCore, QtGui
from saneqt import Ui_StackedWidget
from subprocess import getoutput
from subprocess import run

class StartQT4(QtGui.QStackedWidget):

    global directory

    def switch_window(self):
        self.ui.page.hide()
        self.ui.page1.show()
    def back_to_main(self):
        self.ui.page1.hide()
        self.ui.page.show()

    def scanners_list(self):
        final_list = []
        raw_output = getoutput("scanimage -L")
        lines_list = raw_output.split('\n')
        for line in lines_list:
            line = line.lstrip("device")
            for i in range(0, line.__len__()):
                if line[i] == "'":
                    final_list.append(line[2:i])
                    break
        for i in final_list:
            self.ui.listWidget.addItem(i)


    def dir (self) :
        self.directory = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.pushButton_3.setText("Ok")


    def change_button_name(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Choose name', 'name:')
        if ok:
            self.ui.pushButton_4.setText(str(text))

    def scan(self):
        device = self.ui.listWidget.currentItem().text()
        output = self.ui.pushButton_4.text().__str__()
        dir = self.directory + "/" + output


        run([" scanimage -d " + device + ">" + " " + dir ], shell=True)
        self.ui.graphicsView.setPixmap(QtGui.QPixmap(dir).scaled(QtCore.QSize(256,271)))

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self)
        self.scanners_list()
        self.ui.page.show()
        self.ui.page1.hide()

        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),self.switch_window)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.dir)
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.change_button_name)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.scan)
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.back_to_main)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
