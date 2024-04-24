import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P_12_CompararImagen.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_atras.clicked.connect(self.atras)
        self.btn_siguiente.clicked.connect(self.siguiente)
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.index_control = 0
        self.btn_atras.setEnabled(False)
        self.segundo = QtCore.QTimer()
        self.segundo.timeout.connect(self.carrusel)
        self.btn_validar.clicked.connect(self.validar)
        self.idx = 0

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
            self.segundo.start(100)
        else:
            self.btn_iniciar.setText("INICIAR")
            self.segundo.stop()

    def carrusel(self):
        self.idx = (self.idx + 1)%len(self.lista_imagenes)
        self.imagenPC.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.idx]))
        print(self.idx)

    def atras(self):
        if self.index_control > 0:
            self.index_control -= 1
            self.btn_siguiente.setEnabled(True)
            self.imagenUsu.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.index_control]))

        if self.index_control == 0:
            self.btn_atras.setEnabled(False)
        print(self.index_control)

    def siguiente(self):
        if self.index_control < len(self.lista_imagenes) - 1:
            self.btn_atras.setEnabled(True)
            self.index_control += 1
            self.imagenUsu.setPixmap(
                QtGui.QPixmap(self.lista_imagenes[self.index_control]))
        if self.index_control == len(self.lista_imagenes) - 1:
            self.btn_siguiente.setEnabled(False)

        print(self.index_control)


    def validar(self):
        res = self.index_control == self.idx
        msj = QtWidgets.QMessageBox()
        msj.setText(str(res))
        msj.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
