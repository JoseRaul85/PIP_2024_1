import sys
import self
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpAritmeticas.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_sumar.clicked.connect(self.operacion)
        self.btn_resta.clicked.connect(self.operacion)
        self.btn_multi.clicked.connect(self.operacion)
        self.btn_division.clicked.connect(self.operacion)
        self.txt_resultado.setEnabled(False)

    def operacion(self):
        try:
            objeto = self.sender()
            nombre = objeto.objectName()
            print(nombre)

            num1 = int(self.txt_num1.text())
            num2 = int(self.txt_num2.text())

            if nombre == "btn_sumar":
                resultado = num1 + num2
            elif nombre == "btn_resta":
                resultado = num1 - num2
            elif nombre == "btn_multi":
                resultado = num1 * num2
            elif nombre == "btn_division":
                resultado = num1 / num2

            self.txt_resultado.setText(str(resultado))
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

