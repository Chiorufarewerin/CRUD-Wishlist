'''Start main form'''

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from forms.Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    '''Inherited class from Ui_MainWindow where implemented functional.'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


def start(argv):
    '''Start application function.'''
    app = QApplication(argv)
    windows = MainWindow()
    windows.show()
    app.exec_()
