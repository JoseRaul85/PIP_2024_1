import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_07_CalcularFactorial.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.calculoFactorial)

    # Área de los Slots
    def calculoFactorial(self):
        numero = int(self.txt_numero.text())
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        cadena = "El factorial es: " + str(factorial)
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
