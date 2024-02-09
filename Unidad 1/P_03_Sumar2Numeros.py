import sys

import self
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_03_Sumar2Numeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_sumar.clicked.connect(self.sumar)
        self.txt_resultado.setEnabled(False)


    def sumar(self):
        num1 = int(self.txt_num1.text())
        num2 = int(self.txt_num2.text())
        resultado = num1 + num2
        self.txt_resultado.setText(str(resultado))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

