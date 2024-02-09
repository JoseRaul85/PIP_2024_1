import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_06_PromedioCalificaciones.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.calcularPromedio)

    def calcularPromedio(self):
        cal1 = float(self.txt_calif1.text())
        cal2 = float(self.txt_calif2.text())
        cal3 = float(self.txt_calif3.text())
        cal4 = float(self.txt_calif4.text())
        cal5 = float(self.txt_calif5.text())
        promedio = (cal1 + cal2 + cal3 + cal4 + cal5) / 5
        cadena = "El promedio es: " + str(promedio)
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
