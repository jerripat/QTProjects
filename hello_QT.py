import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World!")

        # Set verticle layout...QHBox.. for horizontal
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Whats your name?")
        my_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_label)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        my_button = qtw.QPushButton("Press me", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f"Hello {my_entry.text()}")
            my_entry.setText("")


app = qtw.QApplication([" "])
mw = MainWindow()
app.exec_()
