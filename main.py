import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_root  # "root" matches your objectName for the main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)

        # Connect buttons to methods
        self.ui.btnS.clicked.connect(self.submit)
        self.ui.btnR.clicked.connect(self.reset)
        self.ui.btnQ.clicked.connect(self.quit_app)

    def submit(self):
        first = self.ui.entFirst.text()
        last  = self.ui.entLast.text()
        email = self.ui.entEmail.text()
        phone = self.ui.entPhone.text()

        # Validate required fields
        if not first or not last:
            QMessageBox.warning(self, "Missing Info", "First Name and Last Name are required.")
            return

        # Print to console
        print(f"First: {first}, Last: {last}, Email: {email}, Phone: {phone}")
        QMessageBox.information(self, "Submitted", f"Name: {first} {last}\nEmail: {email}\nPhone: {phone}")

    def reset(self):
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()

    def quit_app(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())