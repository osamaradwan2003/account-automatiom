from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5 import uic
from auto import Automation
import multiprocessing
import threading
from helpers import showMss
from filesmanger import get_account_from_file


class Application(QtWidgets.QMainWindow, QtGui.QPixmap):
    running = False
    filePath = ''
    folder_path = ''

    def __init__(self):
        super(Application, self).__init__()
        uic.loadUi('./gui.ui', self)
        self.set__window_ico()
        self.auto_state = True
        self.automated.stateChanged.connect(self.set_auto_state)
        self.automation = Automation(
            runing=self.running, parent=self, automated=self.auto_state)
        self.autom = threading.Thread(target=self.automation.run)
        self.brs_btns()
        self.start_puse_b()
        self.update_info([0, 0, 0, 0], 0, 0)

    def set_auto_state(self, checked):
        self.auto_state = bool(checked)
        self.automation.set_automated(self.auto_state)

    def set__window_ico(self):
        self.setWindowIcon(QtGui.QIcon('./assests/icons/icon.png'))

    def brs_btns(self):
        self.brows_btn.setIcon(QtGui.QIcon('./assests/icons/plus.ico'))
        self.brows_btn.clicked.connect(self.browse_btn_fun)
        self.save_btn.setIcon(QtGui.QIcon('./assests/icons/plus.ico'))
        self.save_btn.clicked.connect(self.save_btn_func)

    def browse_btn_fun(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'اختار ملف الحسابات', '', '*.txt')
        if self.automation.set_file_path(filename) == False:
            showMss(self)
            return
        try:
            d, c, f = get_account_from_file(filename)
            self.file_path.setText(filename)
            self.filePath = filename
        except Exception as e:

            showMss(self, text='خطأ فى ملف الكوكيز')
            self.file_path.setText('')
            self.filePath = ''
            return

    def save_btn_func(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'مكان الحفظ', '')
        if self.automation.set_folder_path(folder_path) == False:
            showMss(self)
            return
        self.save_path.setText(folder_path)
        self.folder_path = folder_path

    def start_puse_b(self):
        self.start_puse_btn.clicked.connect(self.start_puse_fun)

    def closeEvent(self, event: QtGui.QCloseEvent):
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

    def start_puse_fun(self):

        if(self.automation.folderPath.strip() != '') and (self.automation.filePath.strip() != ''):

            if(self.running == False):
                self.start_puse_btn.setIcon(
                    QtGui.QIcon('./assests/icons/puse.png'))
                self.start_puse_btn.setToolTip('ايقاف')
                self.running = True
                self.automation.setStutus(self.running)
                try:
                    self.autom.start()
                except:
                    self.autom = threading.Thread(
                        target=self.automation.run)
                    self.autom.start()
            elif(self.running == True):
                self.start_puse_btn.setIcon(
                    QtGui.QIcon('./assests/icons/start.png'))
                self.start_puse_btn.setToolTip('تشغيل')
                self.running = False
                self.automation.setStutus(self.running)
        else:
            showMss(self)
            return

    def update_info(self, info, value1, value2):
        done, check, fill, unknow = info
        comp_label = """
            < html > <head/>
            < body dir='rtl' >
                < b >
                < center >
                < span > {} < /span >
                < sapn > من < /span >
                < span > {} < /span >
                < / center >
                < / b >
            < / body >
            < / html >
            """
        self.done_lable.setText('<center><b>{}</b></center>'.format(done))
        self.check_lable.setText('<center><b>{}</b></center>'.format(check))
        self.fill_lable.setText('<center><b>{}</b></center>'.format(fill))
        self.unknown_label.setText('<center><b>{}</b></center>'.format(unknow))
        self.compleated.setText(comp_label.format(value1, value2))
