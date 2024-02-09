import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_05_CalculoPuntoMedio.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.calcularPuntoMedio)

    # Área de los Slots
    def calcularPuntoMedio(self):
        x1 = float(self.txt_punto1X.text())
        y1 = float(self.txt_punto1Y.text())
        x2 = float(self.txt_punto2X.text())
        y2 = float(self.txt_punto2Y.text())
        puntomedioX = (x1 + x2) / 2
        puntomedioY = (y1 + y2) / 2
        cadena = "El punto medio X es: " + str(puntomedioX) + " y el punto medio Y es: " + str(puntomedioY)
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())