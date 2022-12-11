import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):
    def __init__(self):
        """Main Window constructor"""
        super().__init__()
        # Main UI code goes here
        if __name__=='__main__':
            app = qtw.QApplication(sys.argv)
            mw = MainWindow()
            sys.exit(app.exec())

        # End main UI code
        self.show()