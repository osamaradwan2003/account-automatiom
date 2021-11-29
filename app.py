from securty import *
from PyQt5 import QtWidgets
import sys
from mainwindow import Application
from securty import setActiveded
from active import ActiveDialog


def start_app():
    activeStatus = setActiveded()
    app = QtWidgets.QApplication(sys.argv)
    if activeStatus[0] == True:
        myApp = Application()
        myApp.show()
        app.exec_()
    else:
        myApp = ActiveDialog()
        myApp.show()
        app.exec_()
        if(myApp.actived):
            sys.exit()


if __name__ == '__main__':
    start_app()
