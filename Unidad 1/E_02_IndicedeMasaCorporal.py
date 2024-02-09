import sys
import self
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_02_IndicedeMasaCorporal.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_indice.clicked.connect(self.masa)

    def masa(self):
        centimetros = float(self.txt_centimetro.text())
        peso = float(self.txt_peso.text())
        masa = peso / (centimetros ** 2)
        cadena = "Tu masa corporal es: " + str(masa)
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
