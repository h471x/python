import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFrame, QMessageBox
from login import Ui_Login

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Login()
        self.ui.setupUi(self)

if __name__=='__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
