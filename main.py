from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setFixedWidth(width)
    MainWindow.show()
    sys.exit(app.exec_())