from securty import *
from PyQt5 import QtGui, QtWidgets
from PyQt5 import uic
import sys
from securty import *
from helpers import showMss


class ActiveDialog(QtWidgets.QMainWindow):
    serial = ''

    def __init__(self):
        super(ActiveDialog, self).__init__()
        uic.loadUi('activa.ui', self)
        self.get_serial()
        self.btns_mang()
        self.setWindowIcon(QtGui.QIcon('./assests/icons/icon.png'))
        self.actived = False

    def get_serial(self):
        self.serial_inp.textChanged.connect(self.set_serial)

    def set_serial(self, serial):
        self.serial = serial

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setText("هل تريد الاغلاق")
        close.setWindowTitle('اغلاق')
        close.setWindowIcon(QtGui.QIcon('./assests/icons/icon.png'))
        close.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        close = close.exec()
        if close == QtWidgets.QMessageBox.Yes:
            try:
                self.autom.terminate()
            except:
                pass
            event.accept()
        else:
            event.ignore()

    def btns_mang(self):
        self.acept_btns.accepted.connect(self.accept)
        self.acept_btns.rejected.connect(self.reject)

    def accept(self):
        serial_mange = setActiveded(self.serial)
        if serial_mange[0] == True:
            showMss(self, title='تم', text=serial_mange[1])
            self.actived = True
        else:
            showMss(self, text=serial_mange[1])

    def reject(self):
        self.close()
        sys.exit()
