import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P_11_SliderWithTimers.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_iniciar.clicked.connect(self.iniciar)
        self.segundo = QtCore.QTimer()
        self.segundo.timeout.connect(self.carrusel)

        self.lista_imagenes = [
             ":/Logos/yo xd.jpg",
             ":/Logos/bonillas.jpeg",
             ":/Logos/amando xd.jpeg",
             ":/Logos/jeremias.jpeg",
             ":/Logos/foto.jpeg",
             ":/Logos/perro enojao xd.jpg"
        ]

    def iniciar(self):
        t = self.btn_iniciar.text()
        if t == "INICIAR":
            self.btn_iniciar.setText("DETENER")
            self.idx = 0
            self.segundo.start(500)
        else:
            self.btn_iniciar.setText("INICIAR")
            self.segundo.stop()

    def carrusel(self):
        self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.idx]))
        self.idx = (self.idx + 1)%len(self.lista_imagenes)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
