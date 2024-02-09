import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_04_EcuacionPrimerGrado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.ecuacion)

    def ecuacion(self):
       m = float(self.txt_m.text())
       b = float(self.txt_b.text())
       y = m * float(self.txt_x.text()) + b
       cadena = "El resultado es: " + str(y)
       msj = QtWidgets.QMessageBox()
       msj.setText(cadena)
       msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())