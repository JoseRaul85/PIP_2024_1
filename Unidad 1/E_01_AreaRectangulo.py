import sys
import self
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_01_AreaRectangulo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_area.clicked.connect(self.calcular)

    def calcular(self):
        base = int(self.txt_base.text())
        altura = int(self.txt_altura.text())
        area = base * altura
        cadena = "La base del rectangulo es: " + str(area)
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
