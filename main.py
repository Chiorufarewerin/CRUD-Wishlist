'''Main file of programm.'''

import sys
from PyQt5 import QtWidgets # pylint: disable=unused-import
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow # pylint: disable=unused-import
from forms.Ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    '''Inherited class from Ui_MainWindow where implemented functional.'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

def main():
    '''Start application function.'''
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    app.exec_()

if __name__ == '__main__':
    main()
    