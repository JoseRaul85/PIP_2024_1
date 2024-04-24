import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_13_SeleccionEquipo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.rb_amando.clicked.connect(self.clic_amando)
        self.rb_amando.toggled.connect(self.toggle_amando)

    def clic_amando(self):
        print("Hiciste clic en Amando")


    def toggle_amando(self):
        estado = self.rb_amando.isChecked()
        print(f"Amando cambio de estado (toggle). Nuevo Estado: {estado}")






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

