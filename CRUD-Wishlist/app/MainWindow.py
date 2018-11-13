'''Start main form'''

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from forms.Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    '''Inherited class from Ui_MainWindow where implemented functional.'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def resizeEvent(self, a0):
        photo_size = self.PhotoLabel.size()
        max = photo_size.height()
        if max > photo_size.width():
            max = photo_size.width()
        if (self.PhotoLabel.pixmap() is not None
                and not self.PhotoLabel.pixmap().isNull()):
            pixmap = self.PhotoLabel.pixmap()
            image_size = pixmap.size()
            if image_size.height() > max:
                max = image_size.height()
            if image_size.width() > max:
                max = image_size.width()
        layout = self.PhotoFrame.layout()
        left, top, right, bottom = layout.getContentsMargins()
        left = right = (self.PhotoFrame.size().width() - 40 - max) // 2
        top = bottom = (self.PhotoFrame.size().height() - max) // 2
        print(left, top, right, bottom, max)
        if left < 20:
            left, right, top, bottom = 20, 20, top, bottom
        if top < 20:
            left, right, top, bottom = left, right, 20, 20
        layout.setContentsMargins(left, top, right, bottom)

    def showEvent(self, a0):
        super().showEvent(a0)
        self.resizeEvent(None)


def start(argv):
    '''Start application function.'''
    app = QApplication(argv)
    windows = MainWindow()
    windows.show()
    app.exec_()
