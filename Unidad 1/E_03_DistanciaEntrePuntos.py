import sys
from PyQt5 import uic, QtWidgets
import math

qtCreatorFile = "E_03_DistanciaEntrePuntos.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.calcularDistancia)

    def calcularDistancia(self):
        x1 = float(self.txt_punto1x.text())
        y1 = float(self.txt_punto2x.text())
        x2 = float(self.txt_punto1y.text())
        y2 = float(self.txt_punto2y.text())
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        cadena = "La distancia es: " + str(distancia)
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())