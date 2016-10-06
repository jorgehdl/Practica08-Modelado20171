import sys
from PyQt4 import QtCore, QtGui, uic
 
Ui_MainWindow = uic.loadUiType("cliente.ui")[0]
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.tw.horizontalHeader().setVisible(False)
    window.tw.verticalHeader().setVisible(False)
    window.tw.horizontalHeader().setResizeMode(1)
    window.tw.verticalHeader().setResizeMode(1)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()