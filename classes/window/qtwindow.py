import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFrame, QMessageBox

GuiApp = QApplication(sys.argv)

class QtWindow(QWidget):
    def __init__(self, ui, app):
        super().__init__()
        self.app = app
        self.ui = ui
        self.ui.setupUi(self)

    def open(self):
        self.show()
        sys.exit(self.app.exec())

    def close(self):
        self.close()
