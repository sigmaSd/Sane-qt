import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_StackedWidget
from subprocess import getoutput
from subprocess import run
from pathlib import  Path

class StartQT5(QtWidgets.QStackedWidget):

    global  directory
    global  name_changed

    def switch_window(self):
        if self.ui.listWidget.count() > 0 :
            self.ui.page.hide()
            self.ui.page_2.show()

    def back_to_main(self):
        self.ui.page_2.hide()
        self.ui.page.show()

    def scanners_list(self):

        final_list = []
        raw_output = getoutput("scanimage -L")
        #raw_output ="azeae"
        lines_list = raw_output.split('\n')
        for line in lines_list:
            line = line.lstrip("device")
            for i in range(0, line.__len__()):
                if line[i] == "'":
                    final_list.append(line[2:i])
                    break

        if final_list == [] :
            self.ui.label_2.show()
            self.ui.listWidget.hide()
        for i in final_list:
            self.ui.listWidget.addItem(i)

        self.ui.listWidget.focusNextChild()
    def check_again(self):
        self.ui.listWidget.clear()
        self.ui.listWidget.show()
        self.ui.label_2.hide()
        self.scanners_list()


    def dir (self) :
        self.directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.pushButton_5.setText("Ok")
        self.ui.label.hide()


    def change_button_name(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Choose name', 'name:')
        if ok:
            self.ui.pushButton_6.setText(str(text))
            self.name_changed=True

    def scan(self):

        if self.name_changed==False :
            self.ui.label.setText("Name your file !")
            self.ui.label.show()
        if self.directory =="none" :
            self.ui.label.setText("Choose a directory first !")
        if self.name_changed and self.directory !="none" :
            device = self.ui.listWidget.currentItem().text()
            output = self.ui.pushButton_6.text().__str__().replace(" ","")
            dir = self.directory + "/" + output
            run([" scanimage -d " + device + ">" + " " + dir ], shell=True)
            if Path(dir).is_file():
                self.ui.label.setPixmap(QtGui.QPixmap(dir).scaled(QtCore.QSize(256,271)))
                self.ui.label.show()
                self.ui.pushButton_6.setText("choose name")
                self.name_changed=False

    def __init__(self, parent=None):
        super(StartQT5,self).__init__()
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self)
        self.directory="none"
        self.name_changed = False
        self.ui.label_2.hide()
        self.scanners_list()
        self.ui.page_2.hide()
        self.ui.page.show()
        self.ui.pushButton.clicked.connect(self.switch_window)
        self.ui.pushButton_5.clicked.connect(self.dir)
        self.ui.pushButton_6.clicked.connect(self.change_button_name)
        self.ui.pushButton_3.clicked.connect(self.scan)
        self.ui.pushButton_4.clicked.connect(self.back_to_main)
        self.ui.pushButton_2.clicked.connect(self.check_again)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartQT5()
    myapp.show()
    sys.exit(app.exec_())
