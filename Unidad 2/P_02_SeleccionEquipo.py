import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_02_SeleccionEquipo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.cb_amando.toggled.connect(self.sel_amando)
        self.cb_raul.toggled.connect(self.sel_raul)
        self.cb_bonilla.toggled.connect(self.sel_bonilla)
        self.cb_jeremy.toggled.connect(self.sel_jeremy)
        self.cb_frida.toggled.connect(self.sel_frida)

        self.amando = ""
        self.raul = ""
        self.bonilla = ""
        self.jeremy = ""
        self.frida = ""

    def sel_amando(self):
        if self.cb_amando.isChecked():
            print("Amando True")
            self.amando = "AMANDO\n"
        else:
            print("Amando False")
            self.amando = ""
        self.txt_equipo.setPlainText(self.amando + self.raul + self.bonilla + self.jeremy + self.frida)

    def sel_raul(self):
        if self.cb_raul.isChecked():
            print("Raul True")
            self.raul = "RAUL\n"
        else:
            print("Raul False")
            self.amando = ""
        self.txt_equipo.setPlainText(self.amando + self.raul + self.bonilla + self.jeremy + self.frida)

    def sel_bonilla(self):
        if self.cb_bonilla.isChecked():
            print("Bonilla True")
            self.bonilla = "BONILLA\n"
        else:
            print("Bonilla False")
            self.bonilla = ""
        self.txt_equipo.setPlainText(self.amando + self.raul + self.bonilla + self.jeremy + self.frida)

    def sel_jeremy(self):
        if self.cb_jeremy.isChecked():
            print("Jeremy True")
            self.jeremy = "JEREMY\n"
        else:
            print("Jeremy False")
            self.jeremy = ""
        self.txt_equipo.setPlainText(self.amando + self.raul + self.bonilla + self.jeremy + self.frida)


    def sel_frida(self):
        if self.cb_frida.isChecked():
            print("Frida True")
            self.frida = "FRIDA\n"
        else:
            print("Frida False")
            self.frida = ""
        self.txt_equipo.setPlainText(self.amando + self.raul + self.bonilla + self.jeremy + self.frida)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

