import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_08_DeterminarNota.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.determinar_nota)

    # Área de los Slots
    def determinar_nota(self):
        calificacion = float(self.txt_calificacion.text())
        if calificacion >= 9:
            nota = "A"
        elif calificacion >= 8:
            nota = "B"
        elif calificacion >= 7:
            nota = "C"
        elif calificacion >= 6:
            nota = "D"
        else:
            nota = "F"
        cadena = "La nota es: " + str(nota)
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())