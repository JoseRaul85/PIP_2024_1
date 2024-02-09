import sys

import self
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_06_SumNumeros_V2_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_sumar.clicked.connect(self.sumar)
        self.txt_resultado.setEnabled(False)

    def sumar(self):
        #El usuario ingresa los numeros separados por espacios
        numeros = self.txt_numeros.text() #Entrada ejemplo: 1 2 3 4 5
        lista = numeros.split(" ") #Convierte la entrada de numeros en una lista ['1', '2', '3', '4', '5']
        print(lista)
        lista_en_numeros = [int(i) for i in lista] #Conversion de caracteres a numeros por lista de compresion
        print(lista_en_numeros)

        suma = sum(lista_en_numeros)
        self.txt_resultado.setText(str(suma))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

