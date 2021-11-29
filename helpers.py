from PyQt5 import QtWidgets

def showMss(parent, title='خطأ', text: str = 'برجاء تحديد المسار'):
    dlg = QtWidgets.QMessageBox(parent)
    dlg.setWindowTitle(title)
    dlg.setText(text)
    button = dlg.exec()
    if button == QtWidgets.QMessageBox.Ok:
        dlg.close()

