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

        # Spin box, QDouble to use floats
        my_spin = qtw.QSpinBox(self,
            value=10,
            maximum=100,
            minimum=0,
            singleStep=5,
            prefix="Your order is #",
            #suffix=" Order",
            )
        # Change font size of spin box
        my_spin.setFont(qtg.QFont('Helvetica', 18))

        self.layout().addWidget(my_spin)

        # Create Combo box
        # my_combo = qtw.QComboBox(self)
        # my_combo.addItem("rsync")
        # my_combo.addItem("rClone")
        # my_combo.addItem("Tar")
        # my_combo.addItem("Directory")

        # Put combo box on screen
        #self.layout().addWidget(my_combo)

        # Entry box
        # my_entry = qtw.QLineEdit()my_spin
        # my_entry.setObjectName("name_field")
        # my_entry.setText("")
        # self.layout().addWidget(my_entry)

        my_button = qtw.QPushButton("Press me", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        #def press_it():
            #my_label.setText(f"You selected... {my_combo.currentText()}")
            # Clear entry box on press_it
            # my_entry.setText("")

        def press_it():
            my_label.setText(f"You selected...# {my_spin.value()} ")


app = qtw.QApplication([" "])
mw = MainWindow()
app.exec_()
