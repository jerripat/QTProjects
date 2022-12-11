import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backup Settings")

        # Set verticle layout...QHBox.. for horizontal
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Select Backup Type")
        my_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_label)

        # Create Text box
        my_textBox = qtw.QTextEdit(
            self,
            acceptRichText=True,
            html="<h1><center>Big header text!</h1></center>",
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Hello World!",
            readOnly=False,
        )

        self.layout().addWidget(my_textBox)

        my_button = qtw.QPushButton("Press me", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        # def press_it():
        # my_label.setText(f"You selected... {my_combo.currentText()}")
        # Clear entry box on press_it
        # my_entry.setText("")

        def press_it():
            my_label.setText(f"You selected... {my_textBox.toPlainText()} ")
            my_textBox.setPlainText("You pressed the button!")


app = qtw.QApplication([" "])
mw = MainWindow()
app.exec_()
