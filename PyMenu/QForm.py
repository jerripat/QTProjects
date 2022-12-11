import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backup Settings")

        # Set verticle layout...QHBox.. for horizontal
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add widgets
        label_1 = qtw.QLabel("This is my new form")
        label_1.setFont(qtg.QFont("Helvetica", 24))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        #Arr rows
        form_layout.addRow(label_1)
        form_layout.addRow("First Name", f_name)
        form_layout.addRow("Last Name", l_name)
        form_layout.addRow(qtw.QPushButton("Press me!",
                clicked = lambda: press_it()))

        self.show()

        def press_it():
            label_1.setText(f"You clicked the Button, {f_name.text()}, {l_name.text()}!")

app = qtw.QApplication([" "])
mw = MainWindow()
app.exec_()
