import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFrame, QMessageBox

from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

# import login from one step above
path.append(abs(jn(dir(__file__), '..')))
from app.view.login import Ui_Login

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
