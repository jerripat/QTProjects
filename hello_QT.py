import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World!")

        # Set verticle layout...QHBox.. for horizontal
        self.setLayout(qtw.QVBoxLayout())

        my_Label = qtw.QLabel("Hello World")
        my_Label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_Label)


        self.show()

app = qtw.QApplication([" "])
mw = MainWindow()

app.exec_()
